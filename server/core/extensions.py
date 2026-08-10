from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from flask_jwt_extended import JWTManager
from celery import Celery
from flask_caching import Cache


class BaseModel(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(default=func.now()) 
    updated_at: Mapped[datetime] = mapped_column(default=func.now(),onupdate=func.now())

db = SQLAlchemy(model_class=BaseModel)

jwt = JWTManager()

celery_app = Celery('ppa_workers')

cache = Cache()