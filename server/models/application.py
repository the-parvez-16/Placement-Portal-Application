from server.core.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from server.models.enums import ApplicationStatus

class Application(db.Model):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False, index=True)
    drive_id: Mapped[int] = mapped_column(ForeignKey("placement_drives.id"), nullable=False, index=True)
    status: Mapped[ApplicationStatus] = mapped_column(default=ApplicationStatus.APPLIED)

    __table_args__ = (
        db.UniqueConstraint("drive_id", "student_id", name="unique_student_drive"),
    )