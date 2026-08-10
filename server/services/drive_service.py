from server.exceptions import ResourceNotFoundException
from server.models import PlacementDrive, DriveStatus
from server.repositories import DriveRepository
from server.repositories.company_repository import CompanyRepository

def create_placement_drive(user_id: int, drive_data: dict):
    company = CompanyRepository.get_by_user_id(user_id)
    if company is None:
        raise ResourceNotFoundException("Company not found")

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


def get_drives_by_company(user_id: int):
    company = CompanyRepository.get_by_user_id(user_id)
    if company is None:
        raise ResourceNotFoundException("Company not found")

    return DriveRepository.find_by_company_id(company.id)


def get_approved_drives(page: int=1, search_query: str=""):
    return DriveRepository.get_paginated_drives(page, search_query,status=DriveStatus.APPROVED)