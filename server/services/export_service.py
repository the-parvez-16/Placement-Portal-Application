import os, csv
from server.repositories import ApplicationRepository, DriveRepository
from flask import current_app


def generate_csv_for_student(student_id: int, task_id: str):
    applications = ApplicationRepository.find_by_student_id(student_id)

    export_dir = os.path.join(current_app.root_path, 'static', 'exports')
    os.makedirs(export_dir, exist_ok=True)
    
    file_path = os.path.join(export_dir, f'{task_id}.csv')
    
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Application ID', 'Job Title', 'Company', 'Status', 'Applied On'])
        
        for app in applications:
            writer.writerow([
                app.id,
                app.drive.job_title,
                app.drive.company.name,
                app.status.value,
                app.created_at.strftime("%Y-%m-%d") if app.created_at else "N/A"
            ])

    return f"http://localhost:5000/api/student/download/{task_id}"


def generate_csv_for_company(company_id: int, task_id: str):
    drives = DriveRepository.find_by_company_id(company_id)
    
    export_dir = os.path.join(current_app.root_path, 'static', 'exports')
    os.makedirs(export_dir, exist_ok=True)
    file_path = os.path.join(export_dir, f'{task_id}.csv')
    
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Drive Title', 'Student Name', 'Branch', 'Status', 'Applied On'])
        
        for drive in drives:
            for app in drive.applications:
                writer.writerow([
                    drive.job_title,
                    app.student.name if app.student else 'N/A',
                    app.student.branch if app.student else 'N/A',
                    app.status.value,
                    app.created_at.strftime("%Y-%m-%d") if app.created_at else "N/A"
                ])
                
    return f"http://localhost:5000/api/company/download/{task_id}"
