#!/bin/sh
rm -rf env
virtualenv -p pypy env
env/bin/pip install -r requirements.txt
