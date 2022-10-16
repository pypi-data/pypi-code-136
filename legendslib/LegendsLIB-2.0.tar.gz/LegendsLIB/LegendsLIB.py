try:
	import requests
	from user_agent import generate_user_agent
	import hashlib
	import os
	import instaloader
	import json
	from uuid import uuid4
	import uuid
	import random
except ModuleNotFoundError:
	import os
	os.system("pip install instaloader")
	os.system("pip install user_agent")
	os.system("pip install uuid4")
try:
	import requests  ,re, os , sys , random , uuid , user_agent , json,secrets
	from uuid import uuid4
	from user_agent import generate_user_agent
	
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	
class login:

	def Insta(user,password):
		uid = uuid4()
		agents =["Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)"]
		agent = random.choice(agents)
		url = "https://i.instagram.com/api/v1/accounts/login/"
		
		headers = {
    "Content-Length": "278",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": agent,
    "Cookie": "ds_user_id\u003d54081338738; mid\u003dYrzWBwABAAHGbxxkzuC2P5KGdlwp",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG, en-US",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
        
		data = {
		'uuid':str(uuid4()),
		'password':password,
		'username':user, 
		'device_id':str(uuid4()),
		'from_reg':'false', 
		'_csrftoken':'missing', 
		'login_attempt_countn':'0'}
		
		login = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
		
		if str("logged_in_user") in login.text:

			
			return True
			
		if str('"message":"challenge_required","challenge"') in login.text:
			
			return False
			
		else:
			
			return 'No'
	def Face(user,password):
		uid = uuid4()
		requests.urllib3.disable_warnings()
		url = "https://b-graph.facebook.com/auth/login"
		headers = {
		"authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
		"user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; BLA-L29 Build/HUAWEIBLA-L29S) [FBAN/MessengerLite;FBAV/305.0.0.7.106;FBPN/com.facebook.mlite;FBLC/ar_PS;FBBV/372376702;FBCR/Ooredoo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/BLA-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2040};]"
	}
		data = f"email={user}&password={password}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id={uid}&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"
		response = requests.post(url, data=data, headers=headers, verify=False, timeout=15).json()
		if list(response)[0] == "session_key":
			return True
		else:
			try:
				return False
			except:
				return False
	
	def Twiter(user,password):
		url="https://twitter.com/sessions"
		data={'redirect_after_login': '/',
      'remember_me': '1',
      'authenticity_token': '10908ac0975311eb868c135992f7d397',
      'wfa': '1',
     'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
     'session[username_or_email]': user,
     'session[password]': password}
		headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
      'Content-Length': '901',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
      'Host': 'twitter.com',
     'Origin': 'https://twitter.com',
     'Referer': 'https://twitter.com/login?lang=ar',
     'TE': 'Trailers',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': generate_user_agent()}
		req = requests.post(url,headers=headers,data
 =data)
		if ("ct0") in req.cookies:
			return True
		elif ("error") in req.text:
			return False
class A7X:
	def get_bin():  	
	    d = ('1234567890')
	    f = random.choice(d)
	    g = random.choice(d)
	    haa = random.choice(d)
	    has = random.choice(d)
	    star = (f'48{f}{g}{haa}{has}')
	    return star
	def check_bin(bin):
	    url = f"https://lookup.binlist.net/{bin}"
	    resp = requests.get(url).json()
	    return resp
	def info(user):
           try:
               try:
                   
                   email=user+'@gmail.com'
                   hdo = {'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
                   inpho=requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hdo).json()

                   bio=inpho['data']['user']['biography']
                   privo=inpho['data']['user']['is_private']
                   name=inpho['data']['user']['full_name']
                   IDN=inpho['data']['user']['id']
                   folows=inpho['data']['user']['edge_followed_by']['count']
                   folow=inpho['data']['user']['edge_follow']['count']
                   img1=inpho['data']['user']['profile_pic_url']
                   img=requests.get(f"http://tinyurl.com/api-create.php?url={img1}").text
                   rey = requests.get(f"https://o7aa.pythonanywhere.com/?id={IDN}")   
                   ree = rey.json()
                   date = ree['date']
                   urrlr='https://www.instagram.com/accounts/account_recovery_ajax/'
                   headdr= {
             'accept': '*/*',
             'accept-encoding': 'gzip, deflate, br',
             'accept-language': 'en-US,en;q=0.9',
             'content-length': '336',
             'content-type': 'application/x-www-form-urlencoded',
             'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
             'origin': 'https://www.instagram.com',
             'referer': 'https://www.instagram.com/',
             'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
             'sec-ch-ua-mobile': '?0',
             'sec-fetch-dest': 'empty',
             'sec-fetch-mode': 'cors',
             'sec-fetch-site': 'same-origin',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
             'viewport-width': '30',
             'x-asbd-id': '437806',
             'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
             'x-ig-app-id': '936619743392459',
             'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
             'x-instagram-ajax': 'caee87137ae9',
             'x-requested-with': 'XMLHttpRequest'
      }
                   dataro={
       'query': f'{email}',
               'ig_sig_key_version': '4',"user_id":IDN
      }
                   rq = requests.post(urrlr,headers=headdr,data=dataro).json()
                   try:
                     B19 =f"{email}"
                     fa =str(rq['options']['can_use_facebook'])
                     if fa =='True':
                      facebook = 'Linked Facebook'
                     else:
                      facebook='Not Linked '
                      ph = str(rq['options']['can_send_phone'])
                      if ph =='True':
                       numpho = ('true phone')
                      else:
                       numpho='false phone'
                   except KeyError as Error:
                    facebook ='not work'

                   headerros = {
        # 'Content-Length': '305',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
        # Requests sorts cookies= alphabetically

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
        # 'Accept-Encoding': 'gzip',
       }
                   datada = {
        'ig_sig_key_version': '4',
        "user_id":IDN
       }
                   reso = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headerros, data=datada).json()
                   rest =str(reso['obfuscated_email'])
                   AMT={  "Name" : name , "User" : user , "Email" : email ,"ID" : IDN , "Followors" : folows ,"Followers" : folow , "Facebook" : facebok , "Phone_Number" : numpho ,"Privacy" : privo , "Date" : date , "Reset" : rest , "Bio" : bio , "BY" : "@Alaa7X ~ @C_2_9"  }
                   return AMT
               except:
               	AMT1={  "Name" : name , "User" : user , "Email" : email ,"ID" : IDN , "Followors" : folows ,"Followers" : folow , "Privacy" : privo , "Date" : date ,  "Bio" : bio , "BY" : "@Alaa7X ~ @C_2_9"  }
               	return AMT1

           except:
           	return 'no'
	def rest(email):
		try:	
			uid = uuid4()
			agents =["Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)"]
			agent = random.choice(agents)
			url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
			headers = {
	    "Content-Length": "317",
	    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
	    "Host": "i.instagram.com",
	    "Connection": "Keep-Alive",
	    "User-Agent": agent,
	    "Cookie": f"mid={uid}",
	    "Cookie2": "$Version\u003d1",
	    "Accept-Language": "ar-EG, en-US",
	    "X-IG-Connection-Type": "MOBILE(LTE)",
	    "X-IG-Capabilities": "AQ\u003d\u003d",
	    "Accept-Encoding": "gzip"
		}
			data = {
	"ig_sig_key_version":"4",
	"user_email":email,
	"device_id":uid,
	"guid":uid,
		}
			req = requests.post(url,headers=headers,data=data)
			if req.json()["status"]=="ok":
				return True
			else:
				return False
		except:
			return False
	def call(number):
		if "+2011" in number or "+2010" in number or "+2012" in number or "+2015" in number or "2011" in number or "2010" in number or "2012" in number or "2015" in number:
			url = "https://accept.paymob.com/api/auth/register/phone_number_signup?gclid=EAIaIQobChMI-I2_jqP-9wIVk5BoCR01LwnOEAAYASABEgLY_PD_BwE"
			data = {
  "phone_number":number,
  "country_code": "EGY",
  "phone_country_code": "+964",
  "dashboard": "true"
}
			req = requests.post(url,data=data)
			if req.json()["message"]== "This phone number was already registered but not verified. Otp sent for verification." or "Account registration successful":
				return True
			else:
				return False
