import requests
from bs4 import BeautifulSoup
import traceback
from engines import ScrapEngine

class Leboncoin(ScrapEngine):
    def scrap_data(self) -> str:
        mail_content = ""
        header = {
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language" : "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding" : "gzip, deflate, br",
                "Connection" : "keep-alive",
                "Host" : "www.leboncoin.fr",
                "Sec-GPC" : "1",
                "TE" : "Trailers",
                "Upgrade-Insecure-Requests" : "1"
                }
        r = requests.get(self.config['URLS']['lbc'], headers=header)
        print(r.text)
        dom = BeautifulSoup(r.text, "html.parser")
        lists = dom.find_all("div", "styles_classified__aKs-b")
        for elem in lists:
            if not elem.find('a', "AdCard__AdCardLink-sc-1h74x40-0", href=True):
                continue
            try:
                url = elem.find('a', "AdCard__AdCardLink-sc-1h74x40-0", href=True)['href']
                url = "https://www.leboncoin.fr" + url 
                if self.check_if_data_exist(url) is True:
                    continue
                name = elem.find("p", "AdCardTitle-e546g7-0").text
                price = elem.find("span", "AdCardPrice__Wrapper-bz31y2-0").text
                rows = elem.findAll("p", "TextContent__TextContentWrapper-sc-1lw081p-0")
                #tags = rows[0].text
                tags = ''
                localite = rows[0].text
                date = rows[1].text
                self.write_data(url)
                mail_content += name + " | " + tags + " | " + localite + " | " + price + " | le " + date + "\n" + url + '\n-----------------------------------------------------\n'
                print(name + " | " + tags + " | " + localite + " | " + price + " | le " + date + "\n" + url + '\n-----------------------------------------------------\n')
            except:
                print(traceback.format_exc())
                pass
        return mail_content