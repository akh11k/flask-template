"""Flask config."""


class Base(object):
    """Base config."""

    DEBUG = False
    TESTING = False
    REDIS_URI = 'redis://{host}:{port}/{db}'.format(
        host='redis', port=6379, db=0
    )

    # rq-dashboard stuff
    REDIS_URL = REDIS_URI
    RQ_POLL_INTERVAL = 2500
    WEB_BACKGROUND = "black"
    DELETE_JOBS = False


class Dev(Base):
    """Development config."""

    DEBUG = True
    SECRET_KEY = 'dev'


class Prod(Base):
    """Production config."""

    REDIS_URI = 'redis://{host}:{port}/{db}'.format(
        host='',
        port=6379,
        db=0
    )
    SECRET_KEY = ''

    # rq-dashboard stuff
    REDIS_URL = REDIS_URI


class Testing(Base):
    """Testing config."""

    TESTING = True
    SECRET_KEY = 'testing'


def request_logger(response):
    """Log after every request."""
    import logging
    from flask import request
    skip = ['/swagger', '/openapi.json', '/isActive', '/buildInfo', '/rq']
    if not any(x in request.full_path for x in skip):
        uid = None
        uid = uid if uid is not None else 'Guest'
        logging.getLogger('request').info('%s %s %s %s %s %s',
                                          uid,
                                          request.remote_addr,
                                          request.method,
                                          request.scheme,
                                          request.full_path,
                                          response.status)

    return response
