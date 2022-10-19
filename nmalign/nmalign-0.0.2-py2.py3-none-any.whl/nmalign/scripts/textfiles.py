# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
import click

from . import OptionEatAll
from ..lib import align

@click.command(short_help='short help')
@click.option('-j', '--processes', default=1, help='number of processes to run in parallel', type=click.IntRange(min=1, max=32))
@click.option('-s', '--strings', is_flag=True, help='print strings themselves instead of list indices')
@click.option('-S', '--separator', default='\t', help='print this string between result columns')
#@click.option('--files1', cls=OptionEatAll, type=click.File('r'), required=True)
@click.option('--files1', cls=OptionEatAll, type=tuple, required=True)
@click.option('--files2', cls=OptionEatAll, type=tuple, required=True)
def cli(processes, strings, separator, files1, files2):
    """Align a list of text files."""
    #list1 = list(map(file_.read() for file_ in files1))
    list1 = [open(filename, 'r').read() for filename in files1]
    list2 = [open(filename, 'r').read() for filename in files2]
    res, dst = align.match(list1, list2, workers=processes)
    for ind1, ind2 in enumerate(res):
        score = dst[ind1]
        if ind2 < 0:
            continue
        if strings:
            a = list1[ind1]
            b = list2[ind2]
        else:
            a = ind1
            b = ind2
        click.echo(a + separator + b + separator + score)

if __name__ == '__main__':
    cli()
