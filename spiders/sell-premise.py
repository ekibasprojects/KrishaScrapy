from krishascrapy.items import SellPremise
from .spider import PremiseSpider

class SellPremiseSpider(PremiseSpider):
    name = "sell-premise"
    list_url_template = 'https://krisha.kz/prodazha/pomeshhenija/?page='
    
    def __init__(self):
        self.ad = SellPremise()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
