import requests
from bs4 import BeautifulSoup
import traceback
from engines import ScrapEngine

class SeLoger(ScrapEngine):
    def scrap_data(self) -> str:
        mail_content = ""
        header = {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language" : "en-US,en;q=0.5",
                "Accept-Encoding" : "gzip, deflate, br",
                "Connection" : "keep-alive",
                "Pragma" : "no-cache",
                "Cache-Control" : "no-cache",
                "Upgrade-Insecure-Requests" : "1"
                }

        r = requests.get(self.config['URLS']['seloger'], headers=header)
        dom = BeautifulSoup(r.text, "html.parser")
        lists = dom.find_all("div", "Card__ContentZone-sc-7insep-5")
    
        for elem in lists:
            try:
                url = elem.find('a', "CoveringLink-a3s3kt-0", href=True)['href']
                if self.check_if_data_exist(url) is True:
                    continue
                name = elem.find("ul", "ContentZone__Tags-wghbmy-6").text
                price = elem.find("div", "Price__PriceContainer-sc-1g9fitq-0").text
                tags = elem.find("div", "ContentZone__Title-wghbmy-5").text
                localite = elem.find("div", "ContentZone__Address-wghbmy-1").text
                date = "??"
                self.write_data(url)
                mail_content += name + " | " + tags + " | " + localite + " | " + price + " | le " + date + "\n" + url + '\n-----------------------------------------------------\n'
            except:
                print(traceback.format_exc())
                pass
        return mail_content