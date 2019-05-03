from setuptools import find_packages, setup

setup(
    name='flask-template',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'connexion[swagger-ui]',
        'gevent',
        'gunicorn',
        'pytest',
        'redis',
        'rq',
        'rq-dashboard',
        'tox',
    ],
)
