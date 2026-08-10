from server.repositories import ApplicationRepository, StudentRepository
from server.exceptions import ResourceAlreadyExistsException, InvalidStatusTransitionException
from server.models import Application, ApplicationStatus

def apply_for_drive(user_id: int, drive_id: int):
    student = StudentRepository.get_by_user_id(user_id)
    if student is None:
        raise ResourceNotFoundException("Student not found")

    application = ApplicationRepository.find_by_student_and_drive(student.id, drive_id)
    if application:
        raise ResourceAlreadyExistsException("")

    application = Application(
        student_id=student.id,
        drive_id=drive_id,
        status=ApplicationStatus.APPLIED
    )

    ApplicationRepository.save(application)
    ApplicationRepository.commit()

    return application

def get_drive_applications(drive_id: int):
    applications = ApplicationRepository.find_by_drive_id(drive_id)
    return applications

def update_application_status(application_id: int, new_status: str):
    application = ApplicationRepository.find_by_id(application_id)
    if not application:
        raise ResourceNotFoundException("Application not found")

    new_status_enum = ApplicationStatus[new_status.upper()]
    
    if new_status_enum == ApplicationStatus.REJECTED:
        pass
    elif application.status == ApplicationStatus.APPLIED and new_status_enum == ApplicationStatus.SHORTLISTED:
        pass
    elif application.status == ApplicationStatus.SHORTLISTED and new_status_enum == ApplicationStatus.SELECTED:
        pass
    else:
        raise InvalidStatusTransitionException("Invalid status transition!")

    application.status = new_status_enum
    ApplicationRepository.commit()

    return application
        

def get_student_applications(user_id: int):
    student = StudentRepository.get_by_user_id(user_id)
    if not student:
        raise ResourceNotFoundException("Student not found")
    return ApplicationRepository.find_by_student_id(student.id)


def get_application_by_id(application_id: int):
    app = ApplicationRepository.find_by_id(application_id)
    if not app:
        raise ResourceNotFoundException("Application not found")
    return app
