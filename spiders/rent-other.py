from krishascrapy.items import RentOther
from .spider import OtherSpider

class RentOtherSpider(OtherSpider):
    name = "rent-other"
    list_url_template = 'https://krisha.kz/arenda/prochej-nedvizhimosti/?page='
    
    def __init__(self):
        self.ad = RentOther()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad