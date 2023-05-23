"""
This module contains expected results from base API call.
"""


class BaseRequestResultsExpected:
    """Class for Base Request expected results."""
    STATUS_CODE = 200
    STATUS_CODE_NOT_FOUND = 404
    STATUS_CODE_CREATED = 201
    SUPPORT_URL = 'https://reqres.in/#support-heading'
    SUPPORT_TEXT = 'To keep ReqRes free, contributions towards server costs are appreciated!'
