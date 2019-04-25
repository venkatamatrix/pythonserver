"""these are the constants using"""


class Constants:  # pylint: disable=too-few-public-methods
    """these are the constants using"""
    FAILED_DEPENDENCY_MESSAGE = "Incorrect information found for provided Subscriber key(s), " \
                                "Please contact DealDesk for support"
    FINDALL_FAILURE_MSG = "Failed to retrieve the subscriber records from DB," \
                          " Please contact DealDesk for support"
    SAVE_FLUSH_FAILURE_MSG = "Failed to save the subscriber records into DB," \
                             " Please contact DealDesk for support"
    NO_ACTIVE_MGMTSERVER_MSG = "No Active MgmtServer found!!"
    PRECONDITION_FAILURE_MSG = "The MgmtServerTypeId doesn't exist Please load valid info"
    MGMTSERVER_EXISTS_MSG = "The MgmtServer Name you are trying to insert already exists," \
                            " please provide a different name"
    MGMTSERVER_NOT_EXIST = "No MgmtServerName provided"
    MGMTSERVER_NOT_EXIST_MSG = "The MgmtServer you are trying to update/get does not exist"
    MGMTSERVER_ID_EMPTY_MSG = "The MMgmtServer ID cannot be empty"
    MGMTSERVER_NAME_EMPTY_MSG = "The MgmtServer name cannot be empty"
    MGMTSERVER_NAME_NULL_MSG = "The MgmtServer name cannot be null"
    MGMTSERVER_NAME_SIZE_MSG = "The MgmtServer name must be between 5 and 100 characters"
    MGMTSERVER_IS_ACTIVE = "Please provide active field with true  value"
    LOGGEDUSER_INFO_EMPTY_MSG = "LoggedInUser cannot be empty"
    LOGGEDUSER_SIZE_MSG = "The LoggedInUser must be between 5 and 100 characters"
    LOGGEDUSER_EMPTY = "LoggedInUser attribute not there"
    MGMTSERVER_ID_NULL_MSG = "The MgmtServer ID cannot be null"
    MGMTSERVER_DATA_EMPTY = "The management Data Is Empty"
    MGMTSERVER_NOT_ACTIVE = "The MgmtServerTypeId you are trying to delete does not Active"
    FEILD_VALUE_NOT_VALID = "Field  MgmtServerName should contain Alphanumeric, space, underscore Only"
    FEILD_VALUE_NOT_VALID_DESC = "Field MgmtServerDesc should contain Alphanumeric, space, *, comma, . , parentheses(" \
                                 "), “”, :, ;,’,-,@,& Only "
    FEILD_VALUE_NOT_VALID_REMARKS = "Field MgmtServerRemarks should contain Alphanumeric, space, *, comma, . , " \
                                    "parentheses(), “”, :, ;,’,-,@,& Only "
    MGMTSERVER_FQDN_NOT_EXIST = "No MgmtServerFQDN provided"
    MGMTSERVER_IPADRESS_NOT_EXIST = "No MgmtServerIPAddress provided"
    MGMTSERVER_HOSTNAME_NOT_EXIST = "No MgmtServerHostName provided"
