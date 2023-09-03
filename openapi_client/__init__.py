# coding: utf-8

# flake8: noqa

"""
    АПИ достижений

    Программный интерфейс ачивок для Твой ФФ!

    The version of the OpenAPI document: v2023.08.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.achievement_api import AchievementApi
from openapi_client.api.reciever_api import RecieverApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.achievement_api_routes_achievement_achievement_get import AchievementApiRoutesAchievementAchievementGet
from openapi_client.models.achievement_api_routes_reciever_achievement_get import AchievementApiRoutesRecieverAchievementGet
from openapi_client.models.achievement_create import AchievementCreate
from openapi_client.models.achievement_edit import AchievementEdit
from openapi_client.models.http_validation_error import HTTPValidationError
from openapi_client.models.reciever_get import RecieverGet
from openapi_client.models.validation_error import ValidationError