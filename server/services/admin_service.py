from server.repositories import UserRepository, DriveRepository, ApplicationRepository
from server.models import UserRole, UserStatus, DriveStatus
from server.dto import PendingCompanyDTO, PendingDriveDTO

def get_admin_dashboard_stats():
    total_students = UserRepository.count_by_role(UserRole.STUDENT)
    total_companies = UserRepository.count_by_role(UserRole.COMPANY)
    total_drives = DriveRepository.count_all()
    total_applications = ApplicationRepository.count_all()


    response = {
        "totalStudents": total_students,
        "totalCompanies": total_companies,
        "totalDrives": total_drives,
        "totalApplications": total_applications
    }

    return response


def get_admin_pending_approvals():
    pending_company_users = UserRepository.find_by_role_and_status(UserRole.COMPANY, UserStatus.APPLIED)
    pending_drives = DriveRepository.find_by_status(DriveStatus.PENDING)

    pending_company_users = PendingCompanyDTO(many=True).dump(pending_company_users)
    pending_drives = PendingDriveDTO(many=True).dump(pending_drives)

    response = {
        "pendingCompanyUsers": pending_company_users,
        "pendingDrives": pending_drives
    }

    return response