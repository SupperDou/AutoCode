import requests, json, sys
import random,time

USER=sys.argv[1]
PASSWORD=sys.argv[2]
SCKEY=sys.argv[3]
url1 ="https://www.vikacg.xyz/wp-json/jwt-auth/v1/token"
header1 = {
'Host': 'www.vikacg.xyz',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
# 'Content-Length': '149',
'Origin': 'https://www.vikacg.xyz',
'Alt-Used': 'www.vikacg.xyz',
'Connection': 'keep-alive',
'Referer': 'https://www.vikacg.xyz/?variant=zh-cn',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'
}

data1 = {
'nickname'	:'',
'username':	USER,
'password':	PASSWORD,
'code'	:'',
'img_code':	'',
'invitation_code':	'',
'token':	'',
'smsToken':'',
'luoToken':	'',
'confirmPassword':	'',
'loginType'	:''
}

vex=requests.session()
#
response=vex.post(url1,data1,headers=header1)
#
# response.content.decode("utf-8")
# r1 = json.loads(response.text)
# cookies=response.cookies.get_text()
# r1=response.content.decode("utf-8")
# print('响应{}'.format(response))
token=requests.utils.dict_from_cookiejar(vex.cookies)['b2_token']


header2 ={
'Host': 'www.vikacg.xyz',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding': 'gzip, deflate, br',
'Authorization': 'Bearer '+token,
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '16',
'Origin': 'https://www.vikacg.xyz',
'Alt-Used': 'www.vikacg.xyz',
'Connection': 'keep-alive',
'Referer': 'https://www.vikacg.xyz/user/194980',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'TE': 'trailers'
}

header3={

'Host': 'www.vikacg.xyz',
# 'content-length': '0',
'accept': 'application/json, text/plain, */*',
'Authorization': 'Bearer '+token,
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
'origin': 'https://www.vikacg.xyz',
'x-requested-with': 'mark.via',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.vikacg.xyz/mission/today',
# accept-encoding: gzip, deflate
'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

data2 ={
'count':	"10",
'paged'	:"1"
}

data3={

}

url3 = "https://www.vikacg.xyz/wp-json/b2/v1/userMission"
response1=requests.post(url3,data=data3,headers=header3)
#
response1=json.loads(response1.text)
# # # # print(response1)



num=0
while (num<2):

    id = random.randint(20008, 21008)

    header4 = {
        'Host': 'www.vikacg.xyz',
        # 'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'Authorization': 'Bearer ' + token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'origin': 'https://www.vikacg.xyz',
        'x-requested-with': 'mark.via',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.vikacg.xyz/user/' + str(id),
        # accept-encoding: gzip, deflate
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data4 = {
        'user_id': id
    }
    url4 = "https://www.vikacg.xyz/wp-json/b2/v1/AuthorFollow"


    response4 = requests.post(url4, data=data4, headers=header3)
    # response4=json.loads(response4.text)
    response4 = response4.text
    if response4 == 'true':
        print('关注')
        num+=1
    elif response4 == 'false':
        print("取关")
    else:
        print('错误')
        break
    print(num)
    time.sleep(5)

if num==2:
    string='关注完成'
else:
    string='关注错误'

print(response1+string)
requests.post(f'http://sc.ftqq.com/{SCKEY}.send', {"text": response1+string, "desp": '不会变魔术的安娜'})
