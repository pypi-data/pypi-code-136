from crontab import CronTab


def create_cron(command, interval=60, cron=None, **kwargs):
    cron_mgr = CronTab(user=True)
    job = cron_mgr.new(command=command)
    cron = kwargs.get("cron", cron)
    if cron:
        job.setall(cron)
    else:
        job.minute.every(kwargs.get("interval", interval))
    cron_mgr.write()
