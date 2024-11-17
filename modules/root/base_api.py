import json
from json import JSONDecodeError
import requests

from modules.dataclass_collection import ApiResponse


class BaseApi:

    def __init__(self):
        """
        Initializing Base Api object
        """
        self.__session = requests.Session()

    def clear_cookies(self):
        """
        Method to clear rest session cookies inside BaseApi object
        """
        self.__session.cookies.clear()

    def __send_request(self,
                       method: str,
                       url: str,
                       **kwargs) -> ApiResponse:
        """
        Basic method for sending request

        :param method: HTTP method
        :param url: URL where request is to be sent
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """

        response = self.__session.request(method=method,
                                          url=url,
                                          **kwargs)

        # Prepare needed response attributes to build own Response object
        resp_status_code = response.status_code
        resp_body = response.text
        try:
            resp_json = response.json()
        except JSONDecodeError:
            resp_json = None
        resp = ApiResponse(status_code=resp_status_code,
                           body=resp_body,
                           json=resp_json)

        return resp

    def get(self,
            url: str,
            params: dict = None,
            **kwargs) -> ApiResponse:
        """
         GET request

        :param url: URL where request is to be sent
        :param params: request query parameters
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """
        return self.__send_request(method="GET",
                                   url=url,
                                   params=params,
                                   **kwargs)

    def post(self,
             url: str,
             body: dict = None,
             **kwargs) -> ApiResponse:
        """
        POST request

        :param url: URL where request is to be sent
        :param body: request body
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """
        return self.__send_request(method="POST",
                                   url=url,
                                   json=body,
                                   **kwargs)

    def patch(self,
              url: str,
              body: dict = None,
              data: dict = None,
              **kwargs) -> ApiResponse:
        """
        PATCH request

        :param url: URL where request is to be sent
        :param body: Request body
        :param data: Request data (payload)
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """
        return self.__send_request(method="PATCH",
                                   url=url,
                                   json=body,
                                   data=data,
                                   **kwargs)

    def delete(self,
               url: str,
               body: dict = None,
               data: dict = None,
               **kwargs) -> ApiResponse:
        """
        DELETE request

        :param url: URL where request is to be sent
        :param body: Request body
        :param data: Request data (payload)
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """
        return self.__send_request(method="DELETE",
                                   url=url,
                                   json=body,
                                   data=data,
                                   **kwargs)

    def put(self,
            url: str,
            body: dict = None,
            data: dict = None,
            **kwargs) -> ApiResponse:
        """
        PUT request

        :param url: URL where request is to be sent
        :param body: Request body
        :param data: Request data (payload)
        :param kwargs: Additional arguments (body, payload etc)
        :return: Response object with status_code (int), body (str) and json (dict or None, if not in JSON format)
        """
        return self.__send_request(method="PUT",
                                   url=url,
                                   json=body,
                                   data=data,
                                   **kwargs)
