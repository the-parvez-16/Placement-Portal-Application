from server.exceptions import ResourceNotFoundException
from server.models import PlacementDrive, DriveStatus
from server.repositories import DriveRepository
from server.repositories.company_repository import CompanyRepository

def create_placement_drive(user_id: int, drive_data: dict):
    company = CompanyRepository.get_by_user_id(user_id)
    if company is None:
        raise ResourceNotFoundException("Company not found")
    
    if company.user.status.value != "approved":
        raise ValueError("Only approved companies can post drives.")

    job_title = drive_data.get("job_title")
    job_description = drive_data.get("job_description")
    min_cgpa = drive_data.get("min_cgpa")
    allowed_branches = drive_data.get("allowed_branches")
    salary = drive_data.get("salary")
    application_deadline = drive_data.get("application_deadline")
    
    new_drive = PlacementDrive(
        company_id=company.id,
        job_title=job_title,
        job_description=job_description,
        min_cgpa=min_cgpa,
        allowed_branches=allowed_branches,
        salary=salary,
        application_deadline=application_deadline,
        status=DriveStatus.PENDING
    )
    
    DriveRepository.save(new_drive)
    DriveRepository.commit()
    
    return new_drive


def update_placement_drive(drive_id, user_id, drive_data):
    company = CompanyRepository.get_by_user_id(user_id)
    if not company:
        raise ResourceNotFoundException("Company not found")

    drive = DriveRepository.find_by_id(drive_id)
    if not drive:
        raise ResourceNotFoundException("Drive not found")
        
    if drive.company_id != company.id:
        raise ValueError("You can only edit your own drives!")

    drive.job_title = drive_data.get("job_title", drive.job_title)
    drive.job_description = drive_data.get("job_description", drive.job_description)
    drive.min_cgpa = drive_data.get("min_cgpa", drive.min_cgpa)
    drive.allowed_branches = drive_data.get("allowed_branches", drive.allowed_branches)
    drive.salary = drive_data.get("salary", drive.salary)
    drive.application_deadline = drive_data.get("application_deadline", drive.application_deadline)
    
    DriveRepository.commit()
    return drive


def update_drive_status(drive_id: int, user_id: int, new_status):
    company = CompanyRepository.get_by_user_id(user_id)
    drive = get_drive_by_id(drive_id)
    
    if drive.company_id != company.id:
        raise ValueError("You can only manage your own drives")
        
    drive.status = DriveStatus[new_status.upper()]
    DriveRepository.commit()

    return {"message": f"Drive marked as {new_status}!"}


def get_drives_by_company(user_id: int):
    company = CompanyRepository.get_by_user_id(user_id)
    if company is None:
        raise ResourceNotFoundException("Company not found")

    return DriveRepository.find_by_company_id(company.id)


def get_approved_drives(page: int=1, search_query: str=""):
    return DriveRepository.get_paginated_drives(page, search_query,status=DriveStatus.APPROVED)


def get_drive_by_id(drive_id: int):
    drive = DriveRepository.find_by_id(drive_id)

    if not drive:
        raise ResourceNotFoundException("Drive not found")

    return drive
