from request_form import api_request

test = api_request()
url = "/users"
body = {'username': 'httptest', 'password': '123', 'email': 'test@naver.com'}

# resp, content = test.http_request(url=url, method="POST", body=body)

resp, content = test.http_request(url=url)
print resp
print content
