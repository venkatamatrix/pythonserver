"""/src/config.py"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Development(object):  # pylint: disable=too-few-public-methods
    """Development environment configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):  # pylint: disable=too-few-public-methods
    """
    Production environment configurations
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Testing(object):  # pylint: disable=too-few-public-methods
    """Development environment configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'env1': Development,
    'prod': Production,
    'env3': Testing
}

