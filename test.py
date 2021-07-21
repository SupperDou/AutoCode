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
r1 = requests.request("post", url1, json=data1, headers=header1)
r1 = json.loads(r1.text)
uuid = r1['id']
print(uuid)
