import requests
from bs4 import BeautifulSoup

from slacker import Slacker

token = 'xoxb-547158836709-554963956854-Vk1zIjAmBfk9RPOhRtouegyZ'
slack = Slacker(token)
# slack.chat.post_message('#slack_test', 'python')

# req = requests.get("http://www.fnnews.com/news/201902110937317318", verify=False) #connection
req = requests.get("https://finance.naver.com/sise/sise_low_up.nhn",
                   verify=False)
# req = requests.get("http://datalab.naver.com/keyword/realtimeList.naver?where=main")
html = req.text  # naver에서 소스를 받아오기

# BeautifulSoup로 html 소스를 python 객체로 변경할 수 있다.
#  첫 인자에는 html 소스코드를 가져온다. 두번째 인자에는 어떤 parser를 이용할지 정해준다.
# ---------------------------------------------------------#
# python 내장 함수 html.parser
# soup = BeautifulSoup(html.read()).find("div", {"id": "ad_body"})
soup = BeautifulSoup(html, 'html.parser')
sammies = soup.find("div", {"class", "box_type_l"})
arr = []
arr2 = []
for tr in range(2,15):
    # print(tr)
    aa = sammies.findAll('table')[0].findAll('tr')[tr]
    arr.append(aa)

# 등락률 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[1].text.replace(' ','') #등락률
# 등락률_숫자 = sammies.findAll('table')[0].findAll('tr')[6].findAll('td')[1].text.replace(' ','')
#
# 종목명 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[2].text.replace(' ','') #종목명
# 종목명_숫자 = sammies.findAll('table')[0].findAll('tr')[2].findAll('td')[2].text
#
# 현재가 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[3].text.replace(' ','') #현재가
# 현재가_숫자 = sammies.findAll('table')[0].findAll('tr')[2].findAll('td')[3].text
#
# 전일비 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[4].text.replace(' ','') # 전일비
# 전일비_숫자 = sammies.findAll('table')[0].findAll('tr')[2].findAll('td')[4].text.replace(' ','').replace('\n','').replace('\t','')
#
# 등락률2 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[5].text.replace(' ','') #등락률
# 등락률2_숫자 = sammies.findAll('table')[0].findAll('tr')[2].findAll('td')[5].text.replace(' ','').replace('\n','').replace('\t','')
#
# 시가 = sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[6].text.replace(' ','') #시가
# 시가_숫자 = sammies.findAll('table')[0].findAll('tr')[2].findAll('td')[6].text.replace(' ','').replace('\n','').replace('\t','')
total_str = ''
count = 1
for a in arr:
    try:
        print('------------' + str(count) + '------------')
        # print(arr[8])
        total_str = '------------' + str(count) + '------------' + '\n'

        for b in range(2, 6):
            # print(arr[a].findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t',''))
            # exit()
            # print(sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[b].text.replace(' ', '').replace('\n','').replace('\t', ''))
            # print(a.findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t',''))
            total_str = total_str + sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[b].text.replace(' ', '').replace('\n','').replace('\t', '')+": "+a.findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t','')+'\n'
            # print(total_str)
            # print(sammies.findAll('table')[0].findAll('tr')[0].findAll('th')[b].text.replace(' ', '').replace('\n','').replace('\t', ''))
            # name = name+ ": "
            # print(a.findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t',''))

            # print(a.findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t',''))
            # print(sammies.findAll('table')[0].findAll('tr')[a].findAll('td')[b].text.replace(' ','').replace('\n','').replace('\t',''))
        arr2.append(total_str)
        count = count+1
    except Exception as e:
        print("ㅎㅎ:"+str(e))
        # count = count+1
print(arr2)
slack.chat.post_message('#slack_test', ''.join(arr2))

exit()

