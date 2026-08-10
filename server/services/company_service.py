from server.repositories import UserRepository
from server.models import Company, User, UserStatus
from server.exceptions import ResourceNotFoundException, AccountBlockedException

def get_company_profile(user_id: int) -> User:
    company_user = UserRepository.find_by_id(user_id)

    if not company_user or not company_user.company:
        raise ResourceNotFoundException(f"Company with user_id {user_id} not found")

    if company_user.status == UserStatus.BLOCKED:
        raise AccountBlockedException("Company account has been blocked by the admin.")

    return company_user

def update_company_profile(user_id: User.id, data):

    company_user = UserRepository.find_by_id(user_id)

    if not company_user or not company_user.company:
        raise ResourceNotFoundException(f"Company with user_id {user_id} not found")

    if company_user.status == UserStatus.BLOCKED:
        raise AccountBlockedException("Company account has been blocked by the admin.")

    comp_data = data["company"]

    company_user.company.name = comp_data["name"]
    company_user.company.location = comp_data["location"]
    company_user.company.industry = comp_data["industry"]
    company_user.company.about = comp_data["about"]
    company_user.company.hr_contact = comp_data["hr_contact"]
    company_user.company.website = comp_data["website"]

    if company_user.status == UserStatus.PENDING:
        company_user.status = UserStatus.APPLIED
    
    UserRepository.commit()

    return company_user