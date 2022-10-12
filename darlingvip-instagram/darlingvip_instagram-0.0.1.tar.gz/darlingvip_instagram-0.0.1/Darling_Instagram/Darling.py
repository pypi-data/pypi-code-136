import string
import requests, json, random, os
from datetime import datetime
import json

class DarlingInstagram:
    def __init__(self, cookie: str):
        self.cookie = cookie
        self.xcsrftoken = cookie.split("csrftoken=")[1].split(';')[0]
        try:
            headers = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
            }
            post = requests.get("https://www.instagram.com/", headers=headers).text
            self.idProfile = post.split('''"viewerId":"''')[1].split('"}')[0]
            self.x_instagram_ajax = post.split('''rollout_hash":"''')[1].split('",')[0]
            self.appId = post.split('''"appId":"''')[1].split('","')[0]
            self.headersApi = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
            }
        except:
            print('SAI COOKIE RỒI BẠN ƠI | COOKIE NOT VALID')
            quit()
    def UploadPost(self, img_path: str) -> bool:
        try:
            upload_id = int(datetime.now().timestamp())
            url_load_img = "https://i.instagram.com/rupload_igphoto/fb_uploader_{}".format(upload_id)
            headers = {
                'content-type': "image/jpeg",
                'cookie': self.cookie,
                'offset': "0",
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-entity-length': str(os.path.getsize(img_path)),
                'x-entity-name': "fb_uploader_{}".format(upload_id),
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
                'x-instagram-rupload-params': f'{{"media_type":1,"upload_id":"{upload_id}","upload_media_height":780,"upload_media_width":780}}',
            }
            data = open(img_path, "rb")
            requests.post(url=url_load_img,data=data, headers=headers).json()
            url_up_post = "https://i.instagram.com/api/v1/media/configure/"
            data = {
                'source_type': "library",
                'caption': "QUANGDEPTRAI",
                'upload_id': upload_id,
                'disable_comments': "0",
                'like_and_view_counts_disabled': "0",
                'igtv_share_preview_to_feed': "1",
                'is_unified_video': "1",
                'video_subtitles_enabled': "0"
            }
            if proxy != None:
                up_post = requests.post(url = url_up_post, headers = self.headersApi, proxies=self.proxyDict).json()
            else:
                up_post = requests.post(url = url_up_post, headers = self.headersApi, data = data).json()
            if up_post['status'] == "ok":
                return True
            else:
                return False
        except Exception as e:
            return False
        
    def UploadProfilePicture(self, img_path: str) -> bool:
        headers = {
            "Host": "www.instagram.com",
            "User-Agent": f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.instagram.com/pedro_lobito/",
            "X-CSRFToken": self.xcsrftoken,
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": str(os.path.getsize(img_path)),
            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie": self.cookie
        }   

        files = {'profile_pic': open(img_path,'rb')}
        values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg",
        "Content-Type": "image/jpeg"}

        set_avt = requests.post("https://www.instagram.com/accounts/web_change_profile_picture/", files=files, data=values, headers=headers).json()
        if set_avt['has_profile_pic'] == True:
            return True
        else:
            return False
    def FollowUser(self, user_url: str) -> bool:
        try:
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
            }
            user_profile = requests.get(user_url,headers=headers).text
            user_uid = user_profile.split('"profile_id":"')[1].split('"')[0]
            follow = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{user_uid}/follow/',headers=headers)
            return "Success"
        except:
            return False
    def LikePost(self, url_post: str) -> bool:
        try:
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': self.xcsrftoken,
            }
            ig_post = requests.get(url_post,headers=headers).text
            uid_post = ig_post.split('media_id":"')[1].split('"')[0]
            like = requests.post(f'https://i.instagram.com/api/v1/web/likes/{uid_post}/like/',headers=headers)
            return True
        except:
            return False
    def comment_post(self, url_post: str, content: str) -> bool:
        try:
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': self.xcsrftoken,
            }
            ig_post = requests.get(url_post,headers=headers).text
            uid_post = ig_post.split('media_id":"')[1].split('"')[0]
            data = f'comment_text={content}'
            comment = requests.post(f'https://i.instagram.com/api/v1/web/comments/{uid_post}/add/',headers=headers, data=data)
            return True
        except:
            return False

    def UnfollowUser(self, user_url: str):
        try:
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-csrftoken': self.xcsrftoken,
            }
            user_profile = requests.get(user_url,headers=headers).text
            user_uid = user_profile.split('"profile_id":"')[1].split('"')[0]
            unfollow = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{user_uid}/unfollow/',headers=headers)
            return True
        except:
            return False




