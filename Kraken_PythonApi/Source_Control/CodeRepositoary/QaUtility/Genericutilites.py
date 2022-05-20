import logging as logger
import random
import requests
import json
import jsonpath
import string

def generate_random_Ticker(ticker=None):
    logger.debug("Generating random Assest Class Pair")

    if not ticker:
            url = "https://api.kraken.com/0/public/AssetPairs"
            response = requests.get(url)
            assert response.status_code == 200, "Eroor Incorrect Response while getting Ticker Info"
            json_response = json.loads(response.text)
            results = jsonpath.jsonpath(json_response, 'result..altname')
            Payload = {}
            if not results:
                print("List Is Empty")
                return ("No Value on Assertpair")
            else:
                Ticker = random.choices(results)
                Payload['pair'] = Ticker[0]
                return (Payload)


