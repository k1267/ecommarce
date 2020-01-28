class Config(object):
    SECRET_KEY='admin@124'
    SQLALCHEMY_DATABASE_URI='mysql://root:root@localhost/onlineportal1_db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True
class ProductionConfig(Config):
    DEBUG=False
app_config={
    'development':DevelopmentConfig,
    'production':ProductionConfig}