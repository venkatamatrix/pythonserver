""" src/models/resourcetypemodel.py"""
from . import db
import datetime
from marshmallow import fields, Schema


class ManagementServerModel(db.Model):
    """ ManagementServerModel"""
    __tablename__ = 'managementservers'

    mgmtServerId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mgmtServerCommonName = db.Column(db.String(100), unique=True, nullable=False)
    mgmtServerHostName = db.Column(db.String(100), unique=True, nullable=False)
    mgmtServerFQDN = db.Column(db.String(500), unique=True, nullable=False)
    mgmtServerIPAddress = db.Column(db.String(15), unique=True, nullable=False)
    mgmtServerIPV6 = db.Column(db.String(39), nullable=True)
    oSCredentialId = db.Column(db.Integer, db.ForeignKey('credentials.credentialId'), nullable=True)
    appCredentialId1 = db.Column(db.Integer, db.ForeignKey('credentials.credentialId'), nullable=True)
    appCredentialId2 = db.Column(db.Integer, db.ForeignKey('credentials.credentialId'), nullable=True)
    appCredentialId3 = db.Column(db.Integer, db.ForeignKey('credentials.credentialId'), nullable=True)
    appCredentialId4 = db.Column(db.Integer, db.ForeignKey('credentials.credentialId'), nullable=True)
    mgmtServerDesc = db.Column(db.String(500), unique=True, nullable=False)
    mgmtServerRemarks = db.Column(db.String(500), unique=True, nullable=False)
    mgmtServerIsActive = db.Column(db.Boolean(), nullable=False)
    createdBy = db.Column(db.String(100), nullable=False)
    createdOn = db.Column(db.DateTime, nullable=False)
    lastUpdatedBy = db.Column(db.String(100), nullable=True)
    lastUpdatedOn = db.Column(db.DateTime, nullable=True)

    def __init__(self, data):
        self.mgmtServerCommonName = data.get('mgmtServerCommonName')
        self.mgmtServerHostName = data.get('mgmtServerHostName')
        self.mgmtServerFQDN = data.get('mgmtServerFQDN')
        self.mgmtServerIPAddress = data.get('mgmtServerIPAddress')
        self.mgmtServerIPV6 = data.get('mgmtServerIPV6')
        self.oSCredentialId = data.get('oSCredentialId')
        self.appCredentialId1 = data.get('appCredentialId1')
        self.appCredentialId2 = data.get('appCredentialId2')
        self.appCredentialId3 = data.get('appCredentialId3')
        self.appCredentialId4 = data.get('appCredentialId4')
        self.mgmtServerDesc = data.get('mgmtServerDesc')
        self.mgmtServerRemarks = data.get('mgmtServerRemarks')
        self.mgmtServerIsActive = data.get('mgmtServerIsActive')
        self.createdBy = data.get('createdBy')
        self.createdOn = datetime.datetime.utcnow()
        self.lastUpdatedBy = data.get('lastUpdatedBy')
        self.lastUpdatedOn = datetime.datetime.utcnow()

    def save(self, loggeduser):
        """ this is save method"""
        db.session.add(self)
        self.mgmtServerIsActive = True
        self.createdBy = loggeduser
        self.lastUpdatedBy = loggeduser
        db.session.commit()

    def update(self, data, loggeduser):
        """ this is update method"""
        for key, item in data.items():
            setattr(self, key, item)
        self.lastUpdatedBy = loggeduser
        self.lastUpdatedOn = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self, data, loggeduser):
        """ this is delete method"""
        for key, item in data.items():
            setattr(self, key, item)
        self.mgmtServerIsActive = False
        self.lastUpdatedBy = loggeduser
        self.lastUpdatedOn = datetime.datetime.utcnow()
        db.session.commit()

    def __repr__(self):
        return '<mgmtServerId {}>'.format(self.mgmtServerId)


class ManagementServerSchema(Schema):
    """ ManagementServerSchema  """
    mgmtServerId = fields.Int(dump_only=True)
    mgmtServerCommonName = fields.Str(required=False)
    mgmtServerHostName = fields.Str(required=False)
    mgmtServerFQDN = fields.Str(required=False)
    mgmtServerIPAddress = fields.Str(required=False)
    mgmtServerIPV6 = fields.Str(required=False)
    oSCredentialId = fields.Int(required=True)
    appCredentialId1 = fields.Int(required=True)
    appCredentialId2 = fields.Int(required=True)
    appCredentialId3 = fields.Int(required=True)
    appCredentialId4 = fields.Int(required=True)
    mgmtServerDesc = fields.Str(required=False)
    mgmtServerRemarks = fields.Str(required=False)
    mgmtServerIsActive = fields.Boolean(required=True)
    """ below attributes will be uncommented when customer needs """
    # createdBy = fields.Str(required=False)
    # createdOn = fields.DateTime(dump_only=True)
    # lastUpdatedBy = fields.Str(required=False)
    # lastUpdatedOn = fields.DateTime(dump_only=True)

class CredentialModel(db.Model):
    """ ServiceModel"""
    __tablename__ = 'credentials'

    credentialId = db.Column(db.Integer, primary_key=True)

    def save(self):
        """ this is save method"""
        db.session.add(self)
        db.session.commit()


class CredentialSchema(Schema):
    """ ServiceSchema """
    credentialId = fields.Int(dump_only=True)
