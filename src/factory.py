"""Application factory."""
import rq
import connexion
import rq_dashboard
from redis import Redis


def create_app(env):
    """Create and configure connexion app."""
    connexion_app = connexion.App(__name__, specification_dir='openapi/',
                                  options={'swagger_url': '/swagger'})
    app = connexion_app.app
    env_config_class_map = {
        'prod': 'config.Prod',
        'testing': 'config.Testing',
        'dev': 'config.Dev'
    }
    config_class = env_config_class_map.get(env)
    app.config.from_object(config_class)
    print(app.config)
    app.redis = Redis.from_url(app.config['REDIS_URI'])
    app.default_task_queue = rq.Queue('default', connection=app.redis, ttl=-1)
    with app.app_context():
        import config as flask_config
        app.after_request(flask_config.request_logger)
        app.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')
        connexion_app.add_api('spec.yaml')
    return connexion_app
