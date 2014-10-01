from request_form import api_request

url = "/clients"
body = {'name': 'test6', 'url': 'http://211.189.127.73:8000', 'redirect_uri': 'http://211.189.127.73:8000', 'client_type': 0}
header = {'Authorization': 'Token 57bd76c1e2079f13124dcb0b45362a07f156b9c4'}
method = "POST"

url = "/clients/2"
header = {'Authorization': 'Token b07f93d2943f4d9942e84ac9a21e899f54d94062'}
#body = {'name': 'test5', 'url': 'http://211.189.127.73:8000', 'redirect_uri': 'http://211.189.127.73:8000', 'client_type': 0}
method = "GET"


#notebook test : True
#Server test : False
host = True

test = api_request(host)
# resp, content = test.http_request(url=url, method="POST", body=body)
#"token": "a658422cb15e561df5073e43bbdee9e5703232ba", "id": 1
resp, content = test.http_request(method=method, url=url, headers=header)
print resp
print content
