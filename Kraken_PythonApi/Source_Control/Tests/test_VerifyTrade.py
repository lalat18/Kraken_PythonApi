import pytest
import logging as logger
import json
import jsonpath
from Source_Control.CodeRepositoary.QaUtility.Genericutilites import generate_random_Ticker
from Source_Control.CodeRepositoary.Plugins.Basehelper import getApidata
from Source_Control.CodeRepositoary.Plugins.InheritQafunction.Test_Trade_OHLC_cases import Verifytrade_ohlc

@pytest.fixture(scope='module')
def getTrade():
    logger.info("Trade Information request/response process")
    Payload=generate_random_Ticker()
    #make the call
    Data_obj=getApidata()
    Data_api_info = Data_obj.get_apidata(Payload,'Trades')
    json_response = json.loads(Data_api_info)
    Result = (jsonpath.jsonpath(json_response, 'result..'))
    Tradedict = dict((Result[0]))
    key = list(Tradedict.keys())[0]
    assert Data_api_info ,f"Get of Trades end point returned nothing"
    key = list(Tradedict.keys())[0]
    first_trade = Tradedict[key][0]
    Payloadnew = {}
    Payloadnew['pair'] = key
    Payloadnew['since'] = first_trade[2]
    '''Call different Module to prepare Test Data from both Trade and OHLC Endpoints'''
    Create_Verifytrade_ohlc_Obj = Verifytrade_ohlc()
    OHL_List = Create_Verifytrade_ohlc_Obj.test_getohlc(Payloadnew)
    Info_Trade_Open_Low_High = Create_Verifytrade_ohlc_Obj.Info_Trade_Open_low_high(Tradedict, key)
    OnlyHigh_List = Create_Verifytrade_ohlc_Obj.createlistbyindex(OHL_List, 2)
    OnlyLow_List = Create_Verifytrade_ohlc_Obj.createlistbyindex(OHL_List, 3)
    return (key,OHL_List,Info_Trade_Open_Low_High,Tradedict,OnlyHigh_List,OnlyLow_List)

@pytest.mark.tradetime
def test_tradetime(getTrade):
    key = (list(getTrade)[0])
    OHL_List = (list(getTrade)[1])
    Info_Trade_Open_Low_High = (list(getTrade)[2])
    OnlyHigh_List=(list(getTrade)[4])
    OnlyLow_List=(list(getTrade)[5])

@pytest.mark.Tradeopen
def test_verify_Trade_Open(getTrade):
    OHL_List = (list(getTrade)[1])
    Info_Trade_Open_Low_High = (list(getTrade)[2])
    print("This Test case is able to verify Trades and OHLC Api Endpoint")
    '''logic:
        the Trade.Value of first Occurance of Trade for Symbol/pair
                   Must be Same
        The Trade Open Value obtained from ohlc Endpoint and first trade arrival time is
        used Since parameter to  retrive the result '''
    assert Info_Trade_Open_Low_High[0] == OHL_List[0][1],\
        'Seems like TRADE.OPEN is not matching with OHLC Endpoint result'

@pytest.mark.sortbytime
def test_Verify_Trades_SortedbyTime(getTrade):
    key = (list(getTrade)[0])
    Tradedict = (list(getTrade)[3])
    Timestamp = list()
    for ele in (Tradedict[key]):
        Timestamp.append(ele[2])
    assert Timestamp == sorted((Timestamp)) ,\
        'Expecting Arrival of trades to be in Timeseries format '

@pytest.mark.Tradehigh
def test_verify_Trade_High(getTrade):
    Info_Trade_Open_Low_High = (list(getTrade)[2])
    OnlyHigh_List = (list(getTrade)[4])
    # Verify your Trade High with the Trades End Point response
    '''logic:
    the Max(Trade.Price) of  Trade endpoint  for Symbol/pair
                    Must be Same
    With TRADE.HIGH value returned from OHL_List '''
    assert max(OnlyHigh_List) == Info_Trade_Open_Low_High[1] ,\
        'Seems like TRADE.High is not matching with OHLC Endpoint result'

@pytest.mark.Tradelow
def test_verify_Trade_Low(getTrade):
    Info_Trade_Open_Low_High = (list(getTrade)[2])
    OnlyLow_List = (list(getTrade)[5])
    '''logic:
        the Max(Trade.Price) of  Trade endpoint  for Symbol/pair
                    Must be Same
        With TRADE.HIGH value returned from OHL_List '''
    assert min(OnlyLow_List) == Info_Trade_Open_Low_High[2],\
    'Seems like TRADE.OPEN is not matching with OHLC Endpoint result'