import requests
import pytest
import json

@pytest.fixture
def res_obj():
    def _res_obj(ip="176.185.160.94"):
        '''
        This fixture will create a response object
        to be used in subsequent tests
        '''
        try:
            # i am using verify=false just to ignore cert and ssl warnings
            res = requests.get("https://ipinfo.io/%s/geo" %str(ip), verify=False)
            return res
        except Exception as e:
            print (str(e))
    return _res_obj

def test_api(res_obj):
    '''
    This test is verifying if the api is
    live'''
    api_res = res_obj()
    #for now just verifying status_code is 200
    #without complicating too much
    assert api_res.status_code == 200

def test_city_in_api_res(res_obj):
    '''
    This test is  verifying if the response
    has city in it'''
    api_res = res_obj()
    assert  (json.loads(api_res.content)).has_key("city")

@pytest.mark.parametrize("ip, actual_city, actual_country_code",
                        [("165.185.160.94", "toronto", "ca"), 
                        ("167.185.160.94", "cincinnati","us"), 
                        ("161.185.160.93", "new york city", "us")])
def test_various_ips(res_obj, ip, actual_city,actual_country_code):
    '''
    This test verifies if it is returning the
    correct city and country (we know that the ips are in the right cities)'''
    api_res = res_obj(ip=ip)
    assert (json.loads(api_res.content))["city"].lower() == actual_city
    assert (json.loads(api_res.content))["country"].lower() == actual_country_code
