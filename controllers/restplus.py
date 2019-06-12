import logging
import traceback

from flask_restplus import Api

log = logging.getLogger(__name__)


api = Api(version='1.0', title='StartUp API',
          description='A simple API for start up')

@api.errorhandler
def default_error_handler(e):
   message = 'An unhandled exception occurred.'
   log.exception(message)

@api.errorhandler
def name_error_handler(e):
   message = 'An exception occurred in name data expected.'
   log.exception(message)

@api.errorhandler
def firstname_error_handler(e):
   message = 'An exception occurred in firstname data expected.'
   log.exception(message)

@api.errorhandler
def role_error_handler(e):
   message = 'An exception occurred in role data expected.'
   log.exception(message)

@api.errorhandler
def birthdate_error_handler(e):
   message = 'An exception occurred in name birthdate data expected.'
   log.exception(message)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)