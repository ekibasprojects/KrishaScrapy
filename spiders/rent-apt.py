from krishascrapy.items import RentApt
from .spider import AptSpider

class RentAptSpider(AptSpider):
    name = "rent-apt"
    list_url_template = 'https://krisha.kz/arenda/kvartiry/?page='
    
    def __init__(self):
        self.ad = RentApt()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad