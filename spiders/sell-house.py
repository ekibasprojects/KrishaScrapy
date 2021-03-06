from krishascrapy.items import SellHouse
from .spider import HouseSpider

class SellHouseSpider(HouseSpider):
    name = "sell-house"
    list_url_template = 'https://krisha.kz/prodazha/doma/?page='
    
    def __init__(self):
        self.ad = SellHouse()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
