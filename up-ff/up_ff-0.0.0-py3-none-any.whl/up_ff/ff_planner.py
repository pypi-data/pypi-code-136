import pkg_resources # type: ignore
import unified_planning as up
from unified_planning.engines.results import PlanGenerationResultStatus
from unified_planning.model import ProblemKind
from unified_planning.engines import PDDLPlanner, Credits, LogMessage
from typing import Optional, List, Union
import os,sys,subprocess
from unified_planning.io.pddl_writer import PDDLWriter
import asyncio
from asyncio.subprocess import PIPE
import select
import subprocess
import sys
import tempfile
import os
import re
import time
import unified_planning.engines as engines
import unified_planning.engines.mixins as mixins
from unified_planning.engines.results import (
    LogLevel,
    LogMessage,
    PlanGenerationResult,
    PlanGenerationResultStatus,
)
import asyncio
from asyncio.subprocess import PIPE
import select
import subprocess
import sys
import tempfile
import os
import re
import time
import unified_planning as up
import unified_planning.engines as engines
import unified_planning.engines.mixins as mixins
from unified_planning.engines.results import (
    LogLevel,
    LogMessage,
    PlanGenerationResult,
    PlanGenerationResultStatus,
)
from unified_planning.io.pddl_writer import PDDLWriter
from unified_planning.exceptions import UPException
from asyncio.subprocess import PIPE
from fractions import Fraction
from typing import IO, Any, Callable, Optional, List, Tuple, Union, cast


credits = Credits('FF',
                  'Jorg Hoffmann',
                  '',
                  '',
                  'GPL',
                  'Classical Planner',
                  '')

