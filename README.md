# openapi-client
Программный интерфейс ачивок для Твой ФФ!

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2023.08.18
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.profcomff.com/achievement
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.profcomff.com/achievement"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AchievementApi(api_client)
    achievement_create = openapi_client.AchievementCreate() # AchievementCreate | 

    try:
        # Create Achievement
        api_response = api_instance.create_achievement_achievement_post(achievement_create)
        print("The response of AchievementApi->create_achievement_achievement_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AchievementApi->create_achievement_achievement_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.profcomff.com/achievement*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AchievementApi* | [**create_achievement_achievement_post**](docs/AchievementApi.md#create_achievement_achievement_post) | **POST** /achievement | Create Achievement
*AchievementApi* | [**edit_achievement_achievement_id_patch**](docs/AchievementApi.md#edit_achievement_achievement_id_patch) | **PATCH** /achievement/{id} | Edit Achievement
*AchievementApi* | [**get_achievement_achievement_id_get**](docs/AchievementApi.md#get_achievement_achievement_id_get) | **GET** /achievement/{id} | Get Achievement
*AchievementApi* | [**get_all_achievements_achievement_get**](docs/AchievementApi.md#get_all_achievements_achievement_get) | **GET** /achievement | Get All Achievements
*AchievementApi* | [**upload_picture_achievement_id_picture_patch**](docs/AchievementApi.md#upload_picture_achievement_id_picture_patch) | **PATCH** /achievement/{id}/picture | Upload Picture
*RecieverApi* | [**create_reciever_achievement_achievement_id_reciever_user_id_post**](docs/RecieverApi.md#create_reciever_achievement_achievement_id_reciever_user_id_post) | **POST** /achievement/{achievement_id}/reciever/{user_id} | Create Reciever
*RecieverApi* | [**get_all_recievers_achievement_achievement_id_reciever_get**](docs/RecieverApi.md#get_all_recievers_achievement_achievement_id_reciever_get) | **GET** /achievement/{achievement_id}/reciever | Get All Recievers
*RecieverApi* | [**revoke_reciever_achievement_achievement_id_reciever_user_id_delete**](docs/RecieverApi.md#revoke_reciever_achievement_achievement_id_reciever_user_id_delete) | **DELETE** /achievement/{achievement_id}/reciever/{user_id} | Revoke Reciever


## Documentation For Models

 - [AchievementApiRoutesAchievementAchievementGet](docs/AchievementApiRoutesAchievementAchievementGet.md)
 - [AchievementApiRoutesRecieverAchievementGet](docs/AchievementApiRoutesRecieverAchievementGet.md)
 - [AchievementCreate](docs/AchievementCreate.md)
 - [AchievementEdit](docs/AchievementEdit.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [RecieverGet](docs/RecieverGet.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="token"></a>
### token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



