#!/usr/bin/python
import yaml
from os.path import expanduser


import objc
import requests
import json

def set_status():
	"""
	Reads a YML file named .slack_wifi_status.yml in the home directory of the user, and sets
	the slack status text and emoji according to the ssid entry in the yml file.  Example:
	---
	slack:
	  interface: en0
	  token: <oauth token from slack app>
	  url: https://slack.com/api/users.profile.set  
	  <commuting ssid name>:
	    status: On a Bus
	    icon: ":bus:"
	  <office ssid name>:
	    status: "In Office"
	    icon: ":office:"
	  <home ssid name>:
	    status: "WFH"
	    icon: ":house:"
	  Default:
	    status: ""
	    icon: ""
	...
	"""
	objc.loadBundle('CoreWLAN',
	                bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
	                module_globals=globals())

	home = expanduser("~")

	f = open('%s/.slack_wifi_status.yml' % home)
	config = yaml.safe_load(f)['slack']
	f.close()

	interfaceName = config['interface']
	en = CWInterface.interfaceWithName_(interfaceName)

	ssidConfig = config['Default']
	if en:
		ssid = en.ssid()
		if config[ssid]:
			ssidConfig = config[ssid]


	profile={"status_text":ssidConfig['status'],"status_emoji":ssidConfig['icon']}
	js = json.dumps(profile)
	data = {"token":config['token'], "profile":js}

	response = requests.post(config['url'], data=data)

set_status()
#print(response.content)
