from krishascrapy.items import RentHouse
from .spider import HouseSpider

class RentHouseSpider(HouseSpider):
    name = "rent-house"
    list_url_template = 'https://krisha.kz/arenda/doma/?page='
    
    def __init__(self):
        self.ad = RentHouse()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad