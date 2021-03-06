from krishascrapy.items import SellWarehouse
from .spider import WarehouseSpider

class SellWarehouseSpider(WarehouseSpider):
    name = "sell-warehouse"
    list_url_template = 'https://krisha.kz/prodazha/prombazy/?page='
    
    def __init__(self):
        self.ad = SellWarehouse()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        mortgage = response.css('.offer__parameters-mortgaged')
        if len(mortgage):
            ad['mortgage'] = 1
        else:
            ad['mortgage'] = 0
        
        return ad
