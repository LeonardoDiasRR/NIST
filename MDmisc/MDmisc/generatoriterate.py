#!/usr/bin/python
# -*- coding: UTF-8 -*-

def generatoriterate( *iterators ):
    for i in iterators:
        for value in i:
            yield  value
