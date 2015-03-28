import os


class Config(object):
    CACHE_TYPE = 'simple'
    CSRF_ENABLED = True
    DEBUG = False
    SECRET_KEY = os.environ['DATABASE_SECRET']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    TESTING = False


class ProductionConfig(Config):
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = False
    MAIL_PASSWORD = os.environ['EMAIL_PASS']
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
