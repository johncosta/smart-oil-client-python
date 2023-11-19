## Smart Oil Gauge Python Client

[Smart Oil Gauge](https://www.smartoilgauge.com/) is a product used to monitor
oil levels in oil tanks.  Data is sent to <https://www.dropletfuel.com/>
systems. While this site intended for oil distributors and, for a small fee,
the data can be retrieved via an API.

The purpose of this repository is to document the process of connecting to this
API and provide a python based client for convienient access.

### Initial Setup

What worked for me was to email the request for API access to
`support@smartoilgauge.com`. THe support team will provide concise instructions
on how to get setup in the <https://www.dropletfuel.com/> portal.

After setting up a faux "brand" in the <https://www.dropletfuel.com/> portal
and adding credit card on file for the monthly fee, client credentials can then
be retrieved.

Connecting the Sensors to the "brand" requires a final step from support and then
the api will be available for use.

### Unofficial API Documentation

All api calls should be made to the following base url: <https://api.dropletfuel.com>

#### Retrieve token via [OAuth 2.0 Client Credentials](https://oauth.net/2/grant-types/client-credentials/) grant type.

##### POST /token.php (given appropriate credentials, a token is returned)

###### Request Headers

| name         | type     | data type | description                                                                                                                                                                |
|--------------|----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User-Agent   | required | string    | User-Agent is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent. |
| Content-Type | required | string    | Content-Type is a representation header is used to indicate the original media type of the resource.                                                                       |

**_NOTE:_** User-Agent is usually an optional header, but it's been noted that a 406 Not Acceptable response is returned when absent.
**_NOTE:_** Content-Type should be set to `application/x-www-form-urlencoded` for the token request.

###### Request Parameters

> | name         | type     | data type | description                       |
> |--------------|----------|-----------|-----------------------------------|
> | grant_type   | required | string    | Set this to "client_credentials". |
> | client_id    | required | string    | Your application's Client ID.     |
> | grant_type   | required | string    | Your application's Client Secret. |


###### Responses

> | http code | content-type                    | response                                                                                         |
> |-----------|---------------------------------|--------------------------------------------------------------------------------------------------|
> | `200`     | `application/json`              | `{"access_token":"eyJz93a...k4laUWw", "token_type":"Bearer", "expires_in":3600, "scope": null}`  |
> | `400`     | `application/json`              | `{"error":"invalid_client","error_description":"The client credentials are invalid"}`            |
> | `406`     | `text/html; charset=iso-8859-1` | 406 Not Acceptable                                                                               |

###### Example cURL

```shell
curl --request POST \
--url 'https://api.dropletfuel.com/token' \
--header 'content-type: application/x-www-form-urlencoded' \
--header 'User-Agent: ' \
--data grant_type=client_credentials \
--data client_id=YOUR_CLIENT_ID \
--data client_secret=YOUR_CLIENT_SECRET
```

#### Retrieve Tank Data

**_NOTE:_** It seems that this endpoint may only return the last data result from the tank.


##### GET /auto/get_tank_data.php

###### Request Headers

| name         | type     | data type | description                                                                                                                                                                |
|--------------|----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User-Agent   | required | string    | User-Agent is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent. |
| Content-Type | required | string    | Content-Type is a representation header is used to indicate the original media type of the resource.                                                                       |

**_NOTE:_** User-Agent is usually an optional header, but it's been noted that a 406 Not Acceptable response is returned when absent.

**_NOTE:_** Content-Type should be set to `application/x-www-form-urlencoded` for the token request.


###### Request Parameters

> | name        | type     | data type | description                                    |
> |-------------|----------|-----------|------------------------------------------------|
> | start_index | required | string    | Starting index for results returned.           |
> | max_results | required | string    | Maximum number of results returned in the API. |


###### Responses

> | http code | content-type                    | response                                                                                                                                                                                                                                                                                                                                                                            |
> |-----------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
> | `200`     | `application/json`              | `{"result":"ok","start_index":"0","max_results":"1000","data":[{"acct_num":"ABC1234","tank_num":"1","gallons":"307.74","tank_volume":"660","sensor_id":"1123456789","last_read":"2023-09-07 08:25:17","battery":"Good"},{"acct_num":"ABC1234","tank_num":"1","gallons":"178.72","tank_volume":"660","sensor_id":"1123456789","last_read":"2023-09-07 08:39:58","battery":"Good"}]}` |
> | `401`     | `application/json`              | `{"error":"expired_token","error_description":"The access token provided is invalid"}`                                                                                                                                                                                                                                                                                              |
> | `406`     | `text/html; charset=iso-8859-1` | 406 Not Acceptable                                                                                                                                                                                                                                                                                                                                                                  |


###### Example cURL

```shell
curl --request GET \
--url 'https://api.dropletfuel.com/auto/get_tank_data.php' \
--header 'User-Agent: ' \
--header 'Content-Type: application/json'
--header 'Authorization: Bearer <token>'
```
