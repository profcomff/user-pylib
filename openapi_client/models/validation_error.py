# coding: utf-8

"""
    АПИ достижений

    Программный интерфейс ачивок для Твой ФФ!

    The version of the OpenAPI document: v2023.08.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class ValidationError(BaseModel):
    """
    ValidationError
    """
    loc: Optional[Any] = Field(...)
    msg: Optional[Any] = Field(...)
    type: Optional[Any] = Field(...)
    __properties = ["loc", "msg", "type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ValidationError:
        """Create an instance of ValidationError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if loc (nullable) is None
        # and __fields_set__ contains the field
        if self.loc is None and "loc" in self.__fields_set__:
            _dict['loc'] = None

        # set to None if msg (nullable) is None
        # and __fields_set__ contains the field
        if self.msg is None and "msg" in self.__fields_set__:
            _dict['msg'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationError:
        """Create an instance of ValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationError.parse_obj(obj)

        _obj = ValidationError.parse_obj({
            "loc": obj.get("loc"),
            "msg": obj.get("msg"),
            "type": obj.get("type")
        })
        return _obj

