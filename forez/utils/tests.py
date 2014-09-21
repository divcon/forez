from request_form import api_request

test = api_request()
url = "/tokens"
body = {'username': 'sungjin', 'password': 'rkems'}

# resp, content = test.http_request(url=url, method="POST", body=body)

resp, content = test.http_request(method="POST", url=url, body=body)
print resp
print content
