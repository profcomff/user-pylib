# openapi_client.AchievementApi

All URIs are relative to *https://api.profcomff.com/achievement*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_achievement_achievement_post**](AchievementApi.md#create_achievement_achievement_post) | **POST** /achievement | Create Achievement
[**edit_achievement_achievement_id_patch**](AchievementApi.md#edit_achievement_achievement_id_patch) | **PATCH** /achievement/{id} | Edit Achievement
[**get_achievement_achievement_id_get**](AchievementApi.md#get_achievement_achievement_id_get) | **GET** /achievement/{id} | Get Achievement
[**get_all_achievements_achievement_get**](AchievementApi.md#get_all_achievements_achievement_get) | **GET** /achievement | Get All Achievements
[**upload_picture_achievement_id_picture_patch**](AchievementApi.md#upload_picture_achievement_id_picture_patch) | **PATCH** /achievement/{id}/picture | Upload Picture


# **create_achievement_achievement_post**
> AchievementApiRoutesAchievementAchievementGet create_achievement_achievement_post(achievement_create)

Create Achievement

Нужны права на: `achievements.achievement.create`

### Example

* Api Key Authentication (token):
```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_achievement_achievement_get import AchievementApiRoutesAchievementAchievementGet
from openapi_client.models.achievement_create import AchievementCreate
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
    except Exception as e:
        print("Exception when calling AchievementApi->create_achievement_achievement_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_create** | [**AchievementCreate**](AchievementCreate.md)|  | 

### Return type

[**AchievementApiRoutesAchievementAchievementGet**](AchievementApiRoutesAchievementAchievementGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_achievement_achievement_id_patch**
> AchievementApiRoutesAchievementAchievementGet edit_achievement_achievement_id_patch(id, achievement_edit)

Edit Achievement

Нужны права на: `achievements.achievement.edit`

### Example

* Api Key Authentication (token):
```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_achievement_achievement_get import AchievementApiRoutesAchievementAchievementGet
from openapi_client.models.achievement_edit import AchievementEdit
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
    id = None # object | 
    achievement_edit = openapi_client.AchievementEdit() # AchievementEdit | 

    try:
        # Edit Achievement
        api_response = api_instance.edit_achievement_achievement_id_patch(id, achievement_edit)
        print("The response of AchievementApi->edit_achievement_achievement_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchievementApi->edit_achievement_achievement_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **achievement_edit** | [**AchievementEdit**](AchievementEdit.md)|  | 

### Return type

[**AchievementApiRoutesAchievementAchievementGet**](AchievementApiRoutesAchievementAchievementGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement_achievement_id_get**
> AchievementApiRoutesAchievementAchievementGet get_achievement_achievement_id_get(id)

Get Achievement

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_achievement_achievement_get import AchievementApiRoutesAchievementAchievementGet
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.profcomff.com/achievement
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.profcomff.com/achievement"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AchievementApi(api_client)
    id = None # object | 

    try:
        # Get Achievement
        api_response = api_instance.get_achievement_achievement_id_get(id)
        print("The response of AchievementApi->get_achievement_achievement_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchievementApi->get_achievement_achievement_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**AchievementApiRoutesAchievementAchievementGet**](AchievementApiRoutesAchievementAchievementGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_achievements_achievement_get**
> object get_all_achievements_achievement_get()

Get All Achievements

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.profcomff.com/achievement
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.profcomff.com/achievement"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AchievementApi(api_client)

    try:
        # Get All Achievements
        api_response = api_instance.get_all_achievements_achievement_get()
        print("The response of AchievementApi->get_all_achievements_achievement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchievementApi->get_all_achievements_achievement_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_picture_achievement_id_picture_patch**
> AchievementApiRoutesAchievementAchievementGet upload_picture_achievement_id_picture_patch(id, picture_file)

Upload Picture

### Example

* Api Key Authentication (token):
```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_achievement_achievement_get import AchievementApiRoutesAchievementAchievementGet
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
    id = None # object | 
    picture_file = None # object | 

    try:
        # Upload Picture
        api_response = api_instance.upload_picture_achievement_id_picture_patch(id, picture_file)
        print("The response of AchievementApi->upload_picture_achievement_id_picture_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchievementApi->upload_picture_achievement_id_picture_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **picture_file** | [**object**](object.md)|  | 

### Return type

[**AchievementApiRoutesAchievementAchievementGet**](AchievementApiRoutesAchievementAchievementGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

