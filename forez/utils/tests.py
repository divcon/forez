#-*- coding: utf-8 -*-
from request_form import api_request
#notebook test : True
#Server test : False
host = True
host = False





#test3
token3 = 'Token 2e8db1aaaa4d9f7798d9739ace085b6301a70537'
server_token3 = 'Token 8a0e3fa510aad716ac044de399f9f2545b0a2fbf'
#test
token1 = 'Token 0a1b58fa99959df21ca2220ec18bab48f939b5e1'
server_token1 = 'Token 0657086b001f75ca6d5a7e961e94cc5f95418d38'
#test2
token2 = 'Token 9161c6f52c5cb473a125a3a5517a67d37ed6f402'
server_token2 = 'Token 7ecb11dddef8b6a97897e4498e677b9d9aa76d45'

# join
# url = "/users"
# body = {'username': 'testuser1', 'password': 'test', 'phone': '010-6619-3238', 'email': 'test@naver.com',
#         'real_name': '밥줘', 'class_num': '23-1', 'gender': '여'}
# header = None
# method = "POST"

# search user
# url = "/search?username=p_ops"
# body = None
# header = {'Authorization': token1}
# method = "GET"

#login
url = "/tokens"
body = {'username': 'p_ops', 'password': '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225'}
header = None
method = 'POST'

#get user
url = "/user?username=test5"
body = None
header = None
method = 'GET'

#logout
url = "/tokens/pooingx2"
body = {'token': '0a1b58fa99959df21ca2220ec18bab48f939b5e1'}
header = None
method = "DELETE"

# changing information
# url = "/users/testuser"
# header = {'Authorization': token3}
# body = {'email': 'hello@naver.com', 'phone': '01001001', 'password': None}
# method = "PUT"

#app registering
url = "/clients"
header = {'Authorization': token1}
body = {'name': 'test4867w698', 'url': 'http://211.189.127.73:8000',
       'redirect_uris': 'http://211.189.127.73:8000',
       'client_type': 'confidential',
       'authorization_grant_type': 'authorization-code'}
method = "POST"

#app list 
# url = "/clients"
# body = None
# header = {'Authorization': token1}
# method = "GET"

#app info
# url = "/clients/testapp2"
# body = None
# header = {'Authorization': token3}
# method = "GET"

#modify url
# url = "/clients/testapp1"
# body = {"url": "http://123.123.123.12:8000", "redirect_uris": "http://123.123.123.12:8000"}
# header = {'Authorization': server_token1}
# method = "PUT"

#app delete
# url = "/clients/testapp1"
# header = {'Authorization': server_token1}
# method = "DELETE"

#team list
#url = "/teams"
#header = {'Authorization': token}
#body = None
#method = "GET"
#token = 'Token 9a8cf47d1c67f42370d2087a52e7f0939d590119'

#add member
#url = "/teams/testapp1/members"
#header = {'Authorization': server_token1}
#body = {'member': 'test3'}
#method = "POST"

#delete member
# url = "/teams/testapp1/members?username=test2"
# header = {'Authorization': token1}
# body = None
# method = "DELETE"

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
# url = "/clients/testapp2/setting"
# header = {'Authorization': token3}
# body = {'display_name': 'setting_test', 'contact_email': 'test4@naver.com', 'publish': 'True'}
# method = "POST"

#get client setting
#url = "/clients/testapp2/setting"
#header = {'Authorization': token3}
#body = None
#method = "GET"

#get access token
# url = "/o/token/"
# body = {"cleint_id": "TMcIpph@CU18e_@r07J0D_o??VToL.9GBJXt.!Wb",
#         "client_secret": "vQ0.Z0Sfqo@C6u;D27xtSoLs:LeZNk6G-GRDWnkq_uf3Yywj0=bFmau?=HYpxO4U;PWf4WT_2;c9YyheV7Rb9i;n?sWz6B3zKEaA?E@ffKuEv5z6O:MIBvn!c=Z!Q7R4i",
#         "grant_type": 'athorization-code', 'authorization': ''}
# header = None
# method = "POST"
#"client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=password&username=YOUR_USERNAME&password=YOUR_PASSWORD" http://localhost:8000/oauth2/access_token/
#
#get store list
#url = "/stores"
#body = None
#header = {'Authorization': token3}
#method = "GET"

# get app list by category
#url = "/stores?category=Webapp"
#body = None
#header = {'Authorization': token3}
#method = "GET"


# search apps
#url = "/stores?search=t&tag=True"
#body = None
#header = {'Authorization': token3}
#method = "GET"


# get app info
# url = "/stores/testapp1"
# body = None
# header = {'Authorization': token3}
# method = "GET"

# get authorization
# url = "/o/authorize?response_type=code&client_id=Tr952;dZ7iiX=J94B2ST9w;r7cgOqJ0BlBGASa-C&scope=read&state=xyz&approval_prompt=auto&redirect_uri=http://211.189.127.121:8080/JSper/loginGardenCallBack"
# # GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
# body = None
# header = {'Authorization': token2}
# method = "GET"


#add user app
# url = "/users/test1/apps"
# body = {"client_name": "testapp2"}
# header = {'Authorization': token1}
# method = "POST"

#delete user app
# url = "/users/p_ops/apps?name=zxcv"
# body = None
# header = {'Authorization': token1}
# method = "DELETE"


#get user's app
# url = "/users/p_ops/apps"
# body = None
# header = {'Authorization': token1}
# method = "GET"

# token test
url = '/o/token/'
body = {"code": "qgsziecddIPFkAmsZBFjjRcitlXmxt", "client_secret": "zMvWRZf6Z9E5JHXj0eaNJv8e86DXEJUn4bBXzRASiQPHvPaXLciULrM3oAhkkdgyMGoee2UhiKplH7SFHnziAFjhx25LfYOtsxCw6k1F2t6uhFAXDGuGK1SzsGIEySFj", "redirect_uri": "http://127.0.0.1:9000/oauth", "client_id": "N4DejrNGy7JBacEjJv3KtK20rKTfLvs9tgNlTsPG", "grant_type": "authorization_code"}
header = None
method = "POST"

# api test
# url = '/api/v1/me'
# body = None
# header = {'Authorization': 'Bearer WQF7oABoIuTPdR3MGsYZ5UyjB8F5IA'}
# method = "GET"

# setting password at first use
# url = '/api/v1/users/p_ops/projects'
# header = {'Authorization': 'Bearer MvTlvcwEuYu2erBlQq2j1NXcyDrrLh'}
# # header = None
# method = "GET"

test = api_request(host)
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
print resp
print content
