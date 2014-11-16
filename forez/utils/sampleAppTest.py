from request_form import api_request
import json
import sys
import os

# server setting
#notebook : true
#server   : False
host = True
host = False
directory = "/home/sungjin/error/"
extends = ".html"

def bad_exit():
    print "occured error. program will exit"
    sys.exit()

def init_test():
    file_list = os.listdir(directory)
    for f in file_list:
        os.remove(directory + f)

def login():
# Get Each token
#config common interface
    url = "/tokens"
    method = "POST"
    header = None
    password = "test"
#generate error log
    file_name = "login"

    print "get each tokens"
#test1
    body = {"username": "test1", "password": password}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        token1 = json.loads(content)['token']
        print "token1 : " + token1
    else :
        log_file = open(directory + file_name + '1' + extends, 'w')
        log_file.write(content)
        bad_exit()

#test2
    body = {"username": "test2", "password": password}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        token2 = json.loads(content)['token']
        print "token2 : " + token2
    else :
        log_file = open(directory + file_name + '2' + extends, 'w')
        log_file.write(content)
        bad_exit()

#test3
    body = {"username": "test3", "password": password}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        token3 = json.loads(content)['token']
        print "token3 : " + token3
    else :
        log_file = open(directory + file_name + '3' + extends, 'w')
        log_file.write(content)
        bad_exit()

    token_dict = dict()
    token_dict['1'] = token1
    token_dict['2'] = token2
    token_dict['3'] = token3
    return token_dict

def registering_clients(token_dict):
    url = "/clients"
    method = "POST"

#generate error log
    file_name = "post_clients"

# clients1
    header = {'Authorization': 'Token ' + token_dict['1']}
    body = {'name': 'sampleapp1', 'url': 'http://localhost:8080/GardenSampleApp_4',
            'redirect_uris': 'http://localhost:8080/GardenSampleApp_4/login_success.jsp', 
            'client_type': 'confidential',
            'authorization_grant_type': 'authorization-code'}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print content
    else :
        log_file = open(directory + file_name + '1' + extends, 'w')
        log_file.write(content)
        bad_exit()

token_dict = login()
registering_clients(token_dict)
