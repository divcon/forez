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

#sungjin
token = 'Token b6da821453aaaae2148c7c47433673b2889b8ff8'
#test
token = 'Token aeb6e590c44e085fe52020dbbce1d2f0d8ef83a7'
#test4
#token = 'Token d18f0e378d0abfc0b3321838dcc645cd25ba98e2'

#app registering
#url = "/clients"
#header = {'Authorization': token}
#body = {'name': 'test3', 'url': 'http://211.189.127.73:8000',
#        'redirect_uri': 'http://211.189.127.73:8000', 'client_type': '0'}
#method = "POST"

#app list
url = "/clients"
body = None
header = {'Authorization': token}
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
header = {'Authorization': token}
body = {'tag1': 'sample1', 'tag2': 'sample2', 'tag3': 'sample3', 'category': 'sample4', 'short': 'short des', 'long': 'long des', 'explanation': 'ex', 'publish': 'False'}
method = "POST"

#get client details
url = "/clients/testapp1/details"
header = {'Authorization': token}
body = None 
method = "GET"

test = api_request(host)
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
print resp
print content
