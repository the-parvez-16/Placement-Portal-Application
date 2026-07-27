from server.core.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Text, ForeignKey, DateTime
from typing import Optional
from datetime import datetime

from server.models.enums import DriveStatus

class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False, index=True)
    job_title: Mapped[str] = mapped_column(String(150), nullable=False)
    job_description: Mapped[str] = mapped_column(Text, nullable=False)


    # eligibility_criteria: Mapped[str] = mapped_column(String(), nullable=False)
    min_cgpa: Mapped[Optional[float]] = mapped_column(Float)
    allowed_branches: Mapped[Optional[str]] = mapped_column(String(255))

    salary: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[DriveStatus] = mapped_column(default=DriveStatus.PENDING)

    application_deadline: Mapped[Optional[datetime]] = mapped_column(DateTime)
    
    applications = relationship("Application", backref="drive", lazy="select", cascade="all, delete-orphan")
