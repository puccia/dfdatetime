# -*- coding: utf-8 -*-
"""The date and time definitions.

Also see:
  https://en.wikipedia.org/wiki/Day
  https://en.wikipedia.org/wiki/Hour
  https://en.wikipedia.org/wiki/Minute
"""

from __future__ import unicode_literals


PRECISION_1_DAY = '1d'
PRECISION_1_HOUR = '1h'
PRECISION_1_NANOSECOND = '1ns'
PRECISION_100_NANOSECONDS = '100ns'
PRECISION_1_MICROSECOND = '1us'
PRECISION_1_MILLISECOND = '1ms'
PRECISION_100_MILLISECONDS = '100ms'
PRECISION_1_MINUTE = '1min'
PRECISION_1_SECOND = '1s'
PRECISION_2_SECONDS = '2s'

PRECISION_VALUES = frozenset([
    PRECISION_1_DAY,
    PRECISION_1_HOUR,
    PRECISION_1_NANOSECOND,
    PRECISION_100_NANOSECONDS,
    PRECISION_1_MICROSECOND,
    PRECISION_1_MILLISECOND,
    PRECISION_100_MILLISECONDS,
    PRECISION_1_MINUTE,
    PRECISION_1_SECOND,
    PRECISION_2_SECONDS])
