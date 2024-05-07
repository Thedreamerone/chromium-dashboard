from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.link_preview_open_graph_all_of_information import LinkPreviewOpenGraphAllOfInformation
from chromestatus_openapi import util

from chromestatus_openapi.models.link_preview_open_graph_all_of_information import LinkPreviewOpenGraphAllOfInformation  # noqa: E501

class LinkPreviewWebkitBug(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, type=None, information=None, http_error_code=None):  # noqa: E501
        """LinkPreviewWebkitBug - a model defined in OpenAPI

        :param url: The url of this LinkPreviewWebkitBug.  # noqa: E501
        :type url: str
        :param type: The type of this LinkPreviewWebkitBug.  # noqa: E501
        :type type: str
        :param information: The information of this LinkPreviewWebkitBug.  # noqa: E501
        :type information: LinkPreviewOpenGraphAllOfInformation
        :param http_error_code: The http_error_code of this LinkPreviewWebkitBug.  # noqa: E501
        :type http_error_code: int
        """
        self.openapi_types = {
            'url': str,
            'type': str,
            'information': LinkPreviewOpenGraphAllOfInformation,
            'http_error_code': int
        }

        self.attribute_map = {
            'url': 'url',
            'type': 'type',
            'information': 'information',
            'http_error_code': 'http_error_code'
        }

        self._url = url
        self._type = type
        self._information = information
        self._http_error_code = http_error_code

    @classmethod
    def from_dict(cls, dikt) -> 'LinkPreviewWebkitBug':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinkPreviewWebkitBug of this LinkPreviewWebkitBug.  # noqa: E501
        :rtype: LinkPreviewWebkitBug
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this LinkPreviewWebkitBug.


        :return: The url of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this LinkPreviewWebkitBug.


        :param url: The url of this LinkPreviewWebkitBug.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def type(self) -> str:
        """Gets the type of this LinkPreviewWebkitBug.


        :return: The type of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this LinkPreviewWebkitBug.


        :param type: The type of this LinkPreviewWebkitBug.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def information(self) -> LinkPreviewOpenGraphAllOfInformation:
        """Gets the information of this LinkPreviewWebkitBug.


        :return: The information of this LinkPreviewWebkitBug.
        :rtype: LinkPreviewOpenGraphAllOfInformation
        """
        return self._information

    @information.setter
    def information(self, information: LinkPreviewOpenGraphAllOfInformation):
        """Sets the information of this LinkPreviewWebkitBug.


        :param information: The information of this LinkPreviewWebkitBug.
        :type information: LinkPreviewOpenGraphAllOfInformation
        """
        if information is None:
            raise ValueError("Invalid value for `information`, must not be `None`")  # noqa: E501

        self._information = information

    @property
    def http_error_code(self) -> int:
        """Gets the http_error_code of this LinkPreviewWebkitBug.


        :return: The http_error_code of this LinkPreviewWebkitBug.
        :rtype: int
        """
        return self._http_error_code

    @http_error_code.setter
    def http_error_code(self, http_error_code: int):
        """Sets the http_error_code of this LinkPreviewWebkitBug.


        :param http_error_code: The http_error_code of this LinkPreviewWebkitBug.
        :type http_error_code: int
        """
        if http_error_code is None:
            raise ValueError("Invalid value for `http_error_code`, must not be `None`")  # noqa: E501

        self._http_error_code = http_error_code
