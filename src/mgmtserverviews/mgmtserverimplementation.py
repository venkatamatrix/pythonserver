"""/src/mgmtserverviews/mgmtserverimplementation.py"""
from http import HTTPStatus
from flask import request, json, Response, abort
from ..models.mgmtservermodel import ManagementServerModel, ManagementServerSchema
from ..utils import responsehandler
from src.mgmtserverviews import validations, db_validations
from src.utils.constants import Constants
import logging

logging.basicConfig(level=logging.INFO)

mgmtserver_schema = ManagementServerSchema()


def mgmtserver_creation():
    """
    create mgmtservers
    """
    try:
        logging.debug("looger output: {} )".format("this is mgmtserver creation method"))
        req_data = request.get_json()
        validations.validate_hostname(req_data["mgmtServerHostName"])
        validations.validate_fqdn(req_data["mgmtServerFQDN"])
        validations.validate_ipaddress(req_data["mgmtServerIPAddress"])
        if validations.validate_feilds(req_data["mgmtServerCommonName"]):
            if validations.validate_feilds_desc(req_data["mgmtServerDesc"]):
                if validations.validate_feilds_desc(req_data["mgmtServerRemarks"]):
                    validations.validate_loggeduser(req_data["loggedInUser"])
                    db_validations.validate_username(req_data["mgmtServerCommonName"])
                    mgmtserverdata, error = mgmtserver_schema.load(req_data)
                    post = ManagementServerModel(mgmtserverdata)
                    post.save(req_data["loggedInUser"])
                    mgmtserverdata = mgmtserver_schema.dump(post).mgmtserverdata
                    logging.debug("looger output: {} )".format(mgmtserverdata))
                    return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.CREATED),
                                           HTTPStatus.CREATED)
                else:
                    raise ValueError(Constants.FEILD_VALUE_NOT_VALID_REMARKS)
            else:
                raise ValueError(Constants.FEILD_VALUE_NOT_VALID_DESC)
        else:
            raise ValueError(Constants.FEILD_VALUE_NOT_VALID)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.PRECONDITION_FAILED), HTTPStatus.OK)
    except:
        return custom_response(
            responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY), HTTPStatus.OK)


def get_all_managementservers():
    """
    Get All  mgmtservers
    """
    try:
        logging.debug("logger output: {} )".format("this is to get all mgmtservers"))
        resourcetype = ManagementServerModel.query.all()
        if not resourcetype:
            raise ValueError(Constants.MGMTSERVER_DATA_EMPTY)
        else:
            mgmtserverdata = mgmtserver_schema.dump(resourcetype, many=True).data
            logging.debug("logger output: {} )".format(mgmtserverdata))
            return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.OK), HTTPStatus.OK)
    except ValueError as error:
        logging.debug("logger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NO_CONTENT), HTTPStatus.OK)
    except:
        return custom_response(
            responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY), HTTPStatus.OK)


def get_mgmtserver_by_ids(mgmtServerId):
    """
        Get All  mgmtservers by ids
    """
    logging.debug("logger output: {} )".format("this is to get mgmtServer by ids"))
    data1 = []
    err = []
    for i in mgmtServerId:
        j = i.split(",")
        for h in j:
            try:
                mgmtServerId = int(h)
                post = ManagementServerModel.query.get(mgmtServerId)
                if mgmtServerId in (db_validations.validate1()):
                    if not post:
                        abort(404)
                    data = mgmtserver_schema.dump(post).data
                    data1.append(data)
                else:
                    raise ValueError(Constants.MGMTSERVER_NOT_EXIST_MSG)
            except ValueError as error:
                logging.debug("logger output: {} )".format(error))
                err.append(responsehandler.errordata1(mgmtServerId))
            except:
                return custom_response(
                    responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY),
                    HTTPStatus.OK)
    logging.debug("logger output: {} )".format(data1))
    return custom_response(responsehandler.dbresponsed1(data1, err, HTTPStatus.OK), HTTPStatus.OK)


def get_mgmtserver_by_name(mgmtServerCommonName):
    """
    Get All  active mgmtservers
    """
    logging.info("looger output: {} )".format("this is GET method for all commonname_data "))
    try:
        commonname_data = db_validations.commonname_data(mgmtServerCommonName)
        if not commonname_data:
            raise ValueError(Constants.MGMTSERVER_NOT_EXIST_MSG)
        mgmtserverdata = mgmtserver_schema.dump(commonname_data, many=True).data
        logging.debug("looger output: {} )".format(mgmtserverdata))
        return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.OK), HTTPStatus.OK)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NOT_FOUND), HTTPStatus.OK)


