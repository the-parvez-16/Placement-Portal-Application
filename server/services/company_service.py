from server.repositories import UserRepository
from server.models import Company, User, UserStatus
from server.exceptions import CompanyNotFoundException, AccountBlockedException

def update_company_profile(user_id: User.id, data):

    company_user = UserRepository.find_by_user_id(user_id)

    if not company_user or not company_user.company:
        raise CompanyNotFoundException(f"Company with user_id {user_id} not found")

    if company_user.status == UserStatus.BLOCKED:
        raise AccountBlockedException("Company account has been blocked by the admin.")

    if "hr_contact" in data:
        company_user.company.hr_contact = data["hr_contact"]
    if "website" in data:
        company_user.company.website = data["website"]

    if company_user.status == UserStatus.PENDING:
        company_user.status = UserStatus.APPLIED
    
    UserRepository.commit()

    return company_user