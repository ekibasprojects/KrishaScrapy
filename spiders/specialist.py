from .spider import AgentSpider

class SpecialistSpider(AgentSpider): 
    name = 'specialist'
    list_url_template = 'https://krisha.kz/pro/specialist/?page='
    
    card_class = '.specialist-card__only'
    def parse_agent(self, response):
        agent = super().parse_agent(response)
        name = response.css('.specialist-info__first-title::text')
        if len(name):
            agent['name'] = name.get().strip()
            
        time = response.css('.specialist-info__time::text')
        if len(time):
            agent['time'] = time.get().strip()
            
        address = response.css('.specialist-info__address::text')
        if len(address):     
            agent['address'] = address.get().strip()
        agent['agent_type'] = 2
        
        return agent