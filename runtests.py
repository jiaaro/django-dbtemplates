#!/usr/bin/env python
import os
import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DBTEMPLATES_CACHE_BACKEND = 'dummy://',
        DATABASE_ENGINE='sqlite3',
        SITE_ID=1,
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'dbtemplates',
        ],
    )

from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['dbtemplates']
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dbtemplates'))
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
