import json
import datetime

from flask_restful import Resource, reqparse, abort, fields, marshal_with

__CDSL_ITEMS__ = []

def get_Items(self):
    return __CDSL_ITEMS__

def abort_if_item_doesnt_exist(id):
    if id not in __CDSL_ITEMS__:
        abort(404, message="Item {} doesn't exist".format(item_id))

postData = reqparse.RequestParser()

# Configure required payload arguments

# The type of CDSL Object - TODO: Confirm types
postData.add_argument(
    'type', dest='_type', required=False, location='json',
    help='The CDSL Object type to create')

# The name of the object
postData.add_argument(
    'name', dest='name', required=False, location='json',
    help='the name for the object to create')

# 
postData.add_argument(
    'type', dest='_type', required=False, location='json',
    help='The CDSL Object type to create')


# List all Mandatory fields
# These fields apply to ALL objects
cdsl_mandatory = [{
    'id': fields.String,
}]

cdsl_required = [{
    '_type': fields.String,
    'name': fields.String
 }]

cdsl_optional = [{
    'someOptional': fields.String
}]

cdsl_ALL = [ 
"""     {
        json.dumps(cdsl_mandatory),
        json.dumps(cdsl_required)
    } """
]

class CDSLObject(Resource):

    @property
    def _type(self):
        return self._type

    @_type.setter
    def _type(self, v):
        self._type = v

    def __iter__(self):
        return self.__dict__.items()

    def __init__(self):
        # Private Properties
        self.version = '_alpha'
      
        # Public Properties | Accessors
        self.uri = str()
        self.devices = set()
        self.nodes = set([CDSLObject])
        super(CDSLObject, self).__init__()

    # Marshal for validity
    @marshal_with(cdsl_mandatory)
    def get(self, id):
        abort_if_item_doesnt_exist(id)
        return self.__CDSL_ITEMS__[id], 400

    def delete(self, id):
        abort_if_item_doesnt_exist(id)
        try:
            del self.__CDSL_ITEMS__[id]
        except Exception as e:
            return e

        return "Deleted {}".format(id), 204

    @marshal_with(cdsl_required)
    def put(self, id):
        args = parser.parse_args()
        # Create a new CDSL Object instance
        # and populate the supplied params
        cdslItem = BaseObject()
        cdslItem.___type = 'NEW ITEM TYPE'

        return "yes", 201


class CDSLList(Resource):

    def __init__(self):
        super(CDSLList, self).__init__() 
   
    def get(self):
        return __CDSL_ITEMS__, 200

    def post(self):
        args = parser.parse_args()
        id = int(max(self.__CDSL_ITEMS__.keys()).lstrip('item')) + 1
        id = "_SomePrefix%i" % id
        self.__CDSL_ITEMS__[id] = {'task': args['task']}
        return self.__CDSL_ITEMS__[id], 201