from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

def hash_password(password: str) -> str:
    return generate_password_hash(password=password)

def verify_password(password: str, hashed_password: str) -> bool:
    return check_password_hash(pwhash=hashed_password,password=password)

def generate_token(user):
    additional_claims={"role": user.role.value, "email": user.email}
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=str(user.id))

    return {"access_token": access_token, "refresh_token": refresh_token}