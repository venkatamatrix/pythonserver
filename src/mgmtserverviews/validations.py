"""required validations"""
from src.models.mgmtservermodel import ManagementServerModel, db
from src.utils.constants import Constants
import re




def validate_loggeduser(loggedInUser):
    """ this is validate1 method"""
    if not loggedInUser:
        raise ValueError(Constants.LOGGEDUSER_INFO_EMPTY_MSG)
    if len(loggedInUser) < 1 or len(loggedInUser) > 100:
        raise ValueError(Constants.LOGGEDUSER_SIZE_MSG)
    return loggedInUser



def validate_feilds(req_data):
    if req_data:
        validatename = bool(re.match('^[a-zA-Z0-9-_ ]+$', req_data))
    return validatename

def validate_hostname(hostname):
    if not hostname:
        raise ValueError(Constants.MGMTSERVER_HOSTNAME_NOT_EXIST)
    return hostname

def validate_ipaddress(ipaddress):
    if not ipaddress:
        raise ValueError(Constants.MGMTSERVER_IPADRESS_NOT_EXIST)
    return ipaddress

def validate_fqdn(fqdn):
    if not fqdn:
        raise ValueError(Constants.MGMTSERVER_FQDN_NOT_EXIST)
    return fqdn


def validate_feilds_desc(req_data):
    if req_data:
        validatename = bool(re.match('^[a-zA-Z0-9\_\s,.*()\:\;@&\-\'\"]+$', req_data))
    return validatename
