from celery.schedules import crontab
from server.core import celery_app

celery_app.conf.beat_schedule = {
    'daily-reminders': {
        'task': 'server.workers.tasks.send_daily_reminders',
        'schedule': crontab(hour=10, minute=0),
    },
    'monthly-report': {
        'task': 'server.workers.tasks.generate_monthly_report',
        'schedule': crontab(day_of_month='1', hour=10, minute=0),
    }
}

celery_app.conf.timezone = 'Asia/Kolkata'
