#!/usr/bin/env python

from . import *

try:
    from .version import __version__
except:
    __version__ = "dev"