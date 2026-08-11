from server.core.extensions import db
from server.models import PlacementDrive, DriveStatus, Company
from server.repositories import BaseRepository
from sqlalchemy import select, func, or_

class DriveRepository(BaseRepository):
    @staticmethod
    def count_all() -> int:
        stmt = select(func.count(PlacementDrive.id))
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_id(id:int):
        stmt = select(PlacementDrive).filter_by(id=id)
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_status(status: DriveStatus) -> list[PlacementDrive]:
        stmt = select(PlacementDrive).filter_by(status=status)
        return db.session.scalars(stmt).all()

    @staticmethod
    def get_paginated_drives(page: int, search_query: str="", per_page: int=10, status: DriveStatus=None):
        stmt = select(PlacementDrive)
        if status:
            stmt = stmt.filter(PlacementDrive.status == status)
        if search_query:
            stmt = stmt.join(Company).filter(
                or_(
                    PlacementDrive.job_title.ilike(f"%{search_query}%"),
                    Company.name.ilike(f"%{search_query}%")
                )
            )
        return db.paginate(stmt, page=page, per_page=per_page)


    @staticmethod
    def find_by_company_id(company_id: int) -> list[PlacementDrive]:
        stmt = select(PlacementDrive).filter_by(company_id=company_id)
        return db.session.scalars(stmt).all()
