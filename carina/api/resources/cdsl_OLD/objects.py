'''
    Class Defs

    All Carina items must either inherit or extend this class.
    This class type is used in the infrastructure
    to ensure object consistency.

'''
import datetime
import re

from flask_restful import Resource

class BaseObject(Resource):
    '''
        Configure Object as per CDSL Spec
        We can base of JSON if needed.
    '''
    @property
    def _type(self):
        return self._type

    @_type.setter
    def _type(self, v):
        self._type = v


    def __init__(self):
        # Private Properties
        self.version = '_alpha'
        self.namemap = {}
        self.class = BaseObject
       
        # Public Properties | Accessors
        self.uri = str()
        self.devices = set()
        self.nodes = set()
        super(BaseObject, self).__init__()
        # ensure tidy name formatting
        # self._type = re.search("(?<=\').*(?=\')",
        #    str(self.__class__)).group()


class PropertyItem(BaseObject):
    '''
        PropertyItem Class
        Inherit the BaseObject
        Override __init__
        Overload public properties
    '''

    @property
    def _type(self):
        return self.___type__

    @property
    def uri(self):
        return self.__uri__

    @uri.setter
    def uri(self, v):
        self.__uri__ = v  

    @property
    def devices(self):
        return self.__devices__

    def __init__(self):
        self.__class__ = PropertyItem
        self.___type__ = re.search("(?<=\').*(?=\')",
            str(self.__class__)).group()
        self.__uri__ = 'MyURI'
        super(PropertyItem, self).__init__()
        