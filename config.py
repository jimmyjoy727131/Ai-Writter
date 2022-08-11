##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
