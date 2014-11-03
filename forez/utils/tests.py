from request_form import api_request
#notebook test : True
#Server test : False
host = True
#host = False
#join us


#login
#url = "/tokens"
#body = {'username': 'sungjin', 'password': 'rkems'}
#method = 'POST'

#test3
token3 = 'Token 21f79828b4e9960a80a03bcf86e01250e3bff6bf'
#test
token1 = 'Token f97e83013f18f07d56faae62419f6aaaa3ab7845'
#test2
token2 = 'Token 2cef969c8fc4be1ab27568b4db308841a3e28a26'

#app registering
url = "/clients/testapp1"
header = {'Authorization': token3}
body = {'name': 'test4', 'url': 'http://211.189.127.73:8000',
        'redirect_uri': 'http://211.189.127.73:8000', 'client_type': '0'}
method = "POST"

#app list 
url = "/clients/testapp2"
body = None
header = {'Authorization': token3}
method = "GET"

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
#url = "/teams/test3/members"
#header = {'Authorization': token}
#body = {'member': 'test2'}
#method = "POST"

#team info
#url = "/teams/test3/members"
#header = {'Authorization': token}
#body = None
#method = "GET"

#post client details
url = "/clients/testapp1/details"
header = {'Authorization': token1}
body = {'tag1': 'sample1', 'tag2': 'sample112', 'tag3': 'sample3', 'category': 'business',
        'short_description': 'short des', 'long_description': 'long des',
        'permission_explanation': 'ex', 'publish': 'False'}
method = "POST"

#get client details
url = "/clients/testapp1/details"
header = {'Authorization': token1}
body = None
method = "GET"

#post client setting
#url = "/clients/test4/setting"
#header = {'Authorization': token}
#body = {'display_name': 'test_client4', 'contact_email': 'test4@naver.com'}
#method = "POST"

#get client setting
#url = "/clients/test4/setting"
#header = {'Authorization': token}
#body = None
#method = "GET"


test = api_request(host)
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
print resp
print content
