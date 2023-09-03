# openapi_client.RecieverApi

All URIs are relative to *https://api.profcomff.com/achievement*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reciever_achievement_achievement_id_reciever_user_id_post**](RecieverApi.md#create_reciever_achievement_achievement_id_reciever_user_id_post) | **POST** /achievement/{achievement_id}/reciever/{user_id} | Create Reciever
[**get_all_recievers_achievement_achievement_id_reciever_get**](RecieverApi.md#get_all_recievers_achievement_achievement_id_reciever_get) | **GET** /achievement/{achievement_id}/reciever | Get All Recievers
[**revoke_reciever_achievement_achievement_id_reciever_user_id_delete**](RecieverApi.md#revoke_reciever_achievement_achievement_id_reciever_user_id_delete) | **DELETE** /achievement/{achievement_id}/reciever/{user_id} | Revoke Reciever


# **create_reciever_achievement_achievement_id_reciever_user_id_post**
> AchievementApiRoutesRecieverAchievementGet create_reciever_achievement_achievement_id_reciever_user_id_post(achievement_id, user_id)

Create Reciever

Нужны права на: `achievements.achievement.give`

### Example

* Api Key Authentication (token):
```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_reciever_achievement_get import AchievementApiRoutesRecieverAchievementGet
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
    api_instance = openapi_client.RecieverApi(api_client)
    achievement_id = None # object | 
    user_id = None # object | 

    try:
        # Create Reciever
        api_response = api_instance.create_reciever_achievement_achievement_id_reciever_user_id_post(achievement_id, user_id)
        print("The response of RecieverApi->create_reciever_achievement_achievement_id_reciever_user_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecieverApi->create_reciever_achievement_achievement_id_reciever_user_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_id** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | 

### Return type

[**AchievementApiRoutesRecieverAchievementGet**](AchievementApiRoutesRecieverAchievementGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_recievers_achievement_achievement_id_reciever_get**
> AchievementApiRoutesRecieverAchievementGet get_all_recievers_achievement_achievement_id_reciever_get(achievement_id)

Get All Recievers

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_reciever_achievement_get import AchievementApiRoutesRecieverAchievementGet
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
    api_instance = openapi_client.RecieverApi(api_client)
    achievement_id = None # object | 

    try:
        # Get All Recievers
        api_response = api_instance.get_all_recievers_achievement_achievement_id_reciever_get(achievement_id)
        print("The response of RecieverApi->get_all_recievers_achievement_achievement_id_reciever_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecieverApi->get_all_recievers_achievement_achievement_id_reciever_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_id** | [**object**](.md)|  | 

### Return type

[**AchievementApiRoutesRecieverAchievementGet**](AchievementApiRoutesRecieverAchievementGet.md)

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

# **revoke_reciever_achievement_achievement_id_reciever_user_id_delete**
> AchievementApiRoutesRecieverAchievementGet revoke_reciever_achievement_achievement_id_reciever_user_id_delete(achievement_id, user_id)

Revoke Reciever

Нужны права на: `achievements.achievement.revoke`

### Example

* Api Key Authentication (token):
```python
import time
import os
import openapi_client
from openapi_client.models.achievement_api_routes_reciever_achievement_get import AchievementApiRoutesRecieverAchievementGet
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
    api_instance = openapi_client.RecieverApi(api_client)
    achievement_id = None # object | 
    user_id = None # object | 

    try:
        # Revoke Reciever
        api_response = api_instance.revoke_reciever_achievement_achievement_id_reciever_user_id_delete(achievement_id, user_id)
        print("The response of RecieverApi->revoke_reciever_achievement_achievement_id_reciever_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecieverApi->revoke_reciever_achievement_achievement_id_reciever_user_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_id** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | 

### Return type

[**AchievementApiRoutesRecieverAchievementGet**](AchievementApiRoutesRecieverAchievementGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

