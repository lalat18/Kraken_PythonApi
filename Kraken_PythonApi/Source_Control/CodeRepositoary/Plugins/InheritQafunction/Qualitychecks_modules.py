import pytest
import logging as logger
import json
import jsonpath


class Qualitycheksmodule():

    def __init__(self,**kwargs):
        self.DataTypes = {
            'ask': 'a',
            'bid': 'b',
            'Yesttrade': 'c',
            'Volume': 'v',
            'price': 'p',
            'Trade': 't',
            'Low': 'l',
            'High': 'h',
            'Open': 'o'
        }
    def test(self):
        DataTypes=self.DataTypes
        return (DataTypes)

    def retrive_mapping():
        key = 'Ticker'
        with open('package.json') as json_file:
            data = json.load(json_file)
            return data[key]

    def createMetadata(self,Tickerdict):
        DataTypes=self.DataTypes
        MappingResult=Qualitycheksmodule.retrive_mapping()
        #Tickerdict=json.loads(StrObj)
        #assert Tickerdict is None ,'Empty object is passed as API response output'
        res = {}
        for Type in MappingResult:
            Mappedlist = MappingResult[Type]
            UpdatedMap = [Type + '.' + i for i in Mappedlist]
            elements = (Tickerdict[DataTypes[Type]])
            result = dict(zip(UpdatedMap, elements))
            res.update(result)
        return res

