from .spider import AgentSpider

class CompanySpider(AgentSpider):   
    name = 'company'     
    list_url_template = 'https://krisha.kz/pro/company/?page='
    
    card_class = '.company-card__only'
    def parse_agent(self, response):
        agent = super().parse_agent(response)
        name = response.css('.company-info__first-title::text')
        if len(name):
            agent['name'] = name.get().strip()
            
        time = response.css('.company-info__time::text')
        if len(time):
            agent['time'] = time.get().strip()
            
        address = response.css('.company-info__address::text')
        if len(address):     
            agent['address'] = address.get().strip()
        agent['agent_type'] = 3
        
        return agent