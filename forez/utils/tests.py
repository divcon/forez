#-*- coding: utf-8 -*-
from request_form import api_request
#notebook test : True
#Server test : False
host = True
host = False


#login
url = "/tokens"
body = {'username': 'test3', 'password': 'test'}
header = None
method = 'POST'


#test3
token3 = 'Token 559d073a1554c40f862bea38796e59f1e081156e'
server_token3 = 'Token 8a0e3fa510aad716ac044de399f9f2545b0a2fbf'
#test
token1 = 'Token 17eaae811ea352c0852eef42ee9e1328eac71340'
server_token1 = 'Token 0657086b001f75ca6d5a7e961e94cc5f95418d38'
#test2
token2 = 'Token d7e5636f0c9118abd3d734cdc6f329a3d4f6b458'
server_token2 = 'Token 7ecb11dddef8b6a97897e4498e677b9d9aa76d45'

# join
url = "/users"
body = {'username': 'testqwer', 'password': 'test', 'phone': '0000', 'email': 'test@naver.com',
        'real_name': 'testuser', 'class_num': '23', 'gender': 'male'}
header = None
method = "POST"

# changing information
#url = "/users/test3"
#header = {'Authorization': token3}
#body = {'email': 'hello@naver.com', 'phone': '01001001', 'password': 'rkems'}
#method = "PUT"

#app registering
#url = "/clients"
#header = {'Authorization': token3}
#body = {'name': 'test4867w698', 'url': 'http://211.189.127.73:8000',
#        'redirect_uris': 'http://211.189.127.73:8000',
#        'client_type': 'confidential',
#        'authorization_grant_type': 'authorization-code'}
#method = "POST"

#app list 
url = "/clients"
body = None
header = {'Authorization': token1}
method = "GET"

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
#url = "/oauths/authorize?response_type=code&client_id=HuW!F1Ph_liu_!9IGakzEMbAP3.J9FKrWfFo4rPx&scope=read&state=xyz&approval_prompt=auto&redirect_uri=http://211.189.127.73:8000"
#GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
#body = None
#header = {'Authorization': token2}
#method = "GET"


#add user app
# url = "/users/test1/apps"
# body = {"client_name": "testapp2"}
# header = {'Authorization': token1}
# method = "POST"

#delete user app
# url = "/users/test5/apps?name=zxcv"
# body = None
# header = {'Authorization': token1}
# method = "DELETE"


#get user's app
# url = "/users/test1/apps"
# body = None
# header = {'Authorization': token1}
# method = "GET"


# api test

url = '/api/v1/users/sungjin'
body = None
header = {'Bearer PiVjkteBWxSiXRxVV8P8oNk8oxxydX'}
method = "GET"


test = api_request(host)
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
print resp
print content
