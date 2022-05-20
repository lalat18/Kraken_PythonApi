from Source_Control.CodeRepositoary.Plugins.hosts_config import API_HOSTS
import requests
import json
import jsonpath
import os
import logging as logger

class Requestutility():

    def __init__(self,**kwargs):
        self.env = os.environ.get('ENV','test')
        self.base_url = API_HOSTS[self.env]

    def getdata(self,Payload,endpoint,expected_status_code=200):
        if endpoint :
            Url=self.base_url+"/"+endpoint
            response=requests.get(Url,params=Payload)
            self.status_code = response.status_code
            assert self.status_code == int(expected_status_code),\
            f'Expected status code {expected_status_code} but actual {self.status_code}'
            return (response.text)
