""" import synctool.configparser
import synctool.lib
import synctool.param
import synctool.range
from synctool import config, param, nodeset
from synctool.lib import error, stderr, verbose, warning
 """
import json
import carina
from carina.api.resources.cdsl import CDSLList
from carina.api.resources.cdsl import CDSLObject

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(carina.api.name)
api = Api(app)

# Create instances of our list management classes
# CDSLManger = carina.api.resources.cdsl.CDSLManger()
# CDSLItem = carina.api.resources.cdsl.CDSLItem()

URI_ROOT = '/carina/{0}'.format(carina.api.version)

# inherit our cdsl classes
class cdsl_root(CDSLList):
    _type = 'RootList'

class cdsl_ci(CDSLObject):
    _type = 'ci_list'


# cdsl_root = CDSLList
cdsl_ci_list = CDSLList()
# cdsl_ci = CDSLObject
cdsl_param_list = CDSLList()
cdsl_param = CDSLObject()
cdsl_attr = CDSLObject()

api.add_resource(cdsl_root,
    URI_ROOT.__add__('/'), endpoint='cdsl_list')

api.add_resource(cdsl_ci_list, 
    URI_ROOT.__add__('/cilist'), endpoint='cdsl_ci_list')

api.add_resource(cdsl_ci,
    URI_ROOT.__add__('/ci'), endpoint='cdsl_ci')

api.add_resource(cdsl_param_list, 
    URI_ROOT.__add__('/paramlist'), endpoint='cdsl_param_list')

api.add_resource(cdsl_param, 
    URI_ROOT.__add__('/param'), endpoint='cdsl_param')


if __name__ == 'main':
    app.run(debug=false)
