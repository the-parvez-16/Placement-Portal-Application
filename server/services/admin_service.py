from server.repositories import UserRepository, DriveRepository, ApplicationRepository
from server.models import UserRole, UserStatus, DriveStatus
from server.dto import PendingCompanyDTO, PendingDriveDTO

def get_admin_dashboard_stats():
    total_students = UserRepository.count_by_role(UserRole.STUDENT)
    total_companies = UserRepository.count_by_role(UserRole.COMPANY)
    total_drives = DriveRepository.count_all()
    total_applications = ApplicationRepository.count_all()

    pending_companies = UserRepository.find_by_role_and_status(UserRole.COMPANY, UserStatus.PENDING)
    pending_drives = DriveRepository.find_by_status(DriveStatus.PENDING)

    pending_companies = PendingCompanyDTO(many=True).dump(pending_companies)
    pending_drives = PendingDriveDTO(many=True).dump(pending_drives)

    response = {
        "total_students": total_students,
        "total_companies": total_companies,
        "total_drives": total_drives,
        "total_applications": total_applications,
        "pending_companies": pending_companies,
        "pending_drives": pending_drives
    }

    return response