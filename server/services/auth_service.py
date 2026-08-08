from server.repositories import BaseRepository, UserRepository, StudentRepository, CompanyRepository
from server.core.security import hash_password, verify_password, generate_token
from server.models import User, Student, Company, UserRole
from server.exceptions import ResourceAlreadyExistsError, InvalidCredentialsError

def register_user_service(data):
    name = data["name"]
    email = data["email"]
    password = data["password"]
    role = data["role"]

    existing_user = UserRepository.find_by_email(email)
    if existing_user:
        raise ResourceAlreadyExistsError("Email already registered")
    
    hashed_password = hash_password(password)
    
    new_user = User(
        email=email,
        password=hashed_password,
        role=role
    )
    
    # 4. Add to db.session and flush (to get the new_user.id)
    UserRepository.save(new_user)
    # 5. Important: Create the linked profile!
    if role == UserRole.STUDENT:
        new_student = Student(user_id=new_user.id, name=name)
        StudentRepository.save(new_student)
    if role == UserRole.COMPANY:
        new_company = Company(user_id=new_user.id, name=name)
        CompanyRepository.save(new_company)
    
    # 6. Commit the database transaction!
    BaseRepository.commit()
    
    # 7. Return the new user or a success message
    return {"message": "Success!", "id": new_user.id}

def login_user_service(data):
    email = data["email"]
    password = data["password"]

    user = UserRepository.find_by_email(email)
    
    if not user or not verify_password(user.password, password):
        raise InvalidCredentialsError("Invalid credentials!")

    token_pair = generate_token(user)
    return {
        "message": "Login success!",
        "access_token": token_pair["access_token"],
        "refresh_token": token_pair["refresh_token"]
    }

def refresh_user_service(user_id):
    user = UserRepository.find_by_id(user_id)
    token_pair = generate_token(user)

    return {
        "access_token": token_pair["access_token"],
        "refresh_token": token_pair["refresh_token"]
    }