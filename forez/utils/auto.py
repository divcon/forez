from request_form import api_request
import json
import sys
import os

# server setting
#notebook : true
#server   : False
host = True 
directory = "/home/sungjin/error/"
extends = ".html"

def bad_exit():
    print "occured error. program will exit"
    sys.exit()

def init_test():
    file_list = os.listdir(directory)
    for f in file_list:
        os.remove(directory + f)

def join():
#join test users
# config common interface
    url = "/users"
    method = "POST"
    header = None
#generate error log
    file_name = "join"

    print "start to join test users"
# test1
    body = {'username': 'test1', 'password': 'test', 'phone': '0000', 'email': 'test@naver.com',
            'real_name': 'testuser', 'class_num': '23', 'gender': 'male'}
    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)
    if resp.status == 201:
        print "make test1"
    else :
        log_file = open(directory + file_name + '1' + extends, 'w')
        log_file.write(content)
        bad_exit()

# test2
    body = {'username': 'test2', 'password': 'test', 'phone': '0000', 'email': 'test@naver.com',
            'real_name': 'testuser', 'class_num': '23', 'gender': 'male'}
    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print "make test2"
    else :
        log_file = open(directory + file_name + '2' + extends, 'w')
        log_file.write(content)
        bad_exit()

# test3
    body = {'username': 'test3', 'password': 'test', 'phone': '0000', 'email': 'test@naver.com',
            'real_name': 'testuser', 'class_num': '23', 'gender': 'male'}
    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print "make test3"
    else :
        log_file = open(directory + file_name + '3' + extends, 'w')
        log_file.write(content)
        bad_exit()

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
    body = {'name': 'testapp1', 'url': 'http://211.189.127.73:8000',
            'redirect_uri': 'http://211.189.127.73:8000', 'client_type': '0'}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print content
    else :
        log_file = open(directory + file_name + '1' + extends, 'w')
        log_file.write(content)
        bad_exit()

# clients2
    header = {'Authorization': 'Token ' + token_dict['3']}
    body = {'name': 'testapp2', 'url': 'http://211.189.127.73:8000',
            'redirect_uri': 'http://211.189.127.73:8000', 'client_type': '0'}

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print content
    else :
        log_file = open(directory + file_name + '2' + extends, 'w')
        log_file.write(content)
        bad_exit()

def give_permission(token_dict):
    file_name = "teams"
    url = "/teams/testapp1/members"
    header = {'Authorization': 'Token ' + token_dict['1']}
    body = {'member': 'test2'}
    method = "POST"

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 201:
        print content
    else :
        log_file = open(directory + file_name + '1' + extends, 'w')
        log_file.write(content)
        bad_exit()

def enter_app_details(token_dict):
    file_name = "client_details"
    url = "/clients/testapp1/details"
    header = {'Authorization': 'Token ' + token_dict['1']}
    body = {'tag1': 'sample1', 'tag2': 'sample2', 'tag3': 'sample3', 'category': 'business',
            'short_description': 'short des', 'long_description': 'long des', 
            'permission_explanation': 'ex', 'publish': 'False'}
    method = "POST"

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 200:
        print content
    else :
        log_file = open(directory + file_name + extends, 'w')
        log_file.write(content)
        bad_exit()

def enter_app_details(token_dict):
    file_name = "client_details"
    url = "/clients/testapp1/setting"
    header = {'Authorization': 'Token ' + token_dict['1']}
    body = {'display_name': 'test_client', 'contact_email': 'test@naver.com'}
    method = "POST"

    test = api_request(host)
    resp, content = test.http_request(method=method, url=url, headers=header, body=body)

    if resp.status == 200:
        print content
    else :
        log_file = open(directory + file_name + extends, 'w')
        log_file.write(content)
        bad_exit()

init_test()
join()
token_dict = login()
registering_clients(token_dict)
give_permission(token_dict)
enter_app_details(token_dict)
enter_app_setting(token_dict)

































