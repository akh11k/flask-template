"""Routes."""
from utils import rq
from service import health


def is_active():
    """Health check."""
    return health.is_active()


def wait(t):
    """Start a sample background rq task that waits t seconds."""
    job = rq.add_task(rq.Queue.default, 'tasks.sample.wait', t)
    return {'job_id': job.id}
