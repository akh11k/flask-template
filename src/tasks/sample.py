"""Example tasks."""
import time

from flask import current_app

from utils import rq


def get_current_config():
    """Get flask config."""
    return current_app.config


def wait(t):
    """Wait t seconds."""
    i = 0
    while i < t:
        time.sleep(1)
        rq.set_task_progress(int(i * 100 / t))
        i = i + 1
    return True
