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
and adding credit card on file for the monthly fee, client credetials can then
be retrieved.

Connecting the Sensors to the "brand" requires a final step from support and then
the api will be available for use.

### API Documentation

All api calls should be made to the following base url: <https://api.dropletfuel.com>

#### Retrieve token via [OAuth 2.0 Client Credentials](https://oauth.net/2/grant-types/client-credentials/) grant type.

<details>
 <summary><code>POST</code> <code><b>/token.php</b></code> <code>(given appropriate credentials, a token is returned)</code></summary>

##### Request Headers

> | name         | type     | data type | description                                                                                                                                                                |
> |--------------|----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
> | User-Agent   | required | string    | User-Agent is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent. |
> | Content-Type | required | string    | Content-Type is a representation header is used to indicate the original media type of the resource.                                                                       |

> **_NOTE:_** User-Agent is usually an optional header, but it's been noted that a 406 Not Acceptable response is returned when absent. 

> **_NOTE:_** Content-Type should be set to `application/x-www-form-urlencoded` for the token request.

##### Request Parameters

> | name         | type     | data type | description                       |
> |--------------|----------|-----------|-----------------------------------|
> | grant_type   | required | string    | Set this to "client_credentials". |
> | client_id    | required | string    | Your application's Client ID.     |
> | grant_type   | required | string    | Your application's Client Secret. |


##### Responses

> | http code | content-type                    | response                                                                                         |
> |-----------|---------------------------------|--------------------------------------------------------------------------------------------------|
> | `200`     | `application/json`              | `{"access_token":"eyJz93a...k4laUWw", "token_type":"Bearer", "expires_in":3600, "scope": null}`  |
> | `400`     | `application/json`              | `{"error":"invalid_client","error_description":"The client credentials are invalid"}`            |
> | `406`     | `text/html; charset=iso-8859-1` | 406 Not Acceptable                                                                               |

##### Example cURL

> ```shell
>  curl --request POST \
> --url 'https://api.dropletfuel.com/token' \
> --header 'content-type: application/x-www-form-urlencoded' \
> --data grant_type=client_credentials \
> --data client_id=YOUR_CLIENT_ID \
> --data client_secret=YOUR_CLIENT_SECRET
> ```

</details>