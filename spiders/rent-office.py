from krishascrapy.items import RentOffice
from .spider import OfficeSpider

class RentOfficeSpider(OfficeSpider):
    name = "rent-office"
    list_url_template = 'https://krisha.kz/arenda/ofisa/?page='
    
    def __init__(self):
        self.ad = RentOffice()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad