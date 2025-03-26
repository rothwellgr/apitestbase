import requests

class HTTPBinClient:
    def __init__(self):
        pass

    def get_slideshow(self):
        try:
            response = requests.get('https://httpbin.org/json')
            response.raise_for_status()

            return response.text
        except Exception as e:
            return f"Failed to retrieve data: {str(e)}"