from server.core import celery_app
from server.services.export_service import *
from server.services.notification_service import process_daily_reminders, process_monthly_reports

@celery_app.task
def send_daily_reminders():
    process_daily_reminders()
    return "Daily reminders dispatched."

@celery_app.task
def generate_monthly_report():
    process_monthly_reports()
    return "Monthly reports dispatched."


@celery_app.task(bind=True)
def export_student_applications_task(self, student_id: int):
    # self.request.id is Celery's unique background Task ID
    download_url = generate_csv_for_student(student_id, self.request.id)
    return download_url


@celery_app.task(bind=True)
def export_company_applications_task(self, company_id: int):
    download_url = generate_csv_for_company(company_id, self.request.id)
    return download_url

