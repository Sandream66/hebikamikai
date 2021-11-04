# -*- coding: utf-8 -*-
# !/usr/bin/env python

import random
from enum import Enum, unique

@unique
class Result(Enum):
    success = 1
    failure = 0
