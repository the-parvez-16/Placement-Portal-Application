from server.core.extensions import db
from server.models import User, UserRole, UserStatus
from server.repositories import BaseRepository

class UserRepository(BaseRepository):
    @staticmethod
    def find_by_email(email: str) -> User | None:
        stmt = db.select(User).filter_by(email=email)
        return db.session.scalar(stmt)

    @staticmethod
    def count_by_role(role: UserRole) -> int:
        stmt = db.select(func.count(User.id)).filter_by(role=role)
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_role_and_status(role: UserRole, status: UserStatus) -> list[User]:
        stmt = db.select(User).filter_by(role=role, status=status)
        return db.session.scalars(stmt).all()
    
