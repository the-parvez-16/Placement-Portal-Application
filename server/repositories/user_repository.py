from server.core.extensions import db
from server.models import User, UserRole, UserStatus, Company, Student
from server.repositories import BaseRepository
from sqlalchemy import func, select, or_

class UserRepository(BaseRepository):
    @staticmethod
    def find_by_id(id: int) -> User | None:
        stmt = select(User).filter_by(id=id)
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_email(email: str) -> User | None:
        stmt = select(User).filter_by(email=email)
        return db.session.scalar(stmt)

    @staticmethod
    def count_by_role(role: UserRole) -> int:
        stmt = select(func.count(User.id)).filter_by(role=role)
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_role_and_status(role: UserRole, status: UserStatus) -> list[User]:
        stmt = select(User).filter_by(role=role, status=status)
        return db.session.scalars(stmt).all()

    @staticmethod
    def get_pending_companies(search_query=""):
        stmt = select(User).filter_by(role=UserRole.COMPANY, status=UserStatus.APPLIED)
        
        if search_query:
            stmt = stmt.join(Company).filter(
                or_(
                    Company.name.ilike(f"%{search_query}%"),
                    Company.industry.ilike(f"%{search_query}%")
                )
            )
            
        return db.session.scalars(stmt).all()

    
    @staticmethod
    def get_paginated_companies(page: int, search_query: str = "", per_page: int = 10):
        stmt = select(User).filter_by(role=UserRole.COMPANY)
        
        if search_query:
            stmt = stmt.join(Company).filter(
                or_(
                    Company.name.ilike(f"%{search_query}%"),
                    Company.industry.ilike(f"%{search_query}%")
                )
            )

        return db.paginate(stmt, page=page, per_page=per_page)

    @staticmethod
    def get_paginated_students(page: int, search_query: str = "", per_page: int = 10):
        stmt = select(User).filter_by(role=UserRole.STUDENT)
        
        if search_query:
            stmt = stmt.join(Student).filter(
                or_(
                    Student.name.ilike(f"%{search_query}%"),
                    Student.branch.ilike(f"%{search_query}%")
                )
            )

        return db.paginate(stmt, page=page, per_page=per_page)
