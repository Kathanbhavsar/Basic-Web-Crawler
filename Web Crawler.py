import requests
import re

class WebCrawler:
    def __init__(self):
        self.discovered_website=[]

    def crawl(self,start_url):
        queue=[start_url]
        self.discovered_website.append(start_url)

        while queue:

            actual_url=queue.pop(0)
            print(actual_url)

            actual_url_html=self.read_raw_html(actual_url)

            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_website:
                    self.discovered_website.append(url)
                    queue.append(url)

    def get_links_from_html(self,raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",raw_html)

    def read_raw_html(self,url):
        raw_html=''
        try:
            raw_html=requests.get(url).text
        except Exception as e:
            pass
        return raw_html


if __name__=="__main__":
    crawler=WebCrawler()
    crawler.crawl('https://www.linkedin.com/jobs/search/?currentJobId=3220905282&distance=25&f_E=1&geoId=102713980&keywords=data%20scientist')
