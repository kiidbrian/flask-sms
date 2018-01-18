import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k11dbri@n09231@32'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://kiidbrian:password@127.0.0.1:5432/testdb'
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False


class DockerDevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://kiidbrian:password@postgres/testdb'
    DEBUG = True


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'docker': DockerDevConfig
}
