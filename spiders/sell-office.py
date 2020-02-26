from krishascrapy.items import SellOffice
from .spider import OfficeSpider

class SellOfficeSpider(OfficeSpider):
    name = "sell-office"
    list_url_template = 'https://krisha.kz/prodazha/ofisa/?page='
    
    def __init__(self):
        self.ad = SellOffice()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
