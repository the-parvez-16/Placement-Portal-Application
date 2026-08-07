from server.core.extensions import db
from server.models import User
from server.repositories import BaseRepository

class UserRepository(BaseRepository):
    @staticmethod
    def find_by_email(email: str) -> User | None:
        stmt = db.select(User).filter_by(email=email)

        return db.session.execute(stmt).scalar_one_or_none()        
    
