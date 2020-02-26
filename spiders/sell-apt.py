from krishascrapy.items import SellApt
from .spider import AptSpider

class SellAptSpider(AptSpider):
    name = "sell-apt"
    list_url_template = 'https://krisha.kz/prodazha/kvartiry/?page='
    
    def __init__(self):
        self.ad = SellApt()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad