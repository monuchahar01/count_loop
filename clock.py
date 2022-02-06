from apscheduler.schedulers.background  import BlockingScheduler
from sample_fire_DB import insert_DB
sched = BlockingScheduler()


def maina():
    """Run tick() at the interval of every ten seconds."""
   
    sched.add_job(insert_DB, 'interval', minutes=1)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass 


maina()


