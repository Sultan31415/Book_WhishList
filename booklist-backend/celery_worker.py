import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery_app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)

# Import tasks so they're registered
import tasks