def update_managementserver(mgmtServerId):
    """
    Update mgmtserver by id
    """
    try:
        logging.debug("logger output: {} )".format("this is mgmtserver updation method"))
        req_data = request.get_json()
        validations.validate_hostname(req_data["mgmtServerHostName"])
        validations.validate_fqdn(req_data["mgmtServerFQDN"])
        validations.validate_ipaddress(req_data["mgmtServerIPAddress"])
        post = ManagementServerModel.query.get(mgmtServerId)
        if mgmtServerId in db_validations.validate1():
            if validations.validate_feilds(req_data["mgmtServerCommonName"]):
                if validations.validate_feilds_desc(req_data["mgmtServerDesc"]):
                    if validations.validate_feilds_desc(req_data["mgmtServerRemarks"]):
                        db_validations.validate_username(req_data["mgmtServerCommonName"])
                        validations.validate_loggeduser(req_data["loggedInUser"])
                        mgmtserverdata, error = mgmtserver_schema.load(req_data, partial=True)
                        if error:
                            abort(404)
                        post.update(mgmtserverdata, req_data["loggedInUser"])
                        mgmtserverdata = mgmtserver_schema.dump(post).mgmtserverdata
                        logging.debug("logger output: {} )".format(mgmtserverdata))
                        return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.OK), HTTPStatus.OK)
                    else:
                        raise ValueError(Constants.FEILD_VALUE_NOT_VALID_REMARKS)
                else:
                    raise ValueError(Constants.FEILD_VALUE_NOT_VALID_DESC)
            else:
                raise ValueError(Constants.FEILD_VALUE_NOT_VALID)
        else:
            raise ValueError(Constants.PRECONDITION_FAILURE_MSG)
    except ValueError as error:
        logging.debug("logger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NOT_FOUND), HTTPStatus.OK)
    except:
        return custom_response(
            responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY), HTTPStatus.OK)


def get_all_activemanagementservers():
    """
    Get All  active mgmtservers
    """
    try:
        logging.debug("logger output: {} )".format("this is to get all active resources"))
        activeresources = db_validations.get_all_activemgmtServers()
        if not activeresources:
            raise ValueError(Constants.NO_ACTIVE_MGMTSERVER_MSG)
        mgmtserverdata = mgmtserver_schema.dump(activeresources, many=True).mgmtserverdata
        logging.debug("logger output: {} )".format(mgmtserverdata))
        return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.OK), HTTPStatus.OK)
    except ValueError as error:
        logging.debug("logger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NOT_FOUND), HTTPStatus.OK)
    except:
        return custom_response(
            responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY), HTTPStatus.OK)


def deleteManagementServer(mgmtServerId, loggedInUser):
    """
    Delete mgmtserver by id and loggedname
    """
    logging.debug("logger output: {} )".format("this is resource deletion method"))
    post = ManagementServerModel.query.get(mgmtServerId)
    mgmtserverdata = mgmtserver_schema.dump(post).mgmtserverdata
    try:
        if mgmtServerId in db_validations.validate1():
            if mgmtserverdata['mgmtServerIsActive']:
                validations.validate_loggeduser(loggedInUser)
                if not post:
                    abort(404)
                mgmtserverdata = mgmtserver_schema.dump(post).mgmtserverdata
                post.delete(mgmtserverdata, loggedInUser)
                mgmtserverdata = mgmtserver_schema.dump(post).mgmtserverdata
                logging.debug("logger output: {} )".format(mgmtserverdata))
                return custom_response(responsehandler.dbresponsed(mgmtserverdata, HTTPStatus.OK), HTTPStatus.OK)
            else:
                raise ValueError(Constants.MGMTSERVER_NOT_ACTIVE)
        else:
            raise ValueError(Constants.PRECONDITION_FAILURE_MSG)
    except ValueError as error:
        logging.debug("logger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.PRECONDITION_FAILED), HTTPStatus.OK)
    except:
        return custom_response(
            responsehandler.errordata(Constants.SAVE_FLUSH_FAILURE_MSG, HTTPStatus.FAILED_DEPENDENCY), HTTPStatus.OK)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
