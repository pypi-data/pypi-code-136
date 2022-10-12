#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from j5basic import WithContextSkip
import inspect
import logging
import threading
import sys

block_event_lock = threading.Lock()
block_events = {}

@WithContextSkip.conditionalcontextmanager
def only_thread(thread_name):
    """Runs the controlled block only if the current thread has the given name - otherwise skips it"""
    if thread_name == threading.current_thread().name:
        yield
    else:
        raise WithContextSkip.SkipStatement()

@WithContextSkip.conditionalcontextmanager
def only_thread_blocking(thread_name, block_name):
    """Runs the controlled block only if the current thread has the given name - otherwise skips it. Wait for the given thread to run the block before allowing other threads to proceed"""
    with block_event_lock:
        block_event = block_events.setdefault(block_name, threading.Event())
    current_thread_name = threading.current_thread().name
    if thread_name == current_thread_name:
        logging.info("thread %s will run %s", thread_name, block_name)
        yield
        logging.info("thread %s ran %s", thread_name, block_name)
        block_event.set()
        logging.info("thread %s has set event %s", thread_name, block_name)
    else:
        logging.info("thread %s will wait for event %s", thread_name, block_name)
        block_event.wait()
        logging.info("thread %s has received event %s and will skip the block", thread_name, block_name)
        raise WithContextSkip.SkipStatement()

