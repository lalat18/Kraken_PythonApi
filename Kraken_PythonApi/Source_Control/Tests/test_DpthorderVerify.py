import pytest
import logging as logger
import json
import jsonpath
from Source_Control.CodeRepositoary.QaUtility.Genericutilites import generate_random_Ticker
from Source_Control.CodeRepositoary.Plugins.Basehelper import getApidata
from Source_Control.CodeRepositoary.Plugins.InheritQafunction.Test_Trade_OHLC_cases import Verifytrade_ohlc

@pytest.fixture(scope='module')
def getDepth():
    logger.info("Depth order Information request/response process")
    Payload = generate_random_Ticker()
    # make the call
    Data_obj = getApidata()
    Data_api_info = Data_obj.get_apidata(Payload, 'Depth')
    json_response = json.loads(Data_api_info)
    Result = (jsonpath.jsonpath(json_response, 'result..'))
    Orderbookdict = dict((Result[0]))
    key = list(Orderbookdict.keys())[0]
    assert Data_api_info, f"Get of Depth end point returned nothing"
    BidList = (Orderbookdict[key]['bids'])
    AskList = (Orderbookdict[key]['asks'])
    Create_Verifytrade_ohlc_Obj = Verifytrade_ohlc()
    Bidprices = Create_Verifytrade_ohlc_Obj.createlistbyindex(BidList, 0)
    Askprices = Create_Verifytrade_ohlc_Obj.createlistbyindex(AskList, 0)
    BidTime = Create_Verifytrade_ohlc_Obj.createlistbyindex(BidList, 2)
    AskTime = Create_Verifytrade_ohlc_Obj.createlistbyindex(AskList, 2)
    return (Bidprices,Askprices,BidTime,AskTime)

@pytest.mark.Crossedorder
def test_Crossedorder(getDepth):
    Bidprices = list(getDepth[0])
    Askprices = list(getDepth[1])
    for i in range(len(Bidprices)):
        assert Bidprices[i] < Askprices[i],'Seems like crossed Order'

@pytest.mark.Timechecks
def test_Quotearrival(getDepth):
    BidTime = list(getDepth[2])
    AskTime = list(getDepth[2])
    assert BidTime == sorted((BidTime)), \
        'Expecting Arrival of Bid to be in Timeseries format '
    assert AskTime == sorted((AskTime)), \
        'Expecting Arrival of Bid to be in Timeseries format '


