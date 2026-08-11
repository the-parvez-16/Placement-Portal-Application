from flask import Flask
from flask_cors import CORS
from .config import config
from .extensions import db, jwt, celery_app, cache
from .security import hash_password
from server.models import *
import os
from dotenv import load_dotenv
from server.exceptions import register_error_handlers
from server.controllers import auth, admin, company, student
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

class Admin:
    name = "cb16"
    role = UserRole.SUDO
    email = "cb16@admin.com"
    password = "cb16"
    status = UserStatus.APPROVED

def celery_init_app(app):
    class FlaskTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = FlaskTask


def create_app(config_name=os.getenv("FLASK_ENV", "development")):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    
    app.config.from_object(config[config_name])
    db.init_app(app)
    jwt.init_app(app)
    celery_app.conf.update(
        broker_url=app.config.get("CELERY_BROKER_URL"),
        result_backend=app.config.get("CELERY_RESULT_BACKEND"),
        include=['server.workers.tasks']
    )
    celery_init_app(app)
    cache.init_app(app)
    register_error_handlers(app)

    if not os.path.exists('logs'):
        os.mkdir('logs')
        
    file_handler = RotatingFileHandler('logs/backend.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    
    with app.app_context():
        db.create_all()
        admin_user = User.query.filter_by(email=Admin.email).first()

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

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(student)
    
    return app