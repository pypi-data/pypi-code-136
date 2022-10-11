#!/usr/bin/env python
# encoding: utf-8
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2018 Research Group Biomedical Physics,
# Max-Planck-Institute for Dynamics and Self-Organization Göttingen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#

import argparse
import logging
import os
import math
import sys
import re
from argparse import ArgumentParser
from tempfile import NamedTemporaryFile

import shutil
import caosdb as db

logger = logging.getLogger(__name__)
timeout_fallback = 20


def convert_size(size):
    if (size == 0):
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1000)))
    p = math.pow(1000, i)
    s = round(size / p, 2)

    return '%s %s' % (s, size_name[i])


def combine_ignore_files(caosdbignore, localignore, dirname=None):
    """appends the contents of localignore to caosdbignore and saves the result
    and returns the name

    """

    tmp = NamedTemporaryFile(delete=False, mode="w",
                             dir=dirname, prefix=".caosdbignore")
    with open(caosdbignore, "r") as base:
        tmp.write(base.read())
    with open(localignore, "r") as local:
        tmp.write(local.read())
    tmp.close()
    return tmp.name


def compile_file_list(caosdbignore, localpath):
    """creates a list of files that contain all files under localpath except
    those excluded by caosdbignore

    """

    from gitignore_parser import parse_gitignore
    matches = parse_gitignore(caosdbignore)
    current_ignore = caosdbignore
    non_ignored_files = []
    ignore_files = []
    for root, dirs, files in os.walk(localpath):
        # remove local ignore files that do no longer apply to the current subtree (branch switch)
        while len(ignore_files) > 0 and not root.startswith(ignore_files[-1][0]):
            shutil.os.remove(ignore_files[-1][1])
            ignore_files.pop()

        # use the global one if there are no more local ones
        if len(ignore_files) > 0:
            current_ignore = ignore_files[-1][1]
            matches = parse_gitignore(current_ignore)
        else:
            current_ignore = caosdbignore
            matches = parse_gitignore(current_ignore)

        # create a new local ignore file
        if ".caosdbignore" in files:
            current_ignore = combine_ignore_files(current_ignore,
                                                  os.path.join(
                                                      root, ".caosdbignore"),
                                                  # due to the logic of gitignore_parser the file
                                                  # has to be written to this folder
                                                  dirname=root)
            ignore_files.append((root, current_ignore))
            matches = parse_gitignore(current_ignore)

        # actually append files that are not ignored
        for fi in files:
            fullpath = os.path.join(root, fi)
            if not matches(fullpath):
                non_ignored_files.append(fullpath)
    return non_ignored_files


def create_re_for_file_list(files, localroot, remoteroot):
    """creates a regular expression that matches file paths contained in the
    files argument and all parent directories. The prefix localroot is replaced
    by the prefix remoteroot.

    """
    regexp = ""
    for fi in files:
        path = fi
        reg = ""
        while path != localroot and path != "/" and path != "":
            print(path, localroot)
            reg = "(/"+re.escape(os.path.basename(path)) + reg + ")?"
            path = os.path.dirname(path)
        regexp += "|" + re.escape(remoteroot) + reg
    return "^("+regexp[1:]+")$"


