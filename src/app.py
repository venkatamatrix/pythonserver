"""/src/app.py"""
import os
from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.routing import BaseConverter
from .config import app_config
from .models import db, bcrypt
from src.mgmtserverviews import mgmtserverimplementation

port = os.getenv('PORT')


class ListConverter(BaseConverter):
    """List Converter"""
    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)for value in values)


def create_app(env_name):
    """
  Create application
  """
    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.url_map.converters['list'] = ListConverter

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)
    api = Api(app, default='ManagementServer', default_label='This is the ManagementServer service', version='0.0.1', title='ManagementServer API with Python',
                           description='API for ICP OpsAuto services', ordered=True
                           )
    managementServerSchema = api.model('managementServerSchema', {
        'loggedInUser': fields.String(required=True, description='The loggedInUser'),
        'mgmtServerCommonName': fields.String(required=False, description='The mgmtServerCommonName'),
        'mgmtServerHostName': fields.String(description='The mgmtServerHostName'),
        'mgmtServerFQDN': fields.String(description='mgmtServerFQDN'),
        'mgmtServerIPAddress': fields.String(description='mgmtServerIPAddress'),
        'oSCredentialId': fields.Integer(dump_only=True),
        'appCredentialId1': fields.Integer(dump_only=True),
        'appCredentialId2': fields.Integer(dump_only=True),
        'appCredentialId3': fields.Integer(dump_only=True),
        'appCredentialId4': fields.Integer(dump_only=True),
        'mgmtServerIPV6': fields.String(description='mgmtServerIPV6'),
        'mgmtServerDesc': fields.String(description='mgmtServerDesc'),
        'mgmtServerRemarks': fields.String(description='mgmtServerRemarks'),
        'mgmtServerIsActive': fields.Boolean(description='mgmtServerIsActive', required=True)
        })


    managementServerPut = api.model('managementServerPut', {
        'loggedInUser': fields.String(required=True, description='The loggedInUser'),
        'mgmtServerCommonName': fields.String(required=False, description='The mgmtServerCommonName'),
        'mgmtServerHostName': fields.String(description='The mgmtServerHostName'),
        'mgmtServerFQDN': fields.String(description='mgmtServerFQDN'),
        'mgmtServerIPAddress': fields.String(description='mgmtServerIPAddress'),
        'oSCredentialId': fields.Integer(dump_only=True),
        'appCredentialId1': fields.Integer(dump_only=True),
        'appCredentialId2': fields.Integer(dump_only=True),
        'appCredentialId3': fields.Integer(dump_only=True),
        'appCredentialId4': fields.Integer(dump_only=True),
        'mgmtServerIPV6': fields.String(description='mgmtServerIPV6'),
        'mgmtServerDesc': fields.String(description='mgmtServerDesc'),
        'mgmtServerRemarks': fields.String(description='mgmtServerRemarks')
        })
    managementServer = api.model('managementServer', {
        'loggedInUser': fields.String(required=True, description='The loggedInUser'),
        'mgmtServerCommonName': fields.String(required=False, description='The mgmtServerCommonName'),
        'mgmtServerHostName': fields.String(description='The mgmtServerHostName'),
        'mgmtServerFQDN': fields.String(description='mgmtServerFQDN'),
        'mgmtServerIPAddress': fields.String(description='mgmtServerIPAddress'),
        'oSCredentialId': fields.Integer(dump_only=True),
        'appCredentialId1': fields.Integer(dump_only=True),
        'appCredentialId2': fields.Integer(dump_only=True),
        'appCredentialId3': fields.Integer(dump_only=True),
        'appCredentialId4': fields.Integer(dump_only=True),
        'mgmtServerIPV6': fields.String(description='mgmtServerIPV6'),
        'mgmtServerDesc': fields.String(description='mgmtServerDesc'),
        'mgmtServerRemarks': fields.String(description='mgmtServerRemarks'),
        'mgmtServerIsActive': fields.Boolean(description='mgmtServerIsActive', required=True)
    })

    managementServerBaseResponse = api.model('managementServerBaseResponse', {
        'applicationCode': fields.Integer(),
        'code': fields.Integer(),
        'message': fields.String(),
        'status': fields.String()
    })

    managementServerResponse = api.inherit('managementServerResponse', managementServerBaseResponse, {'managementServer':
                                                                                                          fields.List(fields.Nested(managementServerSchema))
    })

    @api.route('/managementServers/<list:mgmtServerId>')
    class ManagementServerByIds(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(params={'mgmtServerId': 'mgmtServerId'}, responses={400: 'ERROR', 500: 'SERVER_ERROR'}, description='Get managementServer by Ids')
        def get(self, mgmtServerId):
            return mgmtserverimplementation.get_mgmtserver_by_ids(mgmtServerId)

    @api.route('/managementServers/mgmtServerCommonNames/<mgmtServerCommonName>')
    class ManagementServerByIds(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(params={'mgmtServerCommonName': 'mgmtServerCommonName'}, responses={400: 'ERROR', 500: 'SERVER_ERROR'},
                 description='Get managementServer by Ids')
        def get(self, mgmtServerCommonName):
            return mgmtserverimplementation.get_mgmtserver_by_name(mgmtServerCommonName)

    @api.route('/managementServers/<int:mgmtServerId>')
    class ManagementServerUpdate(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(params={'mgmtServerId': 'mgmtServerId'}, responses={400: 'ERROR', 500: 'SERVER_ERROR'}, description='Get managementServer by Ids')
        @api.expect(managementServer)
        def put(self, mgmtServerId):
            return mgmtserverimplementation.update_managementserver(mgmtServerId)

    @api.route('/managementServers')
    class ManagementServerCreation(Resource):
        @api.response(201, 'CREATED', managementServerResponse)
        @api.doc(responses={400: 'ERROR', 500: 'SERVER_ERROR'}, description='create a management server')
        @api.expect(managementServerPut)
        def post(self):
            print("this is post")
            return mgmtserverimplementation.mgmtserver_creation()

    @api.route('/managementServers/allManagementServers')
    class AllResourceTypes(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(responses={400: 'ERROR', 500: 'SERVER_ERROR'}, description='Get managementServer by Ids')
        def get(self):
            return mgmtserverimplementation.get_all_managementservers()

    @api.route('/managementServers/allActiveManagementServers')
    class AllActiveManagementServers(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(responses={400: 'ERROR', 500: 'SERVER_ERROR'}, )
        def get(self):
            return mgmtserverimplementation.get_all_activemanagementservers()

    @api.route('/managementServers/<int:mgmtServerId>/<loggedInUser>')
    class ResourceType(Resource):
        @api.response(200, 'OK', managementServerResponse)
        @api.doc(params={'mgmtServerId': 'An ID', 'loggedInUser': 'loggedInUser'}, responses={400: 'ERROR', 500:'SERVER_ERROR'}, description='Get mgmtServer by Ids')
        def delete(self, mgmtServerId, loggedInUser):
            return mgmtserverimplementation.deleteManagementServer(mgmtServerId, loggedInUser)
    return app
