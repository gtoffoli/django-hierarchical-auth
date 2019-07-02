#!/usr/bin/env python

import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'hierarchical_auth.tests.test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))

sys.path.insert(0, parent)

from django.test.runner import DiscoverRunner
from django.conf import settings

# Possibly broken
def runtests():
    failures = DiscoverRunner.run_tests(['tests'], verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

