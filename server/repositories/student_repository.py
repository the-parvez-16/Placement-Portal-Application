from server.core.extensions import db
from server.models import Student
from server.repositories import BaseRepository
from sqlalchemy import select

class StudentRepository(BaseRepository):
    @staticmethod
    def get_by_user_id(user_id: int) -> Student | None:
        stmt = select(Student).filter_by(user_id=user_id)
        return db.session.scalar(stmt)