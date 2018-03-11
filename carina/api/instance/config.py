import os

'''
    Configuration Wrapper for environmental
    variables

'''

class Config(object):
    '''
        Parent configuration class.
        All other environments inherit
        this class
    '''
    DEBUG = False
    SECRET = None
    DB_URI = None


class Development(Config):
    '''
        Config for DEV
    '''
    DEBUG = True


class Testing(Config):
    '''
        Config for Tests
    '''
    TESTING = True
    DEBUG = True
    DB_URI = None
    SECRET = None


class Production(Config):
    '''
        Config for Prod
    '''
    DEBUG = False
    DB_URI = None
    TESTING = False


'''
    Settings array for all environments
'''

app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}