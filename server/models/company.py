from server.core.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

class Company(db.Model):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    hr_contact: Mapped[Optional[str]] = mapped_column(String(200))
    website: Mapped[Optional[str]] = mapped_column(String(200))

    placement_drives = relationship("PlacementDrive", backref="company", lazy="select", cascade="all, delete-orphan")


