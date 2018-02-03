# -*- coding: utf-8 -*-

"""Top-level package for FEAT."""

from __future__ import absolute_import

__author__ = """Jin Hyun Cheong, Nathaniel Hanes, Luke Chang """
__email__ = 'jcheong0428@gmail.com'
version = {}
with open("nltools/version.py") as f:
    exec(f.read(), version)
__version__ = version['__version__'],

__all__ = ['data',]

from .data import (Fex)
