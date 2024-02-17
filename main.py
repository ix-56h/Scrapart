#!/usr/bin/env python3
import time
import warnings
import traceback
import configparser
import base64
from datetime import datetime, date
from engines import MailingEngine
from engines.leboncoin import Leboncoin
from engines.pap import Pap
from engines.seloger import SeLoger


warnings.filterwarnings('ignore')
mail_content    = ''

# Get configuration files (urls, phone number...)
def get_config():
    config = configparser.ConfigParser()
    config.read('config.txt')
    # config['URLS']['pap'] = base64.b64decode(config['URLS']['pap'])
    # config['URLS']['lbc'] = base64.b64decode(config['URLS']['lbc'])
    # config['URLS']['seloger'] = base64.b64decode(config['URLS']['seloger'])
    
    config['GLOBAL']['end_date']
    return config

# Get all datas, using Scrap Functions
def refresh_datas():
    # Instanciate Mailing
    mailing = MailingEngine(config)
    # instanciate scraper engines
    seloger = SeLoger(config)
    pap = Pap(config)
    leboncoin = Leboncoin(config)
    
    # Append result
    mailing.mail_content += pap.scrap_data()
    # mailing.mail_content += seloger.scrap_data()
    # mailing.mail_content += leboncoin.scrap_data()

    if mailing.mail_content != '':
        mailing.notify_mail()
        print('Mail sent !')

if __name__ == '__main__':
    config = get_config()



if __name__ == '__main__':
    today = date.today()
    config = get_config()
    while today != config['GLOBAL']['end_date']:
        refresh_datas()
        print('[%s] Updated' % datetime.now().strftime("%H:%M:%S"))
        time.sleep(60 * 30)
        today = date.today()
