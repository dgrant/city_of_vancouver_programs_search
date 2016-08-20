#!/usr/bin/env python2

from decimal import Decimal
import time

import six
from six import print_
import django
django.setup()

#import logging
#l = logging.getLogger('django.db.backends')
#l.setLevel(logging.DEBUG)
#l.addHandler(logging.StreamHandler())

from annoying.functions import get_object_or_None

import json
import os

from cov_search.models import *

days = {}
progidset = set()

def y_n_to_boolean(y_or_n):
    if y_or_n == 'Y':
        return True
    elif y_or_n == 'N':
        return False
    else:
        raise Exception('field was not y_or_n, it was {0}'.format(y_or_n))

def clean_postalcode(postal_code):
    # Remove all spaces
    postal_code = ''.join(postal_code.split())
    assert len(postal_code) == 6
    return '{0} {1}'.format(postal_code[0:3], postal_code[3:6])

def init_days_of_week():
    for id, name in DAYS_OF_WEEK:
        day = get_object_or_None(Day, id=id)
        if not day:
            day = Day()
        day.id = id
        day.name = name
        if len(day.tracker.changed()) > 0:
            print_('Day {0} has changed'.format(day))
            print_('changed fields: ', day.tracker.changed())
            day.save()
        days[id] = day

def fee_to_decimal(fee):
    while fee[0] == '$':
        fee = fee[1:]
    fee = fee.replace(',', '')
    return Decimal(fee)

def print_diff(model_instance):
    changes = model_instance.tracker.changed()
    print_(six.u('{0} {1} ({2}) has changed: ').format(type(model_instance), model_instance.id, model_instance.name))
    for field_name in changes.keys():
        print_(six.u('    {0} old: {1}, new: {2}').format(field_name, changes[field_name], model_instance.__dict__[field_name]))

def suckin_activity(program_dict):
    # Site
    site = get_object_or_None(Site, id=program_dict['siteid'])
    if not site:
        print_('Couldn\'t find site with id/siteid {0}. Creating new one.'.format(program_dict['siteid']))
        site = Site()
    site.id = long(program_dict['siteid'])
    site.name = program_dict['site']
    site.address = program_dict['address']
    site.postalcode = clean_postalcode(program_dict['postalcode'])
    site.phone = program_dict['phone']

    if len(site.tracker.changed()) > 0:
        print_diff(site)
        site.save()

    # Season
    season = get_object_or_None(Season, name=program_dict['season'])
    if not season:
        print_('Couldn\'t find season with name {0}. Creating new one.'.format(program_dict['season']))
        season = Season()
        season.name = program_dict['season']
        season.save()

    # AgeGroup
    agegroup = get_object_or_None(AgeGroup, name=program_dict['agegroup'])
    if not agegroup:
        print_('Couldn\'t find agegroup with name {0}. Creating new one.'.format(program_dict['agegroup']))
        agegroup = AgeGroup()
        agegroup.name = program_dict['agegroup']
        agegroup.save()

    # ProgramType
    programtype = get_object_or_None(ProgramType, id=program_dict['activitytypeid'])
    if not programtype:
        print_('Couldn\'t find programtype with id/activitytypeid {0}. Creating new one.'.format(program_dict['activitytypeid']))
        programtype = ProgramType()
    programtype.id = long(program_dict['activitytypeid'])
    programtype.name = program_dict['programtype']

    if len(programtype.tracker.changed()) > 0:
        print_diff(programtype)
        programtype.save()

    # Category
    category = get_object_or_None(Category, id=program_dict['categoryid'])
    if not category:
        print_('Couldn\'t find category with id/categoryid {0}. Creating new one.'.format(program_dict['categoryid']))
        category = Category()
    category.id = long(program_dict['categoryid'])
    category.name = program_dict['programcategory']
    category.programtype = programtype

    if len(category.tracker.changed()) > 0:
        print_diff(category)
        category.save()


    # Instructor
    if not program_dict['instructorid'] == '':
        instructor = get_object_or_None(Instructor, id=program_dict['instructorid'])
        if not instructor:
            print_('Couldn\'t find instructor with id/instructorid {0}. Creating new one.'.format(program_dict['instructorid']))
            instructor = Instructor()
        instructor.id = long(program_dict['instructorid'])
        instructor.name = program_dict['instructor']

        if len(instructor.tracker.changed()) > 0:
            print_diff(instructor)
            instructor.save()
    else:
        instructor = None

    # Program
    if long(program_dict['activityid']) in progidset:
        print_(six.u('Already seen program {0} ({1})').format(program_dict['activityid'], program_dict['programname']))
    progidset.add(long(program_dict['activityid']))
    prog = get_object_or_None(Program, id=program_dict['activityid'])
    if not prog:
        prog = Program()
    prog.id = long(program_dict['activityid'])
    prog.site = site
    prog.number = program_dict['programnumber']
    prog.name = program_dict['programname']
    prog.membership = y_n_to_boolean(program_dict['membership'])
    prog.description = program_dict['description']
    prog.site = site
    prog.season = season
    prog.category = category
    prog.programtype = programtype
    prog.agegroup = agegroup
    prog.agemin = int(program_dict['agesmin'])
    prog.agemax = int(program_dict['agesmax'])
    prog.enrollmin = int(program_dict['enrollmin'])
    prog.enrollmax = int(program_dict['enrollmax'])
    prog.sessions = int(program_dict['sessions'])
    prog.numberopen = long(program_dict['numberopen'])
    prog.numberwaitlisted = int(program_dict['numberwaitlists'])
    prog.ignoremaximum = int(program_dict['ignoremaximum'])
    prog.maxenrolledonline = long(program_dict['maxenrolledonline'])
    prog.numberenrolledonline = long(program_dict['numberenrolledonline'])
    prog.dropin = y_n_to_boolean(program_dict['dropin'])
    prog.firstclass = y_n_to_boolean(program_dict['firstclass'])
    prog.onlinereg = y_n_to_boolean(program_dict['onlinereg'])
    prog.lac = y_n_to_boolean(program_dict['lac'])
    prog.fee = fee_to_decimal(program_dict['fee1'])
    prog.instructor = instructor

    if len(prog.tracker.changed()) > 0:
        print_diff(prog)
        prog.save()

    # Days
    for key, value in program_dict.iteritems():
        if key.startswith('day') and len(key) == 4:
            day_num = int(key[3])
            assert 1 <= day_num and day_num <= 7, 'day_num is {0}'.format(day_num)
            day_obj = days[day_num]
            if value != '':
                assert value == day_obj.name, 'expected value to be {0} but was {1}'.format(day_obj.name, value)
                prog.days.add(day_obj)


def suckin_file(path):
    with open(path) as fp:
        for program in json.loads(fp.read())['activities']:
            try:
                suckin_activity(program)
#                print_('.', end='', flush=True)
            except:
                print_('Problem while sucking in:', program)
#                from django.db import connection
#                for query in connection.queries[-1]:
#                    print_(query['sql'])
                raise

def suckin():
    init_days_of_week()
    for i, file in enumerate(os.listdir('json')):
        suckin_file(os.path.join('json', file))
    

if __name__ == '__main__':
#    import cProfile
#    cProfile.run('suckin()')
    suckin()
