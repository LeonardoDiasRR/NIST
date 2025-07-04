#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Expose modules from the nested 'MDmisc' package at the top level so that
# imports such as ``MDmisc.deprecated`` work without modifying ``sys.path``.
# Re-export common helpers from the nested ``MDmisc`` package.  This mirrors the
# historical layout expected by code in :mod:`NIST` which imports modules such as
# ``MDmisc.deprecated`` directly from this package.
import os

# Include the nested ``MDmisc`` directory in the package search path so that
# modules like ``MDmisc.boxer`` can be resolved correctly.
__path__.append(os.path.join(os.path.dirname(__file__), 'MDmisc'))

from .MDmisc.deprecated import deprecated  # noqa:F401
