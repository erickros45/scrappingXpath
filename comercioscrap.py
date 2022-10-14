from tkinter import W
from urllib import response
import requests
import lxml.html as html 
import os 
import datetime


HOME_URL = 'https://www.elcomercio.com'

XPATH_LINK_TO_ARTICLE = '//h3[@class="article-highlighted__title"]/a/@href'
XPATH_TITLE = '//h1[@class="entry__title"]/text()'
XPATH_SUMMARY = '//div[@class="col-md-11"]/p/text()'
XPATH_BODY = '//div[@class="entry__content pw-ctt"]/p//text()'


def parsed_link(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice= response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title= parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','').strip()
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body= parsed.xpath(XPATH_BODY)
                #print(body)
                #body = body.replace('<strong>', '').replace('</strong>', '')

            except IndexError:
                return

            
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    if p.endswith('.'):
                        f.write(p)
                        f.write('\n')
                    else: 
                        f.write(p)
                f.write(link)
                
        else:
            raise ValueError(f'Error: {response.statuscode}')
    except ValueError as ve:
        print(ve)



def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode("utf-8")
            parsed = html.fromstring(home)
            link_to_notice=parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(link_to_notice)
            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in link_to_notice:
                parsed_link(link, today)

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)



def run():
    parse_home()

if __name__ == '__main__':
    run()