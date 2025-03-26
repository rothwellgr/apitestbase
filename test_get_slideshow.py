import json
from clients.http_bin_client import HTTPBinClient
from dto.slideshow_dto import SlideshowDTO

slideshow_client = HTTPBinClient()

data = json.loads(slideshow_client.get_slideshow())
slide_dto = SlideshowDTO.from_json(data['slideshow'])

def test_get_slideshow():
    assert slide_dto.author == "Yours Truly"