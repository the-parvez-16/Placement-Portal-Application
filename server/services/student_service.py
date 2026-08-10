from server.repositories import UserRepository
from server.models import Student, User, UserStatus
from server.exceptions import ResourceNotFoundException, AccountBlockedException

def get_student_profile(user_id: int) -> User:
    student_user = UserRepository.find_by_id(user_id)

    if not student_user or not student_user.student:
        raise ResourceNotFoundException(f"Student with user_id {user_id} not found")

    if student_user.status == UserStatus.BLOCKED:
        raise AccountBlockedException("Student account has been blocked by the admin.")

    return student_user

def update_student_profile(user_id: User.id, data):
    student_user = UserRepository.find_by_id(user_id)

    if not student_user or not student_user.student:
        raise ResourceNotFoundException(f"Student with user_id {user_id} not found")

    if student_user.status == UserStatus.BLOCKED:
        raise AccountBlockedException("Student account has been blocked by the admin.")

    student_data = data["student"]

    student_user.student.name = student_data["name"]
    student_user.student.branch = student_data["branch"]
    student_user.student.cgpa = student_data["cgpa"]
    student_user.student.skills = student_data["skills"]
    student_user.student.expected_graduation_year = student_data["expected_graduation_year"]
    student_user.student.resume_file = student_data["resume_file"]

    UserRepository.commit()

    return student_user