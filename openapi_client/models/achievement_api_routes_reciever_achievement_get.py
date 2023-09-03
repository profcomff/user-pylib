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

class AchievementApiRoutesRecieverAchievementGet(BaseModel):
    """
    AchievementApiRoutesRecieverAchievementGet
    """
    id: Optional[Any] = Field(...)
    name: Optional[Any] = Field(...)
    description: Optional[Any] = Field(...)
    picture: Optional[Any] = Field(...)
    owner_user_id: Optional[Any] = Field(...)
    recievers: Optional[Any] = Field(...)
    __properties = ["id", "name", "description", "picture", "owner_user_id", "recievers"]

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
    def from_json(cls, json_str: str) -> AchievementApiRoutesRecieverAchievementGet:
        """Create an instance of AchievementApiRoutesRecieverAchievementGet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if picture (nullable) is None
        # and __fields_set__ contains the field
        if self.picture is None and "picture" in self.__fields_set__:
            _dict['picture'] = None

        # set to None if owner_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.owner_user_id is None and "owner_user_id" in self.__fields_set__:
            _dict['owner_user_id'] = None

        # set to None if recievers (nullable) is None
        # and __fields_set__ contains the field
        if self.recievers is None and "recievers" in self.__fields_set__:
            _dict['recievers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AchievementApiRoutesRecieverAchievementGet:
        """Create an instance of AchievementApiRoutesRecieverAchievementGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AchievementApiRoutesRecieverAchievementGet.parse_obj(obj)

        _obj = AchievementApiRoutesRecieverAchievementGet.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "picture": obj.get("picture"),
            "owner_user_id": obj.get("owner_user_id"),
            "recievers": obj.get("recievers")
        })
        return _obj

