from apscheduler.schedulers.background  import BlockingScheduler
from run import count_loop
sched = BlockingScheduler()


def maina():
    """Run tick() at the interval of every ten seconds."""
   
    sched.add_job(count_loop, 'interval', minutes=1)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass 


maina()


