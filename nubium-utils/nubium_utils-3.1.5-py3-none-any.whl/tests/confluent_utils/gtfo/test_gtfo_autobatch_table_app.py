from unittest.mock import patch

import pytest

import nubium_utils
from nubium_utils.confluent_utils.gtfo.gtfo_autobatch_table_app import GtfoAutoBatchTableApp


@pytest.mark.parametrize(
    "recovery_offsets_handled,offsets_processed,recovery_elapsed_time,recovery_offsets_remaining",
    [
        (0, 0, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
        (0, 0, 1, 1),
        (0, 1, 0, 0),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 0, 1, 1),
        (1, 1, 0, 0),
        (1, 1, 0, 1),
        (1, 1, 1, 0),
        (1, 1, 1, 1),
    ],
)
def test_progress_logging_does_not_crash_when_zeroes_are_present(recovery_offsets_handled, offsets_processed, recovery_elapsed_time, recovery_offsets_remaining):
    with patch("nubium_utils.confluent_utils.gtfo.gtfo_autobatch_table_app.GtfoAutoBatchTableApp.__init__", return_value=None):
        app = GtfoAutoBatchTableApp(None, None)
    app._recovery_offsets_handled = recovery_offsets_handled
    app._recovery_offsets_remaining = recovery_offsets_remaining
    app._log_recovery_progress(offsets_processed=offsets_processed, recovery_elapsed_time=recovery_elapsed_time)
