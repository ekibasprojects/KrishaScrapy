from krishascrapy.items import SellDacha
from .spider import DachaSpider

class SellDachaSpider(DachaSpider):
    name = "sell-dacha"
    list_url_template = 'https://krisha.kz/prodazha/dachi/?page='
    
    def __init__(self):
        self.ad = SellDacha()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
