# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
import logging
import click

from .. import lib

@click.command(short_help='short help')
@click.option('-j', '--processes', default=1, help='number of processes to run in parallel', type=click.IntRange(min=1, max=32))
@click.argument('files', nargs=-1, type=click.File('r'), required=True)
def cli(processes, files):
    """Align a list of text files."""
    assert len(files) % 2 == 0, "there must be as many files for each side"
    files1 = files[:files/2]
    files2 = files[files/2:]
    list1 = list(map(file_.read() for file_ in files1))
    list2 = list(map(file_.read() for file_ in files2))
    res, dst = lib.match(list1, list2, workers=processes)
    for ind1, ind2 in enumerate(res):
        score = dst[ind1]
        print(list1[ind1] + '|' + list2[ind2] + '[' + score + ']')

if __name__ == '__main__':
    cli()
