# std

# internal
from tier.internal.logging import log
from tier.internal.tier import Tier


def develop():
    log.debug('tier develop')

    tier = Tier()
    tier.develop()
