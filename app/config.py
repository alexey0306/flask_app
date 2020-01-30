import os,tempfile

class Config(object):

    # Paths
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CACHE_DIR = os.path.join(BASE_DIR,"cache")
    TMP_DIR = os.path.join(BASE_DIR,"static")
    UPLOADS_DIR = os.path.join(BASE_DIR,"static")


class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite://' + path.join(path.pardir,'database.db')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://azelenkin:testtest@webserver:3306/backend"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "webserver"
    REDIS_PORT = 6379
    REDIS_EXPIRES = 3600 # 1 hour
    CELERY_BROKER_URL = "redis://%s:6379" % REDIS_HOST
    CELERY_BACKEND_URL = "redis://%s:6379" % REDIS_HOST
