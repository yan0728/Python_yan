#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
import hashlib

ascii_number_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                      "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9", "0"]


def request_id():
    random_list = []
    for i in range(32):
        random_list.append(random.choice(ascii_number_chars))
    return ''.join(random_list)


class Environment:
    def __init__(self, application_id, application_key, security_key, host):
        self.__application_id = application_id
        self.__application_key = application_key
        self.__security_key = security_key
        self.__host = host

    @property
    def application_id(self):
        return self.__application_id

    @application_id.setter
    def application_id(self, application_id):
        self.__application_id = application_id

    @property
    def application_key(self):
        return self.__application_key

    @application_key.setter
    def application_key(self, application_key):
        self.__application_key = application_key

    @property
    def security_key(self):
        return self.__security_key

    @security_key.setter
    def security_key(self, security_key):
        self.__security_key = security_key

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self,host):
        self.__host = host


class SdkRequest:
    split = "::"

    def __init__(self, environment, request_path, method, body):
        self.__environment = environment
        self.__request_path = request_path
        self.__method = method
        self.__body = body
        self.__requestId = request_id()
        self.__content_type = "application/json;charset=UTF-8"
        self.__timestamp = int(round(time.time() * 1000))
        self.__content_md5 = hashlib.md5(body.encode("utf-8")).hexdigest()
        self.__sign_source = (environment.application_id + SdkRequest.split + environment.application_key
                                  + SdkRequest.split + self.__requestId
                                  + SdkRequest.split + self.__content_md5
                                  + SdkRequest.split + str(self.__timestamp)
                                  + SdkRequest.split + method
                                  + SdkRequest.split + request_path
                                  + SdkRequest.split + self.__content_type
                                  + SdkRequest.split + environment.security_key)
        self.__sign = hashlib.md5(self.__sign_source.encode("utf-8")).hexdigest()

    @property
    def request_id(self):
        return self.__requestId

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def content_type(self):
        return self.__content_type

    @property
    def content_md5(self):
        return self.__content_md5

    @property
    def method(self):
        return self.__method

    @property
    def request_path(self):
        return self.__request_path

    @property
    def sign(self):
        return self.__sign

    @property
    def body(self):
        return self.__body


env = Environment("qingdao-yeda", "AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY"
                  , "H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW"
                  , "https://dev-api-gateway.lianjieabs.com")


req = SdkRequest(env, "/file/info/apps/factoring-asset/loan/export/20221214/1670999005615/划款20221214142325.xlsx"
                 , "POST", "")
print(req.request_id)
print(req.timestamp)
print(req.content_type)
print(req.content_md5)
print(req.sign)
