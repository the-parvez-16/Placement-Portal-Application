from server.core.extensions import db
from server.models.enums import UserStatus, UserRole
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[UserRole] = mapped_column(nullable=False)
    status: Mapped[UserStatus] = mapped_column(default=UserStatus.PENDING)

    student = relationship("Student", backref="user", uselist=False, cascade="all, delete-orphan")
    company = relationship("Company", backref="user", uselist=False, cascade="all, delete-orphan")