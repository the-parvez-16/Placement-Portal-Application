from server.core.extensions import db
from server.models import Company
from server.repositories import BaseRepository
from sqlalchemy import select

class CompanyRepository(BaseRepository):
    @staticmethod
    def get_by_user_id(user_id: int) -> Company | None:
        stmt = select(Company).filter_by(user_id=user_id)
        return db.session.scalar(stmt)