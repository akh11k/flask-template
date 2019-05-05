"""RQ tasks."""
import os
from factory import create_app

if os.environ.get('DEV_ENV', None):
    env = 'dev'
else:
    env = 'prod'
app = create_app(env).app
app.app_context().push()
