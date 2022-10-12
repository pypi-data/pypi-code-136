# std

# internal
from tier.internal.logging import log
from tier.internal.tier import Tier


def sync():
    log.debug('tier sync')

    tier = Tier()
    tier.sync()
