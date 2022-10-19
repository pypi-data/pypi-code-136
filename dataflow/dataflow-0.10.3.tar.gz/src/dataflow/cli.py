# Copyright (C) 2022 ALBA Synchrotron
#
# This file is part of dataflow
#
# dataflow is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dataflow is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dataflow.  If not, see <http://www.gnu.org/licenses/>.

"""
DataFlow CLI
------------

This command line interface allows to interact with DataFlow API from a
custom shell
"""

import argparse
import cmd
import readline  # noqa: F401 # pylint: disable=unused-import

from dataflow.jobs import job_service


class RunCmd(cmd.Cmd):
    """
    CLI run command
    """

    intro = r"""
       ___        __       _____             __
 _____/ _ \___   / /___   / _/ /__ _    _____\ \
/____/ // / _ \ / _/ _ \ / _/ / _ \ |/|/ /____  )
    /___ /\__,_/_/ \__,_/_//_/\___/__,__/    /_/

"""
    prompt = "-DF->"
    use_rawinput = True

    def __init__(self):
        super().__init__()
        self.args = None
        self.job = None

    def do_list(self, _):
        """
        List available jobs
        """
        list_jobs()

    def do_submit(self, message):
        """
        Send message to start a new task in the workflow.
        """
        if message:
            self.job.submit(*self.parse(message))
        else:
            print("No message to be sent.")

    def do_send(self, message):
        """
        Send message to an operation in the workflow.
        Use an arrow to specify the operator.
        e.g.:
            send message -> task_id:operator
        """
        if message:
            target = ""
            task_id = ""
            if "->" in message:
                message, task_id, *_ = message.split("->")
                if ":" in target:
                    task_id, target, *_ = task_id.split(":")
            message = message.strip()
            target = target.strip()
            task_id = task_id.strip()
            if target == "":
                target = None
            if task_id == "":
                task_id = None
            else:
                task_id = int(task_id)
            task_id = self.job.send(*self.parse(message),
                                    target=target,
                                    task_id=task_id)
        else:
            print("No message to be sent.")

    def do_done(self, _):
        """
        Set the workflow as done. The job will not accept more data.
        """
        self.job.done()
        # Print final prompt for parsing
        print(self.prompt)
        return True

    def run(self, args):
        """
        Create the job and run the shell
        """
        self.args = args
        self.job = job_service.create(self.args.jobname)
        self.job.prepare()
        self.cmdloop()

    def emptyline(self):
        """
        Action to be done when an empty message is passed.

        This overrides repeating last action, as implemented in Cmd class.
        """

    def default(self, line):
        """
        Default action when the message is unknown.
        """
        print("Unknown command: ", line)
        self.do_help("")

    def parse(self, message):
        """
        Parse message content
        """
        return tuple(message.strip().split())


def list_jobs(_=None):
    """
    List available jobs
    """
    print(" ".join(list(job_service.jobs.keys())))


def run_parser(subparser):
    """
    Subparser for run command
    """
    run = subparser.add_parser("run", help="Run the specified job")
    run.add_argument("jobname", type=str, help="Job name")
    run.set_defaults(func=RunCmd().run)


def list_parser(subparser):
    """
    Subparser for list command
    """
    joblist = subparser.add_parser("list", help="List available job")
    joblist.set_defaults(func=list_jobs)


def main(args=None):
    """
    DataFlow command line interface
    """
    parser = argparse.ArgumentParser(prog="dataflow")
    subparser = parser.add_subparsers(help="dataflow commands")
    run_parser(subparser)
    list_parser(subparser)

    args = parser.parse_args(args)
    if len(vars(args)) > 0:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