class FFEngine(PDDLPlanner):

    def __init__(self):
        super().__init__(needs_requirements=False)
        
    @property
    def name(self) -> str:
        return 'ff'

    def _get_cmd(self, domain_filename: str, problem_filename: str) -> List[str]:
        base_command = [pkg_resources.resource_filename(__name__, 'FF/ff'), '-o', domain_filename, '-f', problem_filename]
        return base_command
    def _plan_from_file(
        self,
        problem: "up.model.Problem",
        plan_filename: str,
        get_item_named: Callable[
            [str],
            Union[
                "up.model.Type",
                "up.model.Action",
                "up.model.Fluent",
                "up.model.Object",
                "up.model.Parameter",
                "up.model.Variable",
            ],
        ],
    ) -> "up.plans.Plan":
        """
        Takes a problem, a filename and a map of renaming and returns the plan parsed from the file.

        :param problem: The up.model.problem.Problem instance for which the plan is generated.
        :param plan_filename: The path of the file in which the plan is written.
        :param get_item_named: A function that takes a name and returns the original up.model element instance
            linked to that renaming.
        :return: The up.plans.Plan corresponding to the parsed plan from the file
        """
        actions: List = []
        solved = False
        with open(plan_filename) as plan:
            for line in plan.readlines():
                if "found legal plan" in line:
                    solved = True
                elif re.match(r".*\d+:.*",line):
                    whole_action = line.strip().lower().split(": ")[1]
                    l = whole_action.split(" ")
                    action = get_item_named(l[0])
                    params_name = []
                    if len(l)>1:
                        params_name = whole_action.split(" ")[1:]
                    assert isinstance(action, up.model.Action), "Wrong plan or renaming."
                    parameters = []
                    for p in params_name:
                        obj = get_item_named(p)
                        assert isinstance(obj, up.model.Object), "Wrong plan or renaming."
                        parameters.append(problem.env.expression_manager.ObjectExp(obj))
                    act_instance = up.plans.ActionInstance(action, tuple(parameters))
                    actions.append(act_instance)
        if not solved:
            return None
        return up.plans.SequentialPlan(actions)

    def _solve(
        self,
        problem: "up.model.AbstractProblem",
        callback: Optional[
            Callable[["up.engines.results.PlanGenerationResult"], None]
        ] = None,
        timeout: Optional[float] = None,
        output_stream: Optional[IO[str]] = None,
    ) -> "up.engines.results.PlanGenerationResult":
        assert isinstance(problem, up.model.Problem)
        w = PDDLWriter(problem, self._needs_requirements)
        plan = None
        logs: List["up.engines.results.LogMessage"] = []
        with tempfile.TemporaryDirectory() as tempdir:
            domain_filename = os.path.join(tempdir, "domain.pddl")
            problem_filename = os.path.join(tempdir, "problem.pddl")
            plan_filename = os.path.join(tempdir, "plan.txt")
            w.write_domain(domain_filename)
            w.write_problem(problem_filename)
            cmd = self._get_cmd(domain_filename, problem_filename)

            if output_stream is None:
                # If we do not have an output stream to write to, we simply call
                # a subprocess and retrieve the final output and error with communicate
                process = subprocess.Popen(
                    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                timeout_occurred: bool = False
                proc_out: List[str] = []
                proc_err: List[str] = []
                try:
                    out_err_bytes = process.communicate(timeout=timeout)
                    proc_out, proc_err = [[x.decode()] for x in out_err_bytes]
                except subprocess.TimeoutExpired:
                    timeout_occurred = True
                print(plan_filename)
                with open(plan_filename,'w') as f:
                    for l in proc_out:
                        f.write(l.strip())

                retval = process.returncode
            else:
                if sys.platform == "win32":
                    # On windows we have to use asyncio (does not work inside notebooks)
                    try:
                        loop = asyncio.ProactorEventLoop()
                        exec_res = loop.run_until_complete(
                            run_command_asyncio(
                                cmd, output_stream=output_stream, timeout=timeout
                            )
                        )
                    finally:
                        loop.close()
                else:
                    # On non-windows OSs, we can choose between asyncio and posix
                    # select (see comment on USE_ASYNCIO_ON_UNIX variable for details)
                    if USE_ASYNCIO_ON_UNIX:
                        exec_res = asyncio.run(
                            run_command_asyncio(
                                cmd, output_stream=output_stream, timeout=timeout
                            )
                        )
                    else:
                        exec_res = run_command_posix_select(
                            cmd, output_stream=output_stream, timeout=timeout
                        )
                timeout_occurred, (proc_out, proc_err), retval = exec_res

            logs.append(up.engines.results.LogMessage(LogLevel.INFO, "".join(proc_out)))
            logs.append(
                up.engines.results.LogMessage(LogLevel.ERROR, "".join(proc_err))
            )
            if os.path.isfile(plan_filename):
                plan = self._plan_from_file(problem, plan_filename, w.get_item_named)
            if timeout_occurred and retval != 0:
                return PlanGenerationResult(
                    PlanGenerationResultStatus.TIMEOUT,
                    plan=plan,
                    log_messages=logs,
                    engine_name=self.name,
                )
        status: PlanGenerationResultStatus = self._result_status(
            problem, plan, retval, logs
        )
        return PlanGenerationResult(
            status, plan, log_messages=logs, engine_name=self.name
        )


    def _result_status(
        self,
        problem: 'up.model.Problem',
        plan: Optional['up.plans.Plan'],
        retval: int = 0,
        log_messages: Optional[List['LogMessage']] = None,
    ) -> 'PlanGenerationResultStatus':
        
        print(log_messages)
        if retval != 0:
            return PlanGenerationResultStatus.INTERNAL_ERROR
        elif plan is None:
            return PlanGenerationResultStatus.UNSOLVABLE_PROVEN
        else:
            return PlanGenerationResultStatus.SOLVED_SATISFICING

    @staticmethod
    def supported_kind() -> 'ProblemKind':
        supported_kind = ProblemKind()
        supported_kind.set_problem_class('ACTION_BASED')  # type: ignore
        supported_kind.set_numbers('CONTINUOUS_NUMBERS')  # type: ignore
        supported_kind.set_numbers('DISCRETE_NUMBERS')  # type: ignore
        supported_kind.set_typing('FLAT_TYPING')  # type: ignore
        supported_kind.set_typing('HIERARCHICAL_TYPING')  # type: ignore
        supported_kind.set_fluents_type('NUMERIC_FLUENTS')  # type: ignore
        supported_kind.set_conditions_kind('NEGATIVE_CONDITIONS')  # type: ignore
        supported_kind.set_conditions_kind('DISJUNCTIVE_CONDITIONS')  # type: ignore
        supported_kind.set_conditions_kind('EXISTENTIAL_CONDITIONS')  # type: ignore
        supported_kind.set_conditions_kind('UNIVERSAL_CONDITIONS')  # type: ignore
        supported_kind.set_conditions_kind('EQUALITY')  # type: ignore
        supported_kind.set_problem_type('SIMPLE_NUMERIC_PLANNING')  # type: ignore
        supported_kind.set_problem_type('GENERAL_NUMERIC_PLANNING')  # type: ignore
        supported_kind.set_effects_kind('INCREASE_EFFECTS')  # type: ignore
        supported_kind.set_effects_kind('DECREASE_EFFECTS')  # type: ignore
        supported_kind.set_effects_kind('CONDITIONAL_EFFECTS')  # type: ignore
        supported_kind.set_quality_metrics("ACTIONS_COST")
        supported_kind.set_quality_metrics("PLAN_LENGTH")
        return supported_kind

    @staticmethod
    def supports(problem_kind: 'ProblemKind') -> bool:
        return problem_kind <= FFEngine.supported_kind()

    @staticmethod
    def get_credits(**kwargs) -> Optional['Credits']:
        return credits