from server.core.extensions import db
from server.models import Application, ApplicationStatus
from server.repositories import BaseRepository

class ApplicationRepository(BaseRepository):
    @staticmethod
    def count_all() -> int:
        stmt = db.select(func.count(Application.id))
        return db.session.scalar(stmt)