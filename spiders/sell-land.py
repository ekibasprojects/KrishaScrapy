from krishascrapy.items import SellLand
from .spider import LandSpider

class SellLandSpider(LandSpider):
    name = "sell-land"
    list_url_template = 'https://krisha.kz/prodazha/uchastkov/?page='
    
    def __init__(self):
        self.ad = SellLand()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
