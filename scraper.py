from pycommon import http
import argparse
import json
import os
from six.moves.queue import Queue
from threading import Thread
import itertools
import shutil

from six import print_

CONCURRENT = 16
MAX = 500
ROOT = os.path.split(os.path.abspath(__file__))[0]
URL = 'http://app.vancouver.ca/SafariActivityListWR_net/default.aspx'
PARAMS = {'g': 1, 'pg': 1, 'op': 0, 'x': 'C', 't': -1, 'd': -1, 'a': -1, 'l': -1, 'ft': -1, 'c': 0, 'pp': 0, 's': ''}
JSON_DIR = os.path.join(ROOT, 'json')

counter = itertools.count(1)
q = Queue(CONCURRENT * 2)

def getfilepath(page):
    return os.path.join(JSON_DIR, 'data_{0:05d}.json'.format(page))

def doWork():
    while True:
        page = q.get()
        scrape_page(page)
#        next_page = next(counter)
#        if next_page < MAX:
#            q.put(next_page)
        q.task_done()

for i in range(CONCURRENT):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

def scrape_page(page):
    print_('Scraping page {0}'.format(page))
    if os.path.exists(getfilepath(page)):
        print_("Scraping page {0}...already done".format(page))
        return True
    params = PARAMS.copy()
    params['pg'] = page
    print('URL=', URL)
    output = http.do_http_get(URL, params=params)
    try:
        json_str = json.loads(output)
    except ValueError:
        print_('output=', output)
        raise
    if len(json_str['activities']) == 0:
        print_("Scraping page {0}...no activities".format(page))
        return False
    else:
        path = getfilepath(page)
        with open(path, 'w') as fp:
            json.dump(json_str, fp, indent=3, sort_keys=True)
        print_("Scraping page {0}...done".format(page))
        return True

def scrape():
    shutil.rmtree('json')
    os.makedirs('json')
#    for i in range(CONCURRENT):
    for i in range(MAX):
        q.put(next(counter))
    q.join()

def main():
    parser = argparse.ArgumentParser(description="Scrape City of Vancouver website")
    args = parser.parse_args()

    scrape()

if __name__ == '__main__':
    scrape()
