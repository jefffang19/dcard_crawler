import requests
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    headers = {
        'User-Agent': UserAgent
    }
    # url = 'https://www.dcard.tw/service/api/v2/posts?popular=true&limit=1'
    # url = 'https://www.dcard.tw/f/meme'
    url = 'https://www.dcard.tw/f/meme?latest=true'

    resp = requests.get(url, headers)

    # parsing
    soup = BeautifulSoup(resp.text, "html.parser")

    # get posts list
    result = soup.find_all("a", class_="sc-b57812c2-3 iwovon", limit=10)
    thumb = soup.find_all("div", {"class": "sc-28312033-3 bxrsoV"}, limit=10)

    # save
    if not os.path.exists('list.csv'):
        f = open('list.csv', 'w', encoding='UTF-8')
        f.write('topic,url,thumb\n')
        f.close()
    
    f = open('list.csv', 'a', encoding='UTF-8')

    for idx, r in enumerate(result):
        print(r)
        print(r.span.text)
        print(r['href'])
        print('thumb:', thumb[idx].text)
        print()

        f.write('{},{},{}\n'.format(r.span.text.replace(',', ''), 'https://www.dcard.tw' + r['href'], thumb[idx].text))

    f.close()
