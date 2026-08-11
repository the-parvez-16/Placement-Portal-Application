from server.repositories import ApplicationRepository, CompanyRepository
from server.models.enums import ApplicationStatus
from server.services.mail_service import dispatch_email

def process_daily_reminders():
    applications = ApplicationRepository.find_by_status(ApplicationStatus.INTERVIEW)
    
    for app in applications:
        html_template = f"""
        <html>
          <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
            <div style="max-width: 600px; margin: auto; border: 2px solid #323232; padding: 20px; border-radius: 8px;">
                <h2 style="color: #4CAF50; border-bottom: 2px solid #323232; padding-bottom: 10px;">
                    Interview Reminder
                </h2>
                <p>Hello <b>{app.student.name}</b>,</p>
                <p>This is a gentle reminder for your upcoming placement interview.</p>
                <ul style="background: #f4f4f4; padding: 15px; border-radius: 5px;">
                    <li><b>Company:</b> {app.drive.company.name}</li>
                    <li><b>Role:</b> {app.drive.job_title}</li>
                </ul>
                <p>All the best! You're going to rock it! 🚀</p>
                <br>
                <p>Regards,<br><b>Placement Portal Application Team</b></p>
            </div>
          </body>
        </html>
        """
        dispatch_email(app.student.user.email, f"Action Required: Interview at {app.drive.company.name}", html_template)

def process_monthly_reports():
    companies = CompanyRepository.get_all_companies()

    for company in companies:
        total_drives = len(company.placement_drives)
        total_applications = 0
        shortlisted = 0
        
        for drive in company.placement_drives:
            total_applications += len(drive.applications)
            shortlisted += sum(1 for app in drive.applications if app.status in [ApplicationStatus.SHORTLISTED, ApplicationStatus.INTERVIEW, ApplicationStatus.SELECTED])
        
        html_template = f"""
        <html>
          <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #2d3748; line-height: 1.6; background-color: #f7fafc; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background: #ffffff; border: 1px solid #e2e8f0; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                <h2 style="color: #2b6cb0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 0;">
                    Monthly Placement Analytics
                </h2>
                <p>Dear <b>{company.name} HR Team</b>,</p>
                <p>Here is your monthly summary for the placement drives conducted through our portal:</p>
                <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                    <tr style="background-color: #edf2f7;">
                        <td style="padding: 12px; border: 1px solid #cbd5e0;"><b>Total Drives Posted</b></td>
                        <td style="padding: 12px; border: 1px solid #cbd5e0; text-align: right;">{total_drives}</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px; border: 1px solid #cbd5e0;"><b>Total Applications Received</b></td>
                        <td style="padding: 12px; border: 1px solid #cbd5e0; text-align: right;">{total_applications}</td>
                    </tr>
                    <tr style="background-color: #edf2f7;">
                        <td style="padding: 12px; border: 1px solid #cbd5e0;"><b>Candidates Shortlisted/Selected</b></td>
                        <td style="padding: 12px; border: 1px solid #cbd5e0; text-align: right;">{shortlisted}</td>
                    </tr>
                </table>
                <br>
                <p>Best Regards,<br><b>Placement Portal Admin Team</b></p>
            </div>
          </body>
        </html>
        """
        dispatch_email(company.user.email, "Monthly Placement Analytics Report", html_template)
