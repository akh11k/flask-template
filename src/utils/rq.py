import logging
from enum import Enum

import rq
import rq.job
from flask import current_app, abort

logger = logging.getLogger(__name__)


class Queue(Enum):
    default = current_app.default_task_queue


def add_task(queue, function, *args, **kwargs):
    """Add a task to the rq queue.

    :param queue: A utils.rq.Queue, the queue to add the function to.
    :param function: A str, the function import string.
    :param args: args
    :param kwargs: kwargs
    :return: A rq.Job, the enqueued job object.
    """
    return queue.value.enqueue(function, args=args, kwargs=kwargs,
                               timeout=14400)


def set_task_progress(progress):
    """Set custom progress in a task."""
    job = rq.get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()


def get_task(task_id):
    """Get the task info with the give ID."""
    job = rq.job.Job.fetch(task_id, current_app.redis)
    if job is None:
        abort(404)
    return {
        'status': job.get_status(),
        'result': job.result,
        'progress': job.meta.get('progress', 'NA')
    }
