"""firmatazero"""

__version__ = "0.0.1"

# firmatazero: a library for controlling Arduino's pins from Python, using Firmata protocol
# Copyright (C) Olli Paloviita 2022 <olli.paloviita@gmail.com>
#
# Heavily inspired by GPIO Zero library: https://github.com/gpiozero/gpiozero/tree/master/gpiozero
# This project aims to bring the same Python interface to Arduino. This means that the
# structure and docstrings are very related, even if the underlying code is different.

# GPIO Zero's copyright from __init__.py:
#
# GPIO Zero: a library for controlling the Raspberry Pi's GPIO pins
#
# Copyright (c) 2015-2021 Dave Jones <dave@waveform.org.uk>
# Copyright (c) 2015-2021 Ben Nuttall <ben@bennuttall.com>
# Copyright (c) 2019 tuftii <3215045+tuftii@users.noreply.github.com>
# Copyright (c) 2019 Jeevan M R <14.jeevan@gmail.com>
# Copyright (c) 2019 ForToffee <ForToffee@users.noreply.github.com>
# Copyright (c) 2018 Claire Pollard <claire.r.pollard@gmail.com>
# Copyright (c) 2016 pcopa <scheltovandoorn@gmail.com>
# Copyright (c) 2016 Ian Harcombe <ian.harcombe@gmail.com>
# Copyright (c) 2016 Andrew Scheller <github@loowis.durge.org>
# Copyright (c) 2016 Andrew Scheller <lurch@durge.org>
# Copyright (c) 2015 Philip Howard <phil@gadgetoid.com>
#
# SPDX-License-Identifier: BSD-3-Clause

from .output_devices import LED, Servo
from .shared_board import detect_port, get_board, set_board, set_port
