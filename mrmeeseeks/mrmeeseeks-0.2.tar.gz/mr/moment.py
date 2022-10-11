from enum import IntEnum


class Moment(IntEnum):
    """Describe the three main steps of the workflow.

    When defining an action, one can set the right 
    moment to execute it among the three main stages: 

    - Moment.BEFORE
    - Moment.ON_FILE
    - Moment.AFTER

    """
    BEFORE = 0
    ON_FILE = 1
    AFTER = 2
