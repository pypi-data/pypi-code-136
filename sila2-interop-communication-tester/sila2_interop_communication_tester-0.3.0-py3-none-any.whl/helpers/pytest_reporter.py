from functools import partial
from typing import Callable, List, Mapping

from _pytest.reports import CollectReport
from _pytest.terminal import TerminalReporter, _folded_skips, _get_line_with_reprcrash_message, _get_pos


class NotTruncatingTerminalReporter(TerminalReporter):
    def short_test_summary(self) -> None:
        if not self.reportchars:
            return

        def show_simple(stat, lines: List[str]) -> None:
            failed = self.stats.get(stat, [])
            if not failed:
                return
            config = self.config
            for rep in failed:
                line = _get_line_with_reprcrash_message(config, rep, 10_000)
                lines.append(line)

        def show_xfailed(lines: List[str]) -> None:
            xfailed = self.stats.get("xfailed", [])
            for rep in xfailed:
                verbose_word = rep._get_verbose_word(self.config)
                pos = _get_pos(self.config, rep)
                lines.append(f"{verbose_word} {pos}")
                reason = rep.wasxfail
                if reason:
                    lines.append("  " + str(reason))

        def show_xpassed(lines: List[str]) -> None:
            xpassed = self.stats.get("xpassed", [])
            for rep in xpassed:
                verbose_word = rep._get_verbose_word(self.config)
                pos = _get_pos(self.config, rep)
                reason = rep.wasxfail
                lines.append(f"{verbose_word} {pos} {reason}")

        def show_skipped(lines: List[str]) -> None:
            skipped: List[CollectReport] = self.stats.get("skipped", [])
            fskips = _folded_skips(self.startpath, skipped) if skipped else []
            if not fskips:
                return
            verbose_word = skipped[0]._get_verbose_word(self.config)
            for num, fspath, lineno, reason in fskips:
                if reason.startswith("Skipped: "):
                    reason = reason[9:]
                if lineno is not None:
                    lines.append("%s [%d] %s:%d: %s" % (verbose_word, num, fspath, lineno, reason))
                else:
                    lines.append("%s [%d] %s: %s" % (verbose_word, num, fspath, reason))

        REPORTCHAR_ACTIONS: Mapping[str, Callable[[List[str]], None]] = {
            "x": show_xfailed,
            "X": show_xpassed,
            "f": partial(show_simple, "failed"),
            "s": show_skipped,
            "p": partial(show_simple, "passed"),
            "E": partial(show_simple, "error"),
        }

        lines: List[str] = []
        for char in self.reportchars:
            action = REPORTCHAR_ACTIONS.get(char)
            if action:  # skipping e.g. "P" (passed with output) here.
                action(lines)

        if lines:
            self.write_sep("=", "short test summary info")
            for line in lines:
                self.write_line(line)
