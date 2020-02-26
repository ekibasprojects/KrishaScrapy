from krishascrapy.items import RentShop
from .spider import ShopSpider

class RentShopSpider(ShopSpider):
    name = "rent-shop"
    list_url_template = 'https://krisha.kz/arenda/magazina/?page='
    
    def __init__(self):
        self.ad = RentShop()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['rent_unit'] = self.getFieldValue(response, 'rent.square')
        
        return ad