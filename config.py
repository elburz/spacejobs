import os


class Config(object):
    CACHE_TYPE = 'simple'
    CSRF_ENABLED = True
    DEBUG = False
    SECRET_KEY = 'd706881f-db67-4f7d-9e5b-8819ed9bf786'
    SQLALCHEMY_DATABASE_URI = 'postgres://rshxhlpvyizqlx:QpX2BJsjrDHiuF4VhrP6jYkIdJ@ec2-184-73-194-196.compute-1.amazonaws.com:5432/d3mhuhudar4m8c'
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    # MAIL_PASSWORD = os.environ['EMAIL_PASS']
    MAIL_PORT = 465
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'spacejobs.us@gmail.com'
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False


class DevelopmentConfig(Config):
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEVELOPMENT = True
    DEBUG = True
