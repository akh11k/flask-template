"""Root wsgi module."""
import gevent.monkey

gevent.monkey.patch_all()

# configure logging.
with open('logging.yaml', 'r') as logging_conf:
    import yaml
    import logging.config

    logging.config.dictConfig(yaml.load(logging_conf, Loader=yaml.FullLoader))

from factory import create_app  # noqa E402

app = create_app()

if __name__ == "__main__":
    app.run(port=8080)
