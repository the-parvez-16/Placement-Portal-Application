import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def dispatch_email(recipient_email: str, subject: str, html_body: str) -> bool:
    sender_email = os.getenv("MAIL_USERNAME")
    sender_password = os.getenv("MAIL_PASSWORD")
    
    if not sender_email or not sender_password:
        print("[MailService] ERROR: SMTP credentials missing.")
        return False
        
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    msg.attach(MIMEText(html_body, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"[MailService] SUCCESS: Notification dispatched to {recipient_email}")
        return True
    except Exception as e:
        print(f"[MailService] FAILED: Could not dispatch to {recipient_email}. Reason: {e}")
        return False
