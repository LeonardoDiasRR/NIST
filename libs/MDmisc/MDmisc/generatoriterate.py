#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def generatoriterate( *iterators ):
    for i in iterators:
        for value in i:
            yield  value
