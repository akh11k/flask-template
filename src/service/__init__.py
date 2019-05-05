"""Service."""
import logging

from utils import rq

logger = logging.getLogger(__name__)


def is_active():
    """Health check."""
    return True


def wait(t):
    job = rq.add_task(rq.Queue.default, 'tasks.sample.wait', t)
    return job.id
