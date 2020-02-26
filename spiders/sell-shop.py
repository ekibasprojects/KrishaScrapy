from krishascrapy.items import SellShop
from .spider import ShopSpider

class SellShopSpider(ShopSpider):
    name = "sell-shop"
    list_url_template = 'https://krisha.kz/prodazha/magazina/?page='
    
    def __init__(self):
        self.ad = SellShop()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['exchange'] = self.getFieldValue(response, 'has_change')
        
        return ad
