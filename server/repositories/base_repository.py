from server.core.extensions import db

class BaseRepository:
    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def save(model_instance):
        db.session.add(model_instance)
        db.session.flush()
        return model_instance