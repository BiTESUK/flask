'''
    Configure exposed carina modules    

'''
# Set API Private Properties
__major__ = 1
__minor__ = 0
__build__ = 0
__release__ = 'alpha'
__fullVersion__ = 'v{0}.{1}.{2}.{3}'.format(
    __major__, __minor__, __build__, __release__
)

name = 'carina'
# Expose a public short version for URL
version = '{0}.{1}'.format(
        __major__, __minor__
)


# Expose private pointer to configuration classes
from .instance.config import app_config as __config__
# Expose public pointer to CDSL ListManager Classes
from .resources import cdsl as CDSLManager

'''
db = SQLAlchemy()


    Create Flask API
        Configuration controlled by
        app.config - instance.config


def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config(config_name))
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app


def create_carina(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config(config_name))
    app.config.from_pyfile('config.py')
    
    return app


'''
