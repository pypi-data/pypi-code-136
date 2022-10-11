from enum import IntEnum


class Moment(IntEnum):
    """Describe the three main steps of the workflow.

    When defining an action, one can set the right 
    moment to execute it among the three main stages: 

    - Moment.BEFORE
    - Moment.ON_ITEM
    - Moment.AFTER

    """
    BEFORE = 0
    ON_ITEM = 1
    AFTER = 2
