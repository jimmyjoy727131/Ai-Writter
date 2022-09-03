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
