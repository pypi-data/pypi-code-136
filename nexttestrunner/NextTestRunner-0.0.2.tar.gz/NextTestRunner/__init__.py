#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|

"""

import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0,BASE_DIR)


__all__ = [
    "Email",
    "nextEmail",
    "send_email",
]


from main import send_email
from main import (Email, nextEmail, )

