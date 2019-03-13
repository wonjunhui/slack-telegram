# -*- coding: utf-8 -*-

import telegram
from datetime import datetime
from urllib.request import urlopen, Request
import urllib
import bs4

location = '대방동'
enc_location = urllib.parse.quote(location + '+날씨')
url = 'https://search.naver.com/search.naver?ie=utf8&query=' + enc_location
req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html, 'html.parser')
aa = '현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.'
bb = soup.find('dl', class_='indicator').text
now = datetime.now()
# now = str(now.year+'-'+now.month+'-'+now.day+now.hour+':'+now.minute)
now = '%s-%s-%s %s:%s' % ( now.year, now.month, now.day, now.hour,now.minute)

bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')
# chat_id = bot.getUpdates()[-1].message.chat.id
# chat_id = '516485771'
updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.
arr = []
for u in updates:   # 내역중 메세지를 출력합니다.
    print(u.message.text)
    print(u.message.chat.id + '+' + u.message.text)
    arr.append(u.message.chat.id)
    # chat_id = bot.getUpdates()[-1].message.chat.id  # 가장 최근에 온 메세지의 chat id를 가져옵니다

arr = list(set(arr))
print(arr)

bb = bb.replace('초','\n초').replace('오','\n오')
print(bb)
# try:
#     chat_id = bot.getUpdates()[-1].update_id
# except IndexError:
#     chat_id = 0

# for id in arr:
bot.sendMessage(chat_id='516485771', text=str(now) + '\n' + aa + '\n' + bb)
