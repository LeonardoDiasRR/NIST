#!/usr/bin/python
# -*- coding: UTF-8 -*-

import contextlib

@contextlib.contextmanager
def supress( *exceptions ):
    try:
        yield
    except exceptions:
        pass

@contextlib.contextmanager
def noraise( ignoreraise = True ):
    try:
        yield
    except Exception as e:
        if not ignoreraise:
            raise e
