"""Service."""
import logging

logger = logging.getLogger(__name__)


def is_active():
    """Health check."""
    return True
