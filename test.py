import requests, json, sys

username=sys.argv[1]
password=sys.argv[2]
# 登录抓包
url1 = "https://www.vikacg.com/wp-json/jwt-auth/v1/token"
header1 = {
'Host': 'www.vikacg.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '149',
'Origin': 'https://www.vikacg.com',
'Proxy-Authorization': 'Basic LnN2QDMyODQyMjc7Y24uOjYrL285ZThhOUpJME8vK0dNNXJIM284di9FZXFVVHUvalpkSUF0N3o5MGs9',
'Connection': 'keep-alive',
'Referer': 'https://www.vikacg.com/',
'Cookie': '_ga=GA1.2.1399209464.1588809352; _ga_6BRRXJ5S7F=GS1.1.1626839893.28.1.1626840144.0; _ga_801TFF6N89=GS1.1.1626839893.28.1.1626840144.0; wpcc_variant_f43f0782b8316b4e5ae70619d05a28eb=zh-hans; Hm_lvt_49cc02c62fdb09c867c9340508d5af34=1600393511,1600439469,1601120773,1601258134; __gads=ID=852b8adc87f3efd2:T=1596793142:S=ALNI_MaOkhTCpfeB5K2yFSrUesVkag-wOg; _ga_0EBQJT2CGX=GS1.1.1626839893.4.1.1626840144.0; allow_primary=true; _gid=GA1.2.915180452.1626779313; wpdiscuz_hide_bubble_hint=1; gg_info=1626840136',
'Cache-Control': 'max-age=0',
'TE': 'Trailers'

}
data1 = {

'nickname'	:'',
'username':	username,
'password':	password,
'code'	:'',
'img_code':	'',
'invitation_code':	'',
'token':	'',
'smsToken':'',
'luoToken':	'',
'confirmPassword':	'',
'loginType'	:''
}
response = requests.request("post", url1, json=data1, headers=header1)
print(response.encoding)
response.encoding = 'utf-8'
print(response)
# print(r1.text)
# r1 = json.loads(r1.text)
# uuid = r1['id']
# print(uuid)
