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


cdsl_root = CDSLList()
cdsl_ci_list = CDSLList()
cdsl_ci = CDSLObject


api.add_resource(cdsl_root,
    URI_ROOT.__add__('/'), endpoint='cdsl_list')

api.add_resource(cdsl_ci_list, 
    URI_ROOT.__add__('/cilist'), endpoint='cdsl_ci_list')

if __name__ == 'main':
    app.run(debug=false)
