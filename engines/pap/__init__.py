import requests
from bs4 import BeautifulSoup
import traceback
from engines import ScrapEngine

class Pap(ScrapEngine):
    def scrap_data(self) -> str:
        mail_content = ""
        localisations = self.config['REGIONS']['villes'].split(', ')
        header = {
            "Host": "www.pap.fr",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"
            }
        r = requests.get(self.config['URLS']['pap'], headers=header)
        print(r.status_code)
        dom = BeautifulSoup(r.text, "html.parser")
        lists = dom.find_all("div", "search-list-item-alt")
    
        for elem in lists:
            try:
                localite = elem.find("a", "item-title").find("span").text
                res = any(ele in localite for ele in localisations)
                if res is False:
                    continue
                url = "https://www.pap.fr" + elem.find('a', "item-title", href=True)['href']
                if self.check_if_data_exist(url) is True:
                    continue
                name = elem.find("ul", "item-tags").text.replace("\n", ' ')
                tags = elem.find("p", "item-description").text.strip()
                price = elem.find("span", "item-price").text
                date = "??"
                self.write_data(url)
                mail_content += name + " | " + tags + " | " + localite + " | " + price + " | le " + date + "\n" + url + '\n-----------------------------------------------------\n'
                print(name + " | " + tags + " | " + localite + " | " + price + " | le " + date + "\n" + url + '\n-----------------------------------------------------\n')
            except:
                print(traceback.format_exc())
                pass
        return mail_content
