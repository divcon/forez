from request_form import api_request

url = "/users/sungjin"
body = {'username': 'sungjin', 'password': 'rkems'}
header = {'Authorization': 'Token 57bd76c1e2079f13124dcb0b45362a07f156b9c4'}
method = "GET"

#url = "/users/sungjin"
#header = {'Authorization': 'Token b07f93d2943f4d9942e84ac9a21e899f54d94062'}
#method = "GET"


#notebook test : True
#Server test : False
host = True

test = api_request(host)
# resp, content = test.http_request(url=url, method="POST", body=body)
#"token": "a658422cb15e561df5073e43bbdee9e5703232ba", "id": 1
resp, content = test.http_request(method=method, url=url, headers=header)
print resp
print content
