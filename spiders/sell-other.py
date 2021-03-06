from krishascrapy.items import SellOther
from .spider import OtherSpider

class SellOtherSpider(OtherSpider):
    name = "sell-other"
    list_url_template = 'https://krisha.kz/prodazha/prochej-nedvizhimosti/?page='
    
    def __init__(self):
        self.ad = SellOther()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
