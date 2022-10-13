import logging as log

log.basicConfig(level=log.WARN,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.StreamHandler()
                ]
                )

