from server.repositories import UserRepository, DriveRepository, ApplicationRepository
from server.models import UserRole, UserStatus, DriveStatus
from server.dto import PendingCompanyDTO, PendingDriveDTO, RecentApplicationDTO, AdminCompanyListDTO, AdminStudentListDTO
from server.exceptions import ResourceNotFoundException

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


def get_admin_pending_approvals(search_query=""):
    pending_company_users = UserRepository.get_pending_companies(search_query)
    pending_drives = DriveRepository.find_by_status(DriveStatus.PENDING)

    pending_company_users = PendingCompanyDTO(many=True).dump(pending_company_users)
    pending_drives = PendingDriveDTO(many=True).dump(pending_drives)

    response = {
        "pendingCompanyUsers": pending_company_users,
        "pendingDrives": pending_drives
    }

    return response


def get_admin_recent_applications():
    recent_apps = ApplicationRepository.get_recent_applications(limit=5)
    return RecentApplicationDTO(many=True).dump(recent_apps)

def update_user_status(user_id: int, new_status: str):
    user = UserRepository.find_by_id(user_id)
    if not user:
        raise ResourceNotFoundException(f"User with ID {user_id} not found!")
    
    user.status = UserStatus[new_status.upper()]
    UserRepository.commit()

    return {"message": "User status updated successfully"}


def update_drive_status(id, new_status):
    drive = DriveRepository.find_by_id(id)
    if not drive:
        raise ResourceNotFoundException(f"Drive with ID {id} not found!")
    
    drive.status = DriveStatus[new_status.upper()]
    DriveRepository.commit()

    return {"message": "Drive status updated successfully"}


def get_admin_companies(page, search_query=""):
    paginated_result = UserRepository.get_paginated_companies(page, search_query)
    dumped_items = AdminCompanyListDTO(many=True).dump(paginated_result.items)
    
    return {
        "companies": dumped_items,
        "current_page": paginated_result.page,
        "total_pages": paginated_result.pages
    }
    
    
def get_admin_students(page, search_query=""):
    paginated_result = UserRepository.get_paginated_students(page, search_query)
    dumped_items = AdminStudentListDTO(many=True).dump(paginated_result.items)
    
    return {
        "students": dumped_items,
        "current_page": paginated_result.page,
        "total_pages": paginated_result.pages
    }
    

def get_admin_drives(page, search_query=""):
    paginated_result = DriveRepository.get_paginated_drives(page, search_query)
    dumped_items = AdminDriveListDTO(many=True).dump(paginated_result.items)
    
    return {
        "drives": dumped_items,
        "current_page": paginated_result.page,
        "total_pages": paginated_result.pages
    }


def get_admin_applications(page, search_query=""):
    paginated_result = ApplicationRepository.get_paginated_applications(page, search_query)
    dumped_items = AdminApplicationListDTO(many=True).dump(paginated_result.items)
    
    return {
        "applications": dumped_items,
        "current_page": paginated_result.page,
        "total_pages": paginated_result.pages
    }
      