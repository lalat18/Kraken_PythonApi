import pytest
import logging as logger
import json
import jsonpath
from Source_Control.CodeRepositoary.QaUtility.Genericutilites import generate_random_Ticker
from Source_Control.CodeRepositoary.Plugins.Basehelper import getApidata
from Source_Control.CodeRepositoary.Plugins.InheritQafunction.Qualitychecks_modules import  Qualitycheksmodule

@pytest.fixture(scope='module')
def getTicker():
    logger.info("Ticker Information request/response process")
    Payload=generate_random_Ticker()
    #make the call
    Data_obj=getApidata()
    Data_api_info = Data_obj.get_apidata(Payload,'Ticker')
    json_response = json.loads(Data_api_info)
    Result = (jsonpath.jsonpath(json_response, 'result..'))
    Tickerdict = dict((Result[1]))
    assert Data_api_info ,f"Get of Ticker end point returned nothing"
    #retrive_mapping_Obj=Qualitycheksmodule.retrive_mapping()
    createMetadata_Obj=Qualitycheksmodule()
    createMetadata_result=createMetadata_Obj.createMetadata(Tickerdict)
    return createMetadata_result

@pytest.mark.Tickerfordepth
def test_Tickerfordepth(getTicker):
    createMetadata_result=getTicker
    #Check if ASK.PRICE is less than BID.PRICE
    assert createMetadata_result['ask.price'] > createMetadata_result['bid.price'] ,\
    'ASK.PRICE is less than BID.PRICE from Ticker Info Seems like we have Crossed Order'

@pytest.mark.Tickerfortrade
def test_Tickerfortrade(getTicker):
    createMetadata_result = getTicker
    assert (int(createMetadata_result['Trade.Today.TradeSize']) != 0 and int(createMetadata_result['Open.Trade.Open']) == 0 ) ,\
            'Seems like Incorrect TRADE.OPEN Population '


