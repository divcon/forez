from request_form import api_request

url = "/clients"
#body = {'phone': '000000000', 'password': 'rkems', 'email': 'abv@test.com'}
#body = {'name': 'testuser1212', 'url': 'http://211.189.127.73:8000', 'redirect_uri': 'http://211.189.127.73:8000', 
#        'client_type': '0'}
header = {'Authorization': 'Token 94083a1a472b0f1b36dd0d5f79b959f30cbae78b'}
method = "GET"

#url = "/clients/sungjin1"
##header = {'authorization': 'token 94083a1a472b0f1b36dd0d5f79b959f30cbae78b'}
#header = {'authorization': 'token 7fe8d203d29bca0197ab48d7c8546686eef22481'}
#body = {'url': 'http://211.189.127.73:8080', 'redirect_uri': 'http://211.189.127.73:8080'}
#method = "PUT"


#notebook test : True
#Server test : False
host = True

#join us


#login
url = "/tokens"
body = {'username': 'sungjin', 'password': 'rkems'}
method = 'POST'

#app registering
url = "/clients"
header = {'Authorization': 'Token aca623fac800aa174eafeb7ff8213024e459233e'}
body = {'name': 'test3', 'url': 'http://211.189.127.73:8000', 'redirect_uri': 'http://211.189.127.73:8000', 
        'client_type': '0'}
method = "POST"

#app list
#url = "/clients/testuser1213"
#header = {'Authorization': 'Token 3a327baddb77b0a0c86bb23c4dd321a3a547b987'}
#method = "GET"

#app delete
#url = "/clients/testuser1213"
#header = {'Authorization': 'Token 3a327baddb77b0a0c86bb23c4dd321a3a547b987'}
#method = "DELETE"


test = api_request(host)
# resp, content = test.http_request(url=url, method="POST", body=body)
#"token": "a658422cb15e561df5073e43bbdee9e5703232ba", "id": 1
resp, content = test.http_request(method=method, url=url, headers=header, body=body)
#resp, content = test.http_request(method=method, url=url)#, headers=header)
print resp
print content
