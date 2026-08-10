from server.core import celery_app
from server.repositories import ApplicationRepository
import io
import csv

@celery_app.task
def send_daily_reminders():
    print("reminders sent...")

@celery_app.task
def generate_monthly_report():
    print("monthly report generated...")

@celery_app.task
def export_applications_csv(student_id):
    applications = ApplicationRepository.find_by_student_id(student_id)

    data = io.StringIO()
    writer = csv.writer(data)

    writer.writerow(['Application ID', 'Student ID', 'Drive ID', 'Status', 'Applied At', 'Updated At'])

    for app in applications:
        writer.writerow([
            app.id,
            app.student_id,
            app.drive_id,
            app.status.name,
            app.created_at,
            app.updated_at
        ])

    data.seek(0)
    return data


