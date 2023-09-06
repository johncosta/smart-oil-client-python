## Smart Oil Gauge Python Client

[Smart Oil Gauge](https://www.smartoilgauge.com/) is a product used to monitor 
oil levels in oil tanks.  Data is sent to <https://www.dropletfuel.com/> 
systems. While this site intended for oil distributors and, for a small fee, 
the data can be retrieved via an API.

The purpose of this repository is to document the process of connecting to this
API and provide a python based client for use to access the api.

### Initial Setup

What worked for me was to email the request for API access to 
`support@smartoilgauge.com`. THe support team will provide concise instructions
on how to get setup in the <https://www.dropletfuel.com/> portal. 

After setting up a faux "brand" in the <https://www.dropletfuel.com/> portal 
and adding credit card on file for the monthly fee, client credetials can then
be retrieved.

Connecting the Sensors to the "brand" requires a final step from support and then
the api will be available for use.
