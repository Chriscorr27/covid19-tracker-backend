from apscheduler import schedulers
from apscheduler.schedulers.background import BackgroundScheduler
from covid_19_app.utils import *

def start_scheluer():
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(get_daily_data,'interval', hours=6,id="covid_027",replace_existing=True)
    scheduler.start()
