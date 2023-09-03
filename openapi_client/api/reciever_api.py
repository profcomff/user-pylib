# coding: utf-8

"""
    АПИ достижений

    Программный интерфейс ачивок для Твой ФФ!

    The version of the OpenAPI document: v2023.08.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from typing import Any

from openapi_client.models.achievement_api_routes_reciever_achievement_get import AchievementApiRoutesRecieverAchievementGet

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RecieverApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_reciever_achievement_achievement_id_reciever_user_id_post(self, achievement_id : Any, user_id : Any, **kwargs) -> AchievementApiRoutesRecieverAchievementGet:  # noqa: E501
        """Create Reciever  # noqa: E501

        Нужны права на: `achievements.achievement.give`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_reciever_achievement_achievement_id_reciever_user_id_post(achievement_id, user_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param user_id: (required)
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AchievementApiRoutesRecieverAchievementGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_reciever_achievement_achievement_id_reciever_user_id_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_reciever_achievement_achievement_id_reciever_user_id_post_with_http_info(achievement_id, user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def create_reciever_achievement_achievement_id_reciever_user_id_post_with_http_info(self, achievement_id : Any, user_id : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Reciever  # noqa: E501

        Нужны права на: `achievements.achievement.give`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_reciever_achievement_achievement_id_reciever_user_id_post_with_http_info(achievement_id, user_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param user_id: (required)
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AchievementApiRoutesRecieverAchievementGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'achievement_id',
            'user_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_reciever_achievement_achievement_id_reciever_user_id_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['achievement_id']:
            _path_params['achievement_id'] = _params['achievement_id']

        if _params['user_id']:
            _path_params['user_id'] = _params['user_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "AchievementApiRoutesRecieverAchievementGet",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/achievement/{achievement_id}/reciever/{user_id}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_all_recievers_achievement_achievement_id_reciever_get(self, achievement_id : Any, **kwargs) -> AchievementApiRoutesRecieverAchievementGet:  # noqa: E501
        """Get All Recievers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_recievers_achievement_achievement_id_reciever_get(achievement_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AchievementApiRoutesRecieverAchievementGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_all_recievers_achievement_achievement_id_reciever_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_all_recievers_achievement_achievement_id_reciever_get_with_http_info(achievement_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_all_recievers_achievement_achievement_id_reciever_get_with_http_info(self, achievement_id : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Get All Recievers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_recievers_achievement_achievement_id_reciever_get_with_http_info(achievement_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AchievementApiRoutesRecieverAchievementGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'achievement_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_recievers_achievement_achievement_id_reciever_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['achievement_id']:
            _path_params['achievement_id'] = _params['achievement_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AchievementApiRoutesRecieverAchievementGet",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/achievement/{achievement_id}/reciever', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def revoke_reciever_achievement_achievement_id_reciever_user_id_delete(self, achievement_id : Any, user_id : Any, **kwargs) -> AchievementApiRoutesRecieverAchievementGet:  # noqa: E501
        """Revoke Reciever  # noqa: E501

        Нужны права на: `achievements.achievement.revoke`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revoke_reciever_achievement_achievement_id_reciever_user_id_delete(achievement_id, user_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param user_id: (required)
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AchievementApiRoutesRecieverAchievementGet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the revoke_reciever_achievement_achievement_id_reciever_user_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.revoke_reciever_achievement_achievement_id_reciever_user_id_delete_with_http_info(achievement_id, user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def revoke_reciever_achievement_achievement_id_reciever_user_id_delete_with_http_info(self, achievement_id : Any, user_id : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Revoke Reciever  # noqa: E501

        Нужны права на: `achievements.achievement.revoke`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revoke_reciever_achievement_achievement_id_reciever_user_id_delete_with_http_info(achievement_id, user_id, async_req=True)
        >>> result = thread.get()

        :param achievement_id: (required)
        :type achievement_id: object
        :param user_id: (required)
        :type user_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AchievementApiRoutesRecieverAchievementGet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'achievement_id',
            'user_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_reciever_achievement_achievement_id_reciever_user_id_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['achievement_id']:
            _path_params['achievement_id'] = _params['achievement_id']

        if _params['user_id']:
            _path_params['user_id'] = _params['user_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "AchievementApiRoutesRecieverAchievementGet",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/achievement/{achievement_id}/reciever/{user_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))