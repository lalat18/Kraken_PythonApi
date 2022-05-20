from Source_Control.CodeRepositoary.QaUtility.Genericutilites import generate_random_Ticker
from Source_Control.CodeRepositoary.QaUtility.Requestsutility import Requestutility
class getApidata(object):

    def __init__(self):
        self.requests_utility=Requestutility()

    def get_apidata(self,Ticker=None,Endpoint=None,**kwargs):
        if not Ticker :
            Ticker=generate_random_Ticker()
        result=self.requests_utility.getdata(Ticker,Endpoint)
        return result


