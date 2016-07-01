import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "conf.settings")

from development_fabfile.fabfile import *
from devops.fabric import *
