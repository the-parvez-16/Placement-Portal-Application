from server.core.extensions import db
from server.models import Application, ApplicationStatus
from server.repositories import BaseRepository
from sqlalchemy import func, select

class ApplicationRepository(BaseRepository):
    @staticmethod
    def count_all() -> int:
        stmt = select(func.count(Application.id))
        return db.session.scalar(stmt)

    @staticmethod
    def get_recent_applications(limit=5):
        stmt = select(Application).order_by(Application.id.desc()).limit(limit)
        return db.session.scalars(stmt).all()

    @staticmethod
    def get_paginated_applications(page: int, search_query: str = "", per_page: int = 10):
        stmt = select(Application)
        if search_query:
            stmt = stmt.join(Student).join(PlacementDrive).filter(
                or_(Student.name.ilike(f"%{search_query}%"),
                PlacementDrive.job_title.ilike(f"%{search_query}%"))
            )
        return db.paginate(stmt, page=page, per_page=per_page)

    @staticmethod
    def find_by_student_and_drive(student_id: int, drive_id: int):
        stmt = select(Application).filter_by(student_id=student_id, drive_id=drive_id)
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_drive_id(drive_id: int):
        stmt = select(Application).filter_by(drive_id=drive_id)
        return db.session.scalars(stmt).all()

    @staticmethod
    def find_by_student_id(student_id: int):
        stmt = select(Application).filter_by(student_id=student_id)
        return db.session.scalars(stmt).all()

    @staticmethod
    def find_by_id(id: int) -> Application | None:
        stmt = select(Application).filter_by(id=id)
        return db.session.scalar(stmt)
