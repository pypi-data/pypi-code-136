import coloredlogs, logging

logger = logging.getLogger(__name__)

# [THEORY] Log levels, pros and cons
coloredlogs.install(level='DEBUG', logger=logger)

logger.info("Example python program")


# [THEORY] TDD and coverage
def add_one(number):
    return number + 1
