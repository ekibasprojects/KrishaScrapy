from krishascrapy.items import RentRoom
from .spider import RoomSpider

class RentRoomSpider(RoomSpider):
    name = "rent-room"
    list_url_template = 'https://krisha.kz/arenda/komnaty/?page='
    
    def __init__(self):
        self.ad = RentRoom()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad