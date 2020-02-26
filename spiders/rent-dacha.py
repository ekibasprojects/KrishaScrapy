from krishascrapy.items import RentDacha
from .spider import DachaSpider

class RentDachaSpider(DachaSpider):
    name = "rent-dacha"
    list_url_template = 'https://krisha.kz/arenda/dachi/?page='
    
    def __init__(self):
        self.ad = RentDacha()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad