
# Import Resources available to this API
# These are exposed through the resources# local import of app config settings

from . import api as __api__
from .api.resources import cdsl as __cdsl__
# import .api.resources

# from instance.config import app_config
# from resources import cdsl

__name__ = 'carina'
__version__ = api.version