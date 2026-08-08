from server.core.extensions import db
from server.models import PlacementDrive, DriveStatus
from server.repositories import BaseRepository
from sqlalchemy import func

class DriveRepository(BaseRepository):
    @staticmethod
    def count_all() -> int:
        stmt = db.select(func.count(PlacementDrive.id))
        return db.session.scalar(stmt)

    @staticmethod
    def find_by_status(status: DriveStatus) -> list[PlacementDrive]:
        stmt = db.select(PlacementDrive).filter_by(status=status)
        return db.session.scalars(stmt).all()

    