from krishascrapy.items import RentWarehouse
from .spider import WarehouseSpider

class RentWarehouseSpider(WarehouseSpider):
    name = "rent-warehouse"
    list_url_template = 'https://krisha.kz/arenda/prombazy/?page='
    
    def __init__(self):
        self.ad = RentWarehouse()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        # add necessary fields
        
        return ad