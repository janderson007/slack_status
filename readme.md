Slack Status
------------

Sets your Slack status based on your Wifi SSID on OSX


Configuration
-------------

First, you need to create a new Slack App.  Follow the instructions here: https://api.slack.com/. to create a new 
app for your team, and authorize it for `users.profile:write`.  You will recieve an auth token.


Then create a YML file in your home directory to tell slack_status how to authorize, 
---
slack:
  # The network interface to use to look up the SSID that is currently in use
  interface: en0
  # The OAuth2 token provided by Slack
  token: <oauth token from slack app>
  # URL for Slack profile API
  url: https://slack.com/api/users.profile.set  

  # An example SSID name, configured with status text and icon
  Bus WIFI:
    status: On a Bus
    icon: ":bus:"    
  # An example SSID name, configured with status text and icon
  Employees:
    status: "In Office"
    icon: ":office:"
  # An example home SSID name, configured with status text and icon:
  XFinity:
    status: "WFH"
    icon: ":house:"
  Default:
    status: ""
    icon: ""
...

