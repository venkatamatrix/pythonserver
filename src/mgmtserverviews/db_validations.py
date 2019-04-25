from src.models.mgmtservermodel import ManagementServerModel, db
from src.utils.constants import Constants
import re

def validate_username(mgmtServerCommonName):
    """ this is validate method"""
    if not mgmtServerCommonName:
        raise ValueError(Constants.MGMTSERVER_NOT_EXIST)
    if ManagementServerModel.query.filter(ManagementServerModel.mgmtServerCommonName
                                          == mgmtServerCommonName).first():
        raise ValueError(Constants.MGMTSERVER_EXISTS_MSG)
    if len(mgmtServerCommonName) < 1 or len(mgmtServerCommonName) > 100:
        raise ValueError(Constants.MGMTSERVER_NAME_SIZE_MSG)
    return mgmtServerCommonName


def get_all_activemgmtServers():
    """ this is get all"""
    result = db.session.query(ManagementServerModel).filter(
        ManagementServerModel.mgmtServerIsActive == True).all()
    return result


def commonname_data(mgmtServerCommonName):
    """ this is get all"""
    result = db.session.query(ManagementServerModel).filter(
        ManagementServerModel.mgmtServerCommonName == mgmtServerCommonName).all()
    return result


def validate1():
    """ this is validate method"""
    validate_resource = []
    res = db.session.query(ManagementServerModel.mgmtServerId).all()
    for i in res:
        validate_resource.append(i[0])
    return validate_resource