class mails:
	def gmail(email):
		
		url = 'https://android.clients.google.com/setup/checkavail'
		headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
		data = json.dumps({
		'username':str(email),
		'version':'3',
		'firstName':'ALAAPTO',
		'lastName':'modalloka'
	})
		res = requests.post(url,data=data,headers=headers)
		if res.json()['status'] == 'SUCCESS':
			
			return True
		
			
		else:
			
			return False
			
		
			
	def hotmail(email):
		
		url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
		
		headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": str(generate_user_agent()),
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		
		data = ""
			
		res = requests.post(url, data=data, headers=headers)	
		if ("Neither") in res .text:
			
			return True
		
		else:
			
			return False
		
		
        
    
    
	def outlook(email):
		
		url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
		
		headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": str(generate_user_agent()),
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		
		data = ""
		
		res = requests.post(url, data=data, headers=headers)
		
		if ("Neither") in res.text:
			
			return True
		
		else:
			
			return False
		
		
			
	def mailur(email):
		
		url = "https://account.mail.ru/api/v1/user/exists"
		
		headers = {
		"User-Agent": str(generate_user_agent())}
		
		data = {'email': str(email)}
		
		response = requests.post(url, data=data, headers=headers)
		
		if str(res.json()['body']['exists']) == False:
			
			return True
		
		else:
			
			return False
		
		
		
	def yahoo(email):
		
		if "@" in email:
			email = email.split("@")[0]
		else:
			pass
		
		url = "https://login.yahoo.com/"
		head = {
		"User-Agent": str(generate_user_agent()),
		"Pragma": "no-cache",
		"Accept": "*/*"}
		reqs = requests.get(url,headers =head).text
		crumb = reqs.split('name="crumb" value="')[1].split('" />')[0]
		acrumb = reqs.split('name="acrumb" value="')[1].split('" />')[0]
		
		
		url = "https://login.yahoo.com/account/module/create?validateField=userId"
		
		headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '7423',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'PH=l=en-JO; cmp=t=1649967133&j=0; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUVM0Uk1FNVM1NTdEQlg2TTdOVFFRUTdHTlUiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJERWI2ZmRZN1BwQVUifX0.qS4v0LTtpXd4vhydwS6vpL9MANSOMDMZEYWffFSxshbnuwRCzeUzJbwM2p7nPMwYV96yEFCkM0B8Lo--XHoBQvQszdP_-M-HuzLttwUwkzkqDpZyo6Lzm5bAnbh6B3P-kTcNBHlCoSg9N-SExB0OrppOO2gONQqoR25mLHXhhnY; A1=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8; A3=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8; B=e62dbv5gv8d0u&b=4&d=6ZQJIRhtYFgpJyr7JyZD&s=1a&i=0ME7ntmY2gMEOPVdtKL3; GUC=AQEABgJiWdBjM0Id8gRd; FS=v=1&d=Sloq608oHDIvM2JuXcI4Gn9LK3_mICxQM3wH9IpTUuhixjO_VCNu~A; F=d=Gd70Kyk9vQ--; A1S=d=AQABBB409GECEJnQ0nfMctyiH6Cq-PmrCeMFEgEABgLQWWIzY2Jcb2UB_eMBAAcIHjT0YfmrCeMID9DBO57ZmNoDBDj1XbSi9wkBBwoB3w&S=AQAAAjb2LJb55ay2ij3P5hQhTG8&j=WORLD; AS=v=1&s=Cgvhb3Xg&d=A627bc5c4|SI2GnZf.2Sr3BNg89zpo_CsNpKuGFl4HUY7VHVfbraWyc8Ii93qDVlDfOt1BfiR7XCEZ21NvQDWrQraqbYJyOJYpsIH0OvCsxXiN8AGzuKcqHrgfGUtOZZrzS7O.VkvbdCiSNYD_w9OB6ML3Y8NMOiMYT_MiAgefNsF_54dXFyJdm4rdq1W.bJhN_PLPvnrKNDEd7saaFV3TnLk.b.kYolEgMoWWAkD71Of5UCjkqQNaQk8RIunPxxXkRXHZwr1ypRWsnBEuqv5oQrEDCiqHFvF8u25Ofg2gKdnPDbFeJ9RleaTB45uuY5sZUv1mdsokSKD6_ahRvGkWfTnrPZzt6E28PE28s0fooo2qY3yUltuO1w.xKUCKkKbWJQyjxXpqTm3hgOwJ66.3I2TIf5r0vA0r43pnZVLl2rttIk4R1ABgy9Wy7OOqga8ZVE3o1l0hHz419cDgN1Hzb0Fexz..nP9ME4F7VWfn8oo.k9pMZYDtHhRMM1kGGmsex0pBbD.QdtUhpuVR4oHP_U7ap4DOcKCGYp2XVml6Z.9xRcb3m_VOukhZ1zwEpcjT6xXJAjZ7AgfC3l7QBLw2NnD0Mtuqh35qDDEABh4dM.YlhgT72EYqSbl8MnvZ7W1q0bk3SMaqQdwbAGle4W1j_uPr0yu90HSPNKzeQ2K5GsPumTtVNzT353rVPBfwGAIDMe1wqR5csd8SV4iFjZ8Y6r..RZT_XsKxT2JOL1QhaTFkx0INLwy88kv._Vv_cBMwcEYUz0LQ9OLwajl6R7b5AYwwk.B4EXpf7DzynJaWtaerDs461oLGbqD_ljVUdWAy.U5mcYXnWqzqseI7fC6W4HvXdAaCIC2qmrAgjow9hJqXDIvkXODlsrZ.usoNnX44L7X8ybtYCKvH4RcQttBv6b0X2jcI~A|B627bc602|8.xHz7z.2TpHZLxVO1hodGUaeVUeU4gERiIt7J2uXM7cv4.YcovtTNaxgcIeRQzeGiqrbxcu1WyDHogAGcIglonu5OSTNDoMeCDAxtZH1Od166YwYdZDIzr0hcNc_epXkOw1KoLhXbyBR5MCTGhdrG0BJoG5njJC9n5N2JJx2P0aWBC9bPoIThLWGi9Wf8wfI4MP3mhqA9lF2eFUkQEX6A2CiocpPLhQbmtgRKbVM1Q3ncBSeVaKuhQOqNcvHOqCSLgppcJg2sBtkJLzet12UCSy8JORfHf6Dc3DMT8QgifRRoGTBoAGs_SOI6hOcNExCo9D5ImvN.lKHPMymFxqnW4pVaq2PBcY7f2t4xNLcqBYPV.O2TCmgvni7WYaq7A0zYaQCJWFcBkzB4BcXX19s8Eeidj213exUfkBq8zgrPQsB0IPQD0KCe.LXf6hNY1dr4vp1rTBLRchdHhzbM2upz50JIDW87taVyq.ZU04zTTOg4KQwv9Hn9poWN_Y2VeiU68nclbo60iQRPXCa5mqucblBHNAxUHuGNiUlD5xYj3N2W.oiUMs7_9esA3eOUubDjN8vj_FAqE9IKrJqNiyOkWOniHFTJ77toR.uk1PW8Bo21lZocUzsa1s9WdzLC5HusiiMErYDEnMdRIyu8_.ZxCeKhvNbi8cbSI3.ZentJbZMr1y5sZrarxJCGi1OGoUBEuHWbaZsRASqKJMiX4I95kvg.aFU6XlIQCbKbVyJPCnf7lMb0bEsP6oYnEiqlME_r8ejtGRi9Nu1vgt5HvJaEjwOlYHZnmO21kqttxWUkhORs_He7F81_HHtWVAez1R6a2WP3qh1MT14ppKSBr6851gallOGB0AJOi2P.9vJaPSwzunhCFzWdpgLH9rx4LTKgseKH1NLyrsvKnmf.AMPdYnZR1NBJSvBJ9kknOWSXWyNFcfOgVyUaHzJKMG.QF.JC3DqEcIsJCW7w12wCyb422YcTwgWhUK1I19S8w9HjhiYg--~A',
		'origin': 'https://login.yahoo.com',
		'referer': 'https://login.yahoo.com/account/create?.intl=xa&.lang=ar&src=ym&specId=yidregsimplified&activity=mail-direct&pspid=959521375&.done=https%3A%2F%2Fmail.yahoo.com%2Fm%2F%3F.intl%3Dxa%26.lang%3Dar&done=https%3A%2F%2Fmail.yahoo.com%2Fm%2F%3F.intl%3Dxa%26.lang%3Dar&intl=xa&context=reg',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': str(generate_user_agent()),
}
		
		data = {
	    'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":4,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":48,"hash":"62d5bbf307ed9e959ad3d5ad6ccd3951"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1652192386973,"render":1652192386434}}',
	    'specId': 'yidregsimplified',
	    'crumb': str(crumb),
	    'acrumb': str(acrumb),
	    'userid-domain': 'yahoo',
	    'userId': str(email),
	    'password': '@GDOTools',
}
		
		res = requests.post(url,headers=headers,data=data).text 
		
		if ('"userId"') in res:
			
			return False
		
		else:
			
			return True




	def aol(email):
		
		if "@" in email:
			email = email.split("@")[0]
		else:
			pass

		url = 'https://login.aol.com/account/module/create?validateField=yid'
		
		headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '18023',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': 'A1=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU; A3=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU; A1S=d=AQABBGBeeWICEBR5epkCARe46kFw6ViOQ_AFEgEBAQGvemKDYgAAAAAA_eMAAA&S=AQAAAp3JQ6CyW2qRJcMsBzHGVvU&j=WORLD; GUC=AQEBAQFieq9ig0IfzwR5; rxx=2bkczirpbih.2q6rpdsb&v=1; AS=v=1&s=JYNxcuAB&d=A627ab0eb|5n7NNlX.2Tqja_1ZC6lprFtAflUVdSswdgLRxIPQFqE9yPLfNXNQGllEgjcaz2MSyNOF0HA9XirM0hGhPu6hRyuyv6NS5uzzU2MRaRQf.1YBAQ8FypG1m_xQXAtuSInDrAwsMOptRW4zfkTgorDT4mTAhLg6RTvtz.RlGfCdtaQ4BBDOfp7jAYaYk.VJlzoY75HEqitjywIRo5cxa2LE6o5SUyxNOi7S_X3k_SPXAVdV.Pie3M8oZSqscWmfYaFDf586bpqdXlRbtd9NfqqCnsm39F_qAPBPvWHWieu4eZ4Guhk.MRMp7Daew_rlTFks0DO5LZYOCyO3RrW3LO3QaHRTvTBTaXP4RsdfXTOXPejofBwqmWSbUlACa4xD1EKndabLWQmEoy1AEUMoSbwgJMxI_j7xuQHqBgjCanjm8A6GOXCZKM44DjwdQdaMnR6GrHEfBfKds9z.7gjHKBoZ2jkWj7Hk7hPMzDGRBkqU.TWCGZRumYVYV8blYxEIS.H9qySKbh3SBBI8MIgkMqBNciHX3QnqQrc_CuA1uBOx7GHKgnI7pemzJnVMGwyYsAGU4UQRwAVGcDrHZH76hH..grS5ceMIZJSVt6nAcvYiTMElRUgLqk4RORTkyF9XbLMB9_U2I_ZVaERHP3X7j7f77RdHq2UlR68eZ_G5RY6ZrgfwFvy1Ptrd9WdFYaab69sfGI8SVXk2dtdR5udVorhaBdtoNxJ5PIy0Ue_qMPhxcsw4VzSExlyyNSaF0SFoSH5fK8kFVQ0IIBIWO_d0ik6d9azkHxffaa7MJpjYfsHmHpERb2hEkyr7uJzTQTf0H8NBfQdcQD8P9ja69DD7Ahdacge_a9D4QGaLgMvQi481iZMNd5Dy46uoeco5T.slB_psK4WxbBJgP7p6hgyb_wkDzvUhd_3ym5sQe1cBySzHgXSMyzsEurBQZKaMHv9302Cj6iNUZ2jjtMkAVdsh~A|B627ab2cd|x0gk8rH.2TpbbztShpG57nIccQOKaEGxqulmFIimnSbIetxQBy35pQAyeLh0g4kZXfUcZ8gS0KtJhnntdd169n74ag_k2YnldeTcAixJ8Oe1U9eEwr4TEKjAn5ew0omTSMojewjLD76vbkEv.zZYyCrRxd5vfs3vmQxAV_f6Y0sOWtsUeIu3OvEzUyK.1trUfGvmn7d3hvyFbF.OTRqd._NMsXRn2QVZ.T5RjYrog5983WaKy_9x1YPoBUNH4QPKi0zZBP9iMgx8Tlsrxhn4zs9Zyr3IiqPFbxjEuBh4G78xoEv7z6_PrYOwB37XEbTdaaeXyPFsSGhZf4bQovQopXVbHe.9nbDzDYkfdXD6d9wmf6jvSEex9a9eEu8Z.14NuIQZJcy_c6_PP5H0eXQAWO6LOsW7CtqdeDlLd74M9jUU5yseMxzkN0HSawwGQ.HU.XZFjoOjowHAX1bsDGRuWObSamI1LdvanTCHZZ6TICNO8lT9GjBWDYK.h6.ojgs.tCAAXzYPMf6UOHvrjtlwaCmODGFlndZMASPIp9IyDMRT9gC52spPRpBQJZOpJUt8YDEY6zKB5r2SsHH.ssGgtrnS3tlCg6rx8k.wEakhoSpj2ezEMO4IAODDXV0paODum6McXkpaxliXReHLYdtXIM9t5smt_PeP92ttd69oDB.zVFsEms7tdF1SQWbmUF.4plddWEwfn6FNVdj7TpJvpTAxjaso_xliccUrnkpUGvH1IUv11w4Pok0k92JLzk2AXJ5Ak_5R51n2X_Oc88nJKif3EZK7ly7lgMXtWaURJx2Zj4.88SxdyHNtRzmHFvkAwmxtDmjgj5OCF7m38h.4TZuT3.D3c7uhs0XPEZARricsnApvw1dUBRY0E3vvSU.S_4zHPhWn7BHQz1nySvei.tQaogRmeBpFHvzS3QNKSWksRu1w7T8O2RDtnr7pzs5VzPifkiXOKw--~A',
		'origin': 'https://login.aol.com',
		'referer': 'https://login.aol.com/account/module/create?validateField=yid%5C',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': str(generate_user_agent()),
		'x-requested-with': 'XMLHttpRequest',
}

		data = {
		'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":4,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":48,"hash":"62d5bbf307ed9e959ad3d5ad6ccd3951"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1652124464147,"render":1652124464497}}',
		'specId': 'yidReg',
		'crumb': 'YLO.LxuwQbD',
		'acrumb': 'JYNxcuAB',
		'done': 'https://www.aol.com',
		'tos0': 'oath_freereg|us|en-US',
		'yid': str(email),
		'password': '@GDOTools',
		'shortCountryCode': 'US',
	}
		res = requests.post(url,headers=headers,data=data).text 
		
		if ('"yid"') in res:
			
			return False
			
		else:
			
			return True