#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from __future__ import print_function
import sys

def eprint( *args, **kwargs ):
    print( *args, file = sys.stderr, **kwargs )
