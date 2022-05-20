# importing the module
from Source_Control.CodeRepositoary.Plugins.hosts_config import META_DATA
from Source_Control.CodeRepositoary.Plugins.hosts_config import API_HOSTS
from Source_Control.CodeRepositoary.QaUtility.Genericutilites import generate_random_Ticker
from Source_Control.CodeRepositoary.Plugins.Basehelper import getApidata
import requests
import json
import jsonpath
import os
import logging as logger

class Verifytrade_ohlc(object):

    def __init__(self,**kwargs):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def test_getohlc(self,Payload):
        logger.info("Trade Information request/response process")
        # make the call
        Data_obj = getApidata()
        Data_api_info = Data_obj.get_apidata(Payload, 'OHLC')
        json_response = json.loads(Data_api_info)
        Result = (jsonpath.jsonpath(json_response, 'result..'))
        OHL = dict((Result[0]))
        key = list(OHL.keys())[0]
        OHL_List = (OHL[key])
        assert Data_api_info, f"Get of OHLC end point returned nothing"
        return OHL_List

    '''Generic function will be used to create list of 
       OPEN/LOW/HIGH values from OHLC endpoint Return'''
    def createlistbyindex(self,OHL_List,Index):
        temp = list()
        for ele in (OHL_List):
            temp.append(ele[Index])
        return (temp)

    def Info_Trade_Open_low_high(self,Tradedict, key):
        '''This function will help to gather all the Information
        with Regards to HIGH/LOW/OPEN from both the Endpoints
            1. Trades
            2. OHLC
        '''
        Trade_Open_low_high = list()
        for ele in (Tradedict[key]):
            Trade_Open_low_high.append(ele[0])
        Info_Trade_Open_Low_High = list()
        Info_Trade_Open_Low_High.append(Trade_Open_low_high[0])
        Info_Trade_Open_Low_High.append(max(Trade_Open_low_high))
        Info_Trade_Open_Low_High.append(min(Trade_Open_low_high))
        return (Info_Trade_Open_Low_High)