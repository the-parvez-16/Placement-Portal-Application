from flask import Flask
from .config import config
from .extensions import db, jwt
from .security import hash_password
from server.models import *

class Admin:
    name = "cb16"
    role = UserRole.SUDO
    email = "cb16@admin.com"
    password = "cb16"
    status = UserStatus.APPROVED

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()
        admin_user = User.query.filter_by(email="cb16@admin.com").first()

        if not admin_user:
            hashed_password = hash_password(Admin.password)
            new_admin = User(
                email=Admin.email,
                password=hashed_password,
                role=Admin.role,
                status=Admin.status
            )
            db.session.add(new_admin)
            db.session.commit()
            print("Default Admin account created successfully!")
    return app