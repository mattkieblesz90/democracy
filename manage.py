#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
    sys.path.append('conf/')
    sys.path.append('devops/fabric/')
    sys.path.append('src/django/')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
