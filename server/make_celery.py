from server.core import create_app
from server.core.extensions import celery_app

app = create_app()