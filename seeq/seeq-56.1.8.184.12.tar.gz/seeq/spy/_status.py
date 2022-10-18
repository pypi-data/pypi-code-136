from __future__ import annotations

import concurrent.futures
import datetime
import queue
import re
import threading
from typing import Tuple, Callable, Dict, Optional

import pandas as pd
from IPython.display import display, HTML
from seeq.spy import _common, _datalab
from seeq.spy._errors import *
from seeq.spy._session import Session


class Status:
    """
    Tracks the progress status of various SPy functions.

    Parameters
    ----------
    quiet : bool, default False
        If True, suppresses progress output. Supersedes the quiet flag
        of any function the status is passed to.
    """

    RUNNING = 0
    SUCCESS = 1
    FAILURE = 2
    CANCELED = 3

    jobs: Dict[object, Tuple[Tuple, Optional[Callable[[object, object], None]]]]

    def __init__(self, quiet: bool = False, errors: Optional[str] = None):
        self.quiet = quiet
        self.errors = errors if errors is not None else 'raise'
        self._catalogued_errors = set()
        self._df = pd.DataFrame()
        self.timer = _common.timer_start()
        self.message = None
        self.code = None
        self.warnings = set()
        self.printed_warnings = set()
        self.inner = dict()
        self.update_queue = queue.Queue()
        self.interrupted_event = threading.Event()
        self.jobs = dict()
        self.current_df_index = None

    def __str__(self):
        return self.message if self.message else 'Uninitialized'

    def __getstate__(self):
        # We can only pickle certain members. This has to mirror __setstate__().
        return self.quiet, self.df, self.message, self.code, self.warnings, self.inner

    def __setstate__(self, state):
        self.quiet, self.df, self.message, self.code, self.warnings, self.inner = state

    @property
    def df(self) -> pd.DataFrame:
        """
        DataFrame containing info about the results of the SPy function
        using this Status object
        """
        _common.clear_properties_on_df(self._df)
        return self._df

    @df.setter
    def df(self, value: pd.DataFrame):
        self._df = value.copy()
        _common.clear_properties_on_df(self._df)

    def create_inner(self, name: str, quiet: bool = None, errors: str = None):
        inner_status = Status(quiet=self.quiet if quiet is None else quiet,
                              errors=self.errors if errors is None else errors)
        self.inner[name] = inner_status
        return inner_status

    def metrics(self, d):
        self.df = pd.DataFrame(d).transpose()

    def put(self, column, value):
        self.df.at[self.current_df_index, column] = value

    def get(self, column):
        return self.df.at[self.current_df_index, column]

    def warn(self, warning):
        self.warnings.add(warning)

    def raise_or_catalog(self, exception, *, force_catalog=False):
        if isinstance(exception, str):
            exception = SPyRuntimeError(exception)

        if force_catalog or self.errors == 'catalog':
            self._catalogued_errors.add(_common.format_exception(exception))
        else:
            raise exception

    def catalog_error(self, exception):
        self.raise_or_catalog(exception, force_catalog=True)

    @property
    def catalogued_errors(self):
        return self._catalogued_errors

    @property
    def catalogued_errors_str(self):
        return 'Errors encountered:\n' + \
               '\n----------------------------------------\n'.join(self._catalogued_errors)

    def _drain_updates(self):
        while True:
            try:
                _index, _updates = self.update_queue.get_nowait()

                for _update_column, _update_value in _updates.items():
                    self.df.at[_index, _update_column] = _update_value

            except queue.Empty:
                break

        self.update()

    def send_update(self, index: object, updates: Dict[str, object]):
        if self.is_interrupted():
            # Raise the exception before we put the update on the queue -- we don't want to incorrectly report success
            raise KeyboardInterrupt()

        self.update_queue.put((index, updates))

    def _skip_display(self):
        return self.quiet or _datalab.is_datalab_api()

    def interrupt(self):
        self.interrupted_event.set()

    def is_interrupted(self):
        return self.interrupted_event.is_set()

    def add_job(self, index: object, func_with_args: Tuple, on_job_success: Callable = None):
        self.jobs[index] = (func_with_args, on_job_success)

    def clear_jobs(self):
        self.jobs = dict()

    def execute_jobs(self, session: Session):
        try:
            exception_raised = None
            with concurrent.futures.ThreadPoolExecutor(max_workers=session.options.max_concurrent_requests) as executor:
                _futures = dict()
                for job_index, (func_with_args, on_job_success) in self.jobs.items():
                    _futures[executor.submit(*func_with_args)] = (job_index, on_job_success)

                while True:

                    # noinspection PyBroadException
                    try:
                        self._drain_updates()

                        # Now we wait for all the futures to complete, breaking out every half second to drain status
                        # updates (see TimeoutError except block).
                        for future in concurrent.futures.as_completed(_futures, 0.5):
                            job_index, on_job_success = _futures[future]
                            del _futures[future]
                            self._drain_updates()

                            if future.cancelled() or isinstance(future.exception(), KeyboardInterrupt):
                                self.df.at[job_index, 'Result'] = 'Canceled'
                                continue

                            if future.exception():
                                self.df.at[job_index, 'Result'] = _common.format_exception(future.exception())
                                if self.errors == 'raise':
                                    raise future.exception()
                                else:
                                    continue

                            if on_job_success:
                                # noinspection PyBroadException
                                try:
                                    on_job_success(job_index, future.result())
                                except BaseException:
                                    self.df.at[job_index, 'Result'] = _common.format_exception()
                                    if self.errors == 'raise':
                                        raise
                                    else:
                                        continue

                        # We got all the way through the iterator without encountering a TimeoutError, so break
                        break

                    except concurrent.futures.TimeoutError:
                        # Start the loop again from the top, draining the status updates first
                        pass

                    except BaseException as e:
                        for future in _futures.keys():
                            future.cancel()
                        self.interrupt()
                        exception_raised = e

            if exception_raised:
                self.exception(exception_raised, throw=True)

        finally:
            self._drain_updates()
            self.clear_jobs()

    def update(self, new_message=None, new_code=None):
        if new_message is None:
            new_message = self.message

        if new_code is not None:
            self.code = new_code

        if self._skip_display():
            self.message = new_message
        else:
            if not _common.display_supports_html():
                self.message = self._display_text(new_message)
            else:
                self.message = self._display_html(new_message)

    def _display_text(self, new_message):
        if new_message == self.message:
            return new_message

        for warning in (self.warnings - self.printed_warnings):
            display(warning)
        self.printed_warnings = set(self.warnings)

        text = re.sub(r'</?[^>]+>', '', new_message)

        # noinspection PyTypeChecker
        display(text)

        return new_message

    def display(self):
        """
        Force the Status object to output its HTML-based display to the Notebook or the console
        """
        if not _common.display_supports_html():
            self.message = self._display_text(self.message)
        else:
            self.message = self._display_html(self.message)

    def _display_html(self, new_message):
        _common.ipython_clear_output(wait=True)

        display_df = self.df
        if self.code == Status.RUNNING and len(self.df) > 20 and 'Result' in self.df.columns:
            display_df = self.df[~self.df['Result'].isin(['Queued', 'Success'])]

        display_df = display_df.head(20)

        if self.code == Status.RUNNING:
            color = '#EEEEFF'
        elif self.code == Status.SUCCESS:
            color = '#EEFFEE'
        else:
            color = '#FFEEEE'

        html = ''
        if len(self.warnings) > 0:
            for warning in self.warnings:
                html += '<div style="background-color: #FFFFCC;">%s</div>' % (Status._massage_cell(warning))

        style = 'background-color: %s;' % color
        html += '<div style="%s">%s</div>' % (
            style + 'color:black; text-align: left;', Status._massage_cell(new_message))

        if len(display_df) > 0:
            html += '<table class="tex2jax_ignore">'  # Ignore mathjax renderings so $...$ isn't converted to latex
            html += '<tr><td style="%s"></td>' % style

            for col in display_df.columns:
                align = 'left' if display_df.dtypes[col] == object else 'right'
                html += '<td style="%s text-align: %s;">%s</td>' % (style, align, Status._massage_cell(col))

            html += '</tr>'

            for index, row in display_df.iterrows():
                html += '<tr style="%s">' % style
                html += '<td style="vertical-align: top;">%s</td>' % index
                for cell in row:
                    if isinstance(cell, datetime.timedelta):
                        hours, remainder = divmod(cell.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        html += '<td style="vertical-align: top;">{:02}:{:02}:{:02}.{:02}</td>'.format(
                            int(hours), int(minutes), int(seconds), int((cell.microseconds + 5000) / 10000))
                    else:
                        align = 'left' if isinstance(cell, str) else 'right'
                        html += '<td style="text-align: %s; vertical-align: top;">%s</td>' % \
                                (align, Status._massage_cell(cell, links=True))
                html += '</tr>'

            html += '</table>'

        # noinspection PyTypeChecker
        if _datalab.is_ipython():
            _common.ipython_clear_output(wait=True)
            display(HTML(html))
            return new_message
        elif _datalab.is_rkernel():
            # CRAB-31224: Calling display_html produces flaky segfault error https://github.com/rstudio/reticulate/issues/1112
            # Uncomment below lines if above reticulate issue is resolved, then remove line: `self.message = html`
            # from rpy2.robjects.packages import importr
            # rdisplay = importr('IRdisplay')
            # rdisplay.clear_output(wait=True)
            # rdisplay.display_html(html)

            # Until segfault issue is resolved, provide html through status message
            return html
        else:
            return html

    @staticmethod
    def _massage_cell(cell, links=False):
        cell = str(cell)

        def markdown_bullets_to_html_bullets(match):
            lines = [re.sub(r'^- ', '', line) for line in match[1].split('\n')]
            return '<ul><li>%s</li></ul>' % '</li><li>'.join(lines)

        cell = re.sub(r'\n(- .*((\n- .*)+|$))', markdown_bullets_to_html_bullets, cell)
        cell = cell.replace('\n', '<br>')
        if links:
            cell = re.sub(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+{}]|[!*(), ]|(%[0-9a-fA-F][0-9a-fA-F]))+)',
                          r'<a target="_blank" href="\1">link</a>',
                          cell)

        return cell

    def get_timer(self):
        return _common.timer_elapsed(self.timer)

    def reset_timer(self):
        self.timer = _common.timer_start()

    def exception(self, e, throw=False, use_error_message=False):
        if isinstance(e, KeyboardInterrupt):
            status_message = 'Canceled'
            status_code = Status.CANCELED
        else:
            status_message = 'Error encountered, scroll down to view' if not use_error_message else str(e)
            status_code = Status.FAILURE

        self.update(status_message, status_code)
        if throw:
            raise e

    @staticmethod
    def validate(status: Status, quiet: bool = False, errors: Optional[str] = None) -> Status:
        """
        :param status: An already-instantiated Status object
        :type status: Status
        :param quiet: If True, suppresses output to Jupyter/console
        :type quiet: bool
        :param errors: 'raise' to raise exceptions immediately, 'catalog' to track them in catalogued_errors attr
        :type errors: str

        :rtype Status
        :return: The already-instantiated Status object passed in, or a newly-instantiated Status object

        :meta private:
        """
        if errors not in [None, 'raise', 'catalog']:
            raise SPyValueError("errors argument must be either 'raise' or 'catalog'")

        if status is None:
            status = Status(quiet=quiet, errors=errors)

        else:
            if not isinstance(status, Status):
                raise SPyTypeError(f'Argument status must be of type Status, not {type(status)}')
            if quiet:
                raise SPyValueError('The quiet flag cannot be supplied when a status object is provided. Instead, '
                                    'use the quiet flag of your status object by creating a quiet status with '
                                    'spy.Status(quiet=True), or setting status.quiet=True.')
            if errors is not None:
                raise SPyValueError('The errors flag cannot be supplied when a status object is provided. Instead, '
                                    'use the errors flag of your status object by creating a status with spy.Status('
                                    'errors="catalog"), or setting status.errors="catalog".')
        return status


# For pickling compatibility, see CRAB-33735. Tested by test_pickle_from_python37_and_spy_182_37()
setattr(_common, 'Status', Status)
