from server.core.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Text, ForeignKey
from typing import Optional

class Student(db.Model):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # education
    branch: Mapped[Optional[str]] = mapped_column(String(200))
    cgpa: Mapped[Optional[float]] = mapped_column(Float)
    expected_graduation_year: Mapped[Optional[int]] = mapped_column(Integer)

    skills: Mapped[Optional[str]] = mapped_column(Text)
    resume_file: Mapped[Optional[str]] = mapped_column(String(200))

    applications = relationship("Application", backref="student", lazy="select", cascade="all, delete-orphan")
