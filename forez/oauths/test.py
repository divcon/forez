# -*- coding: utf-8 -*-
import httplib2
import json



h = httplib2.Http()
client_id = '<qKdUf!3pGIsA4o7hnm5eZY7OZ88j!b.!!=3vg8bJ>'
client_secret = '<r1aaK-R7L6ZfkNAHgUZ-635Wv1y;Fo9Ro6l_Iu;Nj3SHmA=d!?SaOaPfIp-3irxZ?kw.jD@;e-Z=lmb.2SVFc;OTmiM?L2U2cJNg=thHWgtl0.ORJh.W0Ln0w=kA.ryY>'
request_url = 'http://' + client_id + ':' + client_secret + '@localhost:8000/o/token/'
request_body = {
    'grant_type': 'password',
    'username': 'sungjin',
    'password': 'rkems',
}
method = "POST"
request_header = dict()
resp, content = h.request(request_url, method=method, body=request_body, headers=request_header)

# curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" http://<client_id>:<client_secret>@localhost:8000/o/token/