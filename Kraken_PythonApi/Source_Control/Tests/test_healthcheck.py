import pytest
import logging as logger
import requests

@pytest.mark.healthcheck1
def test_healthcheck_1():
    logger.info("Just Running Healthcheck")

@pytest.mark.systemstatus
def test_systemstats():
    Url="https://api.kraken.com/0/public/SystemStatus"
    Api_Response=requests.get(Url)
    assert Api_Response.status_code == 200, "Eroor- Seems like System is not online"