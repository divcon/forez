from request_form import api_request
#notebook test : True
#Server test : False
host = True
#host = False


#login
#url = "/tokens"
#body = {'username': 'sungjin', 'password': 'rkems'}
#method = 'POST'


#test3
token3 = 'Token 824669b77dc525181683afb005ee6177e3d5ec4b'
server_token3 = 'Token 230ff9bca92ce27d30b2eeac0d245906716eb933'
#test
token1 = 'Token c1c98cc1faee9c20ccca8057817e2b60612c9b45'
server_token1 = 'Token cfb665f106bd9f9da512592199afe032ed0723b2'
#test2
token2 = 'Token e918bfc2810a5dcd5704a019d75ed941f4ccf0e1'
server_token2 = 'Token 7ecb11dddef8b6a97897e4498e677b9d9aa76d45'
#app registering
url = "/clients"
header = {'Authorization': token3}
body = {'name': 'test4', 'url': 'http://211.189.127.73:8000',
        'redirect_uri': 'http://211.189.127.73:8000',
        'client_type': 'confidential',
        'authorization_grant_type': 'authorization-code'}
method = "POST"

#app list 
#url = "/clients/testapp1"
#body = None
#header = {'Authorization': token1}
#method = "GET"

#modify url
#url = "/clients/testapp1"
#body = {"url": "http://123.123.123.12:8000", "redirect_uri": "http://123.123.123.12:8000"}
#header = {'Authorization': token1}
#method = "PUT"

#app delete
#url = "/clients/testuser1213"
#header = {'Authorization': 'Token 3a327baddb77b0a0c86bb23c4dd321a3a547b987'}
#method = "DELETE"

#team list
#url = "/teams"
#header = {'Authorization': token}
#body = None
#method = "GET"
#token = 'Token 9a8cf47d1c67f42370d2087a52e7f0939d590119'

#add member
url = "/teams/testapp1/members"
header = {'Authorization': server_token1}
body = {'member': 'test3'}
method = "POST"

#team info
#url = "/teams/test3/members"
#header = {'Authorization': token}
#body = None
#method = "GET"

#post client details
#url = "/clients/testapp1/details"
#header = {'Authorization': server_token1}
#body = {'tag1': 'sample1', 'tag2': 'sample112', 'tag3': 'sample3', 'category': 'business',
#        'short_description': 'short des', 'long_description': 'long des',
#        'permission_explanation': 'ex', 'publish': 'False'}
#method = "POST"

#get client details
#url = "/clients/testapp1/details"
#header = {'Authorization': server_token1}
#body = None
#method = "GET"

#post client setting
url = "/clients/testapp2/setting"
header = {'Authorization': token3}
body = {'display_name': 'setting_test', 'contact_email': 'test4@naver.com', 'publish': 'True'}
method = "POST"

#get client setting
#url = "/clients/testapp2/setting"
#header = {'Authorization': token3}
#body = None
#method = "GET"

#get access token
#url = "/oauth2/access_token/"
#body = {"cleint_id": "63d2649aa23afb7c0653", "client_secret": "71920cd8d88815c94a555bd60f9e1e5d0dc464a2",
#        "grant_type": "a6b7192a5a1e169ec636130ba607bffcab3a86eb", "username": "test1", "password": "test"}
#header = None
#method = "POST"
#"client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=password&username=YOUR_USERNAME&password=YOUR_PASSWORD" http://localhost:8000/oauth2/access_token/
#
#get store list
url = "/stores"
body = None
header = {'Authorization': token3}
method = "GET"

# get app list by category
#url = "/stores?category=business"
#body = None
#header = {'Authorization': token3}
#method = "GET"

# get app info 
#url = "/stores/testapp1"
#body = None
#header = {'Authorization': token3}
#method = "GET"

# get authorizateion
#url = "/o/authorize?response_type=code&client_id=lTQYwlqn;..HW1TVSDFMJnRtx!vunZ-MB?6py??M&state=xyz&scope=read&redirect_uri=http://211.189.127.73:8000"
#GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
#body = None
#header = {'Authorization': token3}
#method = "GET"


test = api_request(host)
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
print resp
print content
