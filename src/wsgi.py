"""Root wsgi module."""
import gevent.monkey

gevent.monkey.patch_all()

# configure logging.
with open('logging.yaml', 'r') as logging_conf:
    import yaml
    import logging.config

    logging.config.dictConfig(yaml.load(logging_conf, Loader=yaml.FullLoader))

import os  # noqa E402
from factory import create_app  # noqa E402

if os.environ.get('DEV_ENV', None):
    env = 'dev'
else:
    env = 'prod'
app = create_app(env)

if __name__ == "__main__":
    app.run(port=8080)