def loadpath(path, include, exclude, prefix, dryrun, forceAllowSymlinks, caosdbignore=None,
             localpath=None):

    if caosdbignore:
        # create list of files and create regular expression for small chunks
        filelist = compile_file_list(caosdbignore, localpath)
        fulllist = filelist

        index = 0
        step_size = 3
        includes = []
        while index < len(fulllist):
            subset = fulllist[index:min(index+step_size, len(fulllist))]
            includes.append(create_re_for_file_list(subset, localpath, path))
            index += step_size
    else:
        includes = [include]

    # if no caosdbignore file is used, this iterates over a single include
    for include in includes:
        if dryrun:
            logger.info("Performin a dryrun!")
            files = db.Container().retrieve(
                unique=False,
                raise_exception_on_error=True,
                flags={"InsertFilesInDir": ("-p " + prefix + " " if prefix else "")
                       + ("-e " + exclude + " " if exclude else "")
                       + ("-i " + include + " " if include else "")
                       + ("--force-allow-symlinks " if forceAllowSymlinks else "")
                       + path})
        else:
            # new files (inserting them using the insertFilesInDir feature of
            # the server, which inserts files via symlinks)
            files = db.Container().insert(
                unique=False,
                raise_exception_on_error=True,
                flags={"InsertFilesInDir": ("-p " + prefix + " " if prefix else "")
                       + ("-e " + exclude + " " if exclude else "")
                       + ("-i " + include + " " if include else "")
                       + ("--force-allow-symlinks " if forceAllowSymlinks else "")
                       + path})

        totalsize = 0  # collecting total size of all new files

        for f in files:
            totalsize += f.size

        print("Made in total {} new files with a combined size of {} "
              "accessible.".format(len(files), convert_size(totalsize)))
        logger.info("Made in total {} new files with a combined size of {} "
                    "accessible.".format(len(files), convert_size(totalsize)))

    return


def main(argv=None):
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    # Setup argument parser
    parser = ArgumentParser()
    parser.add_argument("-p", "--prefix", dest="prefix",
                        help="store files with this prefix into the server's"
                        " file system.")
    parser.add_argument("-c", "--caosdbignore", help="""
Path to a caosdbignore file that defines which files shall be included and which do not.
The syntax is the same as in a gitignore file. You must also provide the localpath option
since the check is done locally.
"""
                        )
    parser.add_argument("-l", "--localpath", help="Path to the root directory on this machine. "
                        "This is needed if a caosdbignore file is used since the check is done "
                        "locally")
    parser.add_argument("-i", "--include", dest="include",
                        help="""
only include paths matching this regex pattern.
Note: The provided directory tree is traversed from its root. I.e. a pattern
like "/some/path/*.readme" will lead to no loading when called on "/some" as the
re does not match "/some". If you want to match some file, make sure the parent
directories are matched. E.g. -i "(/some|/some/path|.*readme).
exclude is given preference over include.
                        """,
                        metavar="RE")
    parser.add_argument("-e", "--exclude", dest="exclude",
                        help="exclude paths matching this regex pattern.",
                        metavar="RE")
    parser.add_argument("-d", "--dry-run", dest="dryrun", action="store_true",
                        help="Just simulate the insertion of the files.")
    parser.add_argument('-t', '--timeout', dest="timeout",
                        help="timeout in seconds for the database requests. "
                        "0 means no timeout. [defaults to the global "
                        "setting, else to {timeout_fallback}s: "
                        "%(default)s]".format(
                            timeout_fallback=timeout_fallback),
                        metavar="TIMEOUT",
                        default=db.get_config().get("Connection", "timeout",
                                                    fallback=timeout_fallback))
    parser.add_argument(dest="path",
                        help="path to folder with source file(s) "
                        "[default: %(default)s]", metavar="path")
    parser.add_argument("--force-allow-symlinks", dest="forceAllowSymlinks",
                        help="Force the processing of symlinks. By default, "
                        "the server will ignore symlinks in the inserted "
                        "directory tree.", action="store_true")
    args = parser.parse_args()

    if args.caosdbignore and (args.exclude or args.include):
        raise ValueError(
            "Do not use a caosdbignore file and in- or exclude simultaneously!")

    if args.caosdbignore and not args.localpath:
        raise ValueError("To use caosdbignore you must supply a local path!")

    if args.localpath and (args.exclude or args.include):
        raise ValueError(
            "Do not use a localpath and in- or exclude simultaneously!")

    con = db.get_connection()
    con.timeout = float(args.timeout)
    con._login()

    loadpath(
        path=args.path,
        include=args.include,
        exclude=args.exclude,
        prefix=args.prefix,
        dryrun=args.dryrun,
        forceAllowSymlinks=args.forceAllowSymlinks,
        caosdbignore=args.caosdbignore,
        localpath=args.localpath,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
