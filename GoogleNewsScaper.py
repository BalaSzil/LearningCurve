import urllib3
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.site)
        response_status = response.status
        
        if response_status == 200:
            print(f'Successful response\nStatus code: {response_status}')
        else:
            print(f'Failed response\nStatus code: {response_status}')
        
        html = response.data.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url:
                print('\n' + 'https://news.google.com/' + url[2:])
    
gugli_news_url = 'https://news.google.com/'
gugli_scraper = Scraper(gugli_news_url)
gugli_scraper.scrape()