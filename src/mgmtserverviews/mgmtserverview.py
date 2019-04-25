"""/src/resourceviews/resourceview.py"""
from flask import Blueprint, Flask
from flask_restplus import Api, Resource, fields, apidoc
from ..models.mgmtservermodel import CredentialModel
from src.mgmtserverviews import mgmtserverimplementation
import logging
# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()
logging.basicConfig(level=logging.INFO)


mgmtserverapi = Blueprint('mgmtserver_api', __name__)
app = Flask(__name__)
mgmtserver_api = Api(app, version='0.0.1', title='ManagementServer API with Python',
              description='API for ICP Core services')
ns = mgmtserver_api.namespace('managementServers', description='managementServers operations')

managementServer = mgmtserver_api.model('MgmtServer', {
    'mgmtServerId': fields.Integer(required=True, description='The managementServer Id')
})




@ns.route('/<list:mgmtServerId>')
@ns.response(404, 'Todo not found')
@ns.param('mgmtServerId', 'The task identifier')
class MgmtServer(Resource):
    @ns.doc(params={'mgmtServerId':'get mgmtServerId'})
    @ns.marshal_with(managementServer)
    def get_mgmtserver_by_id(mgmtServerId):
        #Get A workflow  with resourceTypeId
        logging.info("logger output: {} )".format("this is GET method with ids "))
        return mgmtserverimplementation.get_mgmtserver_by_ids(mgmtServerId)

