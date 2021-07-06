# This python script will mimic the basic functionality of conn class
# NOTE: Not all the validations made in conn class are handled here. We are just bypassing SSL verification
#
# Make sure the python requests module is installed before running this script
# `pip install requests`

#import requests

# OV details
apiVersion = 1800  # provide the api version
ov_hostname = "x.x.x.x"
ov_username = "<ov_admin>"
ov_password = "<ov_password>"

status_codes = [200, 201, 202] # success status codes

default_headers = {
					'X-API-Version': str(apiVersion),
					'Accept': 'application/json',
					'Content-Type': 'application/json'
					}

# URIs
login_uri = '/rest/login-sessions'

# Base method to do http requests
def do_http(method, uri, body={}, headers=default_headers, ssl_verify=False):
	url = 'https://' + str(ov_hostname) + str(uri)
	response = requests.method(url, data=body, headers=headers, verify=ssl_verify)	
	return response

def login(username, password, headers=default_headers):
	body = {
			'userName': username,
			'password': password,
			'loginMsgAck': True
			}
	
	resp = do_http("post", login_uri, body)
	if resp.get('status_code') in status_codes and resp.get('content'):
		sessionID = resp['content']['sessionID']
		default_headers.update(auth=sessionID)
		return sessionID
	else:
		print("OV login failed")


# LOGIN OV
login(ov_username, ov_password)

# GET call
cert_output = do_http("get", '/rest/certificates/ca')
if cert_output.get('status_code') in status_codes and cert_output.get('content'):
	print(cert_output['content'])
