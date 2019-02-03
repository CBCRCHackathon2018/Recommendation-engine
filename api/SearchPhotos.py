import PexelsAPI as papi
import requests as rq

API_Auth = papi.Pexels_API_Key
HEADERS = {'Authorization' : API_Auth}
base_url = "https://api.pexels.com/v1/search?query="
url_suffix = "&per_page=15&page=1"

class PhotoSearch:

    session = None
    
    def __init__(self):
        self.session = rq.Session()

    def MakeRequest(self, strArray):
        buf = ''
        for keyword in strArray:
            temp = '+' + keyword
            buf = buf + temp
        url = base_url + buf[1:] + url_suffix

        request = rq.Request(method='GET', url = url, headers=HEADERS)
        resp = self.session.send(request.prepare()).json()

        return resp
