#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Copyright (C) 2011-2012 Bryce Harrington <bryce@bryceharrington.org>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from time import sleep
from subprocess import (Popen, PIPE)

from .debug import dbg
from .text import o2str


class ReturnCode(BaseException):
    def __init__(self, code, errors=None):
        self.code = code
        if type(errors) in (list, tuple):
            self.errors = errors
        else:
            self.errors = [errors]

    def __str__(self):
        text = '\n'.join(self.errors)
        return f"{text}Returned error code {self.code}"


def shell(command, in_text=None):
    """Executes command in a shell, returns stdout, raises exception on error"""
    dbg(f"shell: {command}")
    if in_text:
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        output, errors = p.communicate(input=in_text)
    else:
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        output, errors = p.communicate()
    if p.returncode:
        raise ReturnCode(p.returncode, o2str(errors))
    return o2str(output)


def execute(command, in_text=None):
    """Executes command, returns stdout; prints errors to stderr"""
    dbg(f"execute: `{command}`")
    if in_text is None:
        p = Popen(command, shell=False, stdout=PIPE, stderr=PIPE)
    else:
        p = Popen(command, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        dbg(f"execute: polling ({in_text})...")
        while p.poll() is None and p.stdin is not None:
            dbg("execute: Sending to process stdin")
            p.stdin.write(in_text)
            dbg("execute: sleeping")
            sleep(0.01)
    output = p.stdout.read()
    if p.returncode:
        dbg(f"Received return code {p.returncode}")
        raise ReturnCode(p.returncode, p.stderr.readlines())
    return o2str(output)


def execute_with_input(command, in_text):
    """Executes command, passing in_text to stdin if provided"""
    execute(command, in_text)
