import pickle

import cloudscraper
import colorama
import json
import time
import datetime
import os
from termcolor import colored
import random, bs4
from requests.utils import cookiejar_from_dict as jar
import os, requests
import sys
from tinydb import TinyDB, Query,where
from cryptography import fernet

encryption_key = b'tUvzG-BWuh2xQB1k4VKynl4ox_2k9VHCMjRe4-UOQgA='
User = Query()

colorama.init()

db = TinyDB('database.json')


class MainBot:
    def __init__(self):
        self.win_instance =None

        self.status=""

        self.hashtags=[]
        self.target_usernames=[]

        self.comments=[]

        self.obtained_users_posts={}

        self.stop_running_bot=False

        '''change this to 1000'''

        self.max_likes = 1000
        self.max_comments = 200

        self.liked_today = 0
        self.comment_today = 0
        self.now = datetime.datetime.today()

    def login_user(self,username,password,db_connector):

        colorama.init()
        self.cookies_expired = False

        self.db=db_connector

        credentials = self.db.search(User.credentials == 'true')

        if credentials:
            # print(credentials)
            encrypt_creds = fernet.Fernet(encryption_key)

            decrypt_credentials = credentials[0].get("encrypted").encode()
            cookies = encrypt_creds.decrypt(credentials[0].get("login_cookies").encode())

            decrypt_cryptography = encrypt_creds.decrypt(decrypt_credentials)
            decrypt_pickle2 = pickle.loads(decrypt_cryptography)
            self.username = decrypt_pickle2.get("username", "specify a username")
            self.password = decrypt_pickle2.get("password", "specify a password")

        else:
            self.username = username
            self.password = password
            cookies = None

        '''if they have the cookies file use it'''

        liked_ = self.db.search(User[f"{self.username}_date_today"] == str(self.now).split(" ")[0])

        if liked_:
            self.liked_today = liked_[0].get("liked_today")
            self.comment_today = liked_[0].get("comment_today")
            print(
                colored(f" [   ]{self.liked_today}  Liked today  ---  {self.comment_today} commented on today", "blue"))
        else:
            self.db.insert({f"{self.username}_date_today": str(self.now).split(" ")[0], "liked_today": self.liked_today,
                            "comment_today": self.comment_today})

        self.track_liked_and_comments()

        if cookies:
                cj = pickle.loads(cookies)
                for cookie in cj:
                    if cookie.is_expired():
                        self.cookies_expired = True
                        print("cookie expired")

                        self.db.remove(where("credentials") == 'true')

                self.scraper = requests.Session()
                self.scraper.cookies = cj

                self.csrf_token = self.scraper.cookies.get_dict()['csrftoken']

                '''update headers'''
                headers = {
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                                  'like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; '
                                  'scale=2.00; 828x1792; 165586599) '
                }

                self.scraper.headers.update(headers)

                user = self.scraper.get(f"https://www.instagram.com/{self.username}/")

                logged_user = str(bs4.BeautifulSoup(user.text, 'lxml').title.text).split('•')[0]
                logged_user_ = str(logged_user).replace("is on Instagram", " ")

                print(colored(f"[+] {time.ctime()} logged in as {logged_user_} via cookies", "green"), end="\n\n")
                self.status=f"logged in as {logged_user_} using cookie session"
                self.return_status(self.status)

                timer=random.randrange(15,40)
                for e in range(timer):
                    progress_=round(e/timer*100)
                    self.return_status(f"startup process initiated {progress_}% complete")
                    time.sleep(1)

                    if self.stop_running_bot:
                        self.status = "stopping bot"
                        self.return_status(self.status)
                        break

                return "logged in"

        else:
            return self.expired_cookies()

    def expired_cookies(self):
        self.scraper = cloudscraper.create_scraper()
        self.time = int(datetime.datetime.now().timestamp())

        self.link = 'https://www.instagram.com/accounts/login/'
        self.login_url = 'https://www.instagram.com/accounts/login/ajax/'

        response = self.scraper.get(self.link)
        self.csrf = response.cookies.get("csrftoken")

        self.csrf_token = None

        self.payload = {
            'username': self.username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.time}:{self.password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        self.login_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/49.0.2623.112 Safari/537.36',
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": self.csrf
        }

        self.scraper = cloudscraper.CloudScraper()



        self.headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; '
                          'scale=2.00; 828x1792; 165586599) ',
            "x-csrftoken": self.csrf_token
        }

        return self.login()

    def login(self):

        login_response = self.scraper.post(self.login_url, data=self.payload, headers=self.login_header)

        json_data = json.loads(login_response.text)
        print(json_data)
        if json_data.get("authenticated"):
            print(colored("login successful", "green"))
            self.status="login successful"

            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()

            self.csrf_token = cookie_jar['csrftoken']
            print("csrf_token: ", self.csrf_token)
            session_id = cookie_jar['sessionid']
            user_id = cookie_jar['ds_user_id']
            print("session_id: ", session_id)

            encrypt_creds = fernet.Fernet(encryption_key)

            credentials = {"username": self.username, "password": self.password}
            pickled_credentials = pickle.dumps(credentials)
            encrypted = encrypt_creds.encrypt(pickled_credentials)

            encrypt_cookies=encrypt_creds.encrypt(pickle.dumps(cookies))

            self.db.insert({"encrypted": encrypted.decode("utf-8"),"login_cookies":encrypt_cookies.decode("utf-8"),"credentials": "true"})

            return "successful first login"

        else:
            print(colored(f"login failed {login_response.text}", "red"), end="\n\n")

            if "wait" in login_response.text:
                print(colored("! wait a couple of hours before trying again", "magenta"))
                return "! login failed, wait a couple of hours before trying again"

            else:
                if login_response.json()["user"]:
                    print(colored(f"! login failed, wrong password for user {self.username}", "red"))

                    return f"login failed ,wrong password for user {self.username}"

                else:
                    return f"!login failed, invalid user {self.username}", "red"

    def like_and_comment(self, post_id, post_username):
        print(post_id)
        self.status = f"{post_id}"
        self.return_status(self.status)

        print("\n")

        new_header = {
            'content-length': '0',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; '
                          'en-US; '
                          'scale=2.00; 828x1792; 165586599) ',
            "x-csrftoken": self.csrf_token}
        try:

            if self.update_liked(post_id) == "seen before":
                pass

            else:

                time_out_count = [count * 50 for count in range(1,20)]

                if self.liked_today in time_out_count:
                    '''timeout sleep'''
                    self.sleep_bot(timer=random.randrange(900, 1200), reason=" ⌛ like function time out ")

                liked_post = self.scraper.post(f"https://i.instagram.com/api/v1/web/likes/{post_id}/like/",
                                               headers=new_header)

                self.liked_today += 1

                print(colored(str(liked_post.json()), "green"))

                bar_val = round(self.liked_today / self.max_likes * 100)

                self.status = f"successfully liked {post_id} by {post_username} |{bar_val}"
                self.return_status(self.status)
                time.sleep(2)

                print("")

                try:
                    if len(self.comments)>=1:
                        set_timer=random.randrange(25,45)
                        for comment_count in range(set_timer):
                            self.status = f"posting comment on {post_id} {round(comment_count/set_timer*100)} "
                            self.return_status(self.status)
                            time.sleep(1)

                        random.shuffle(self.comments)

                        comment=self.comments[0]

                        comment_Post=self.scraper.post(f"https://i.instagram.com/api/v1/web/comments/{post_id}/add/",data={"comment_text":comment},
                                                       headers=new_header)
                        print(comment_Post.json())

                        bar_val=round(self.comment_today / self.max_comments * 100)
                        self.status = f"successfully commented on {post_id} by {post_username} |{bar_val}"
                        self.return_status(self.status)

                        self.comment_today+=1

                except Exception as e:
                    print(e)

            self.db.update(
                {f"{self.username}_date_today": str(self.now).split(" ")[0], "liked_today": self.liked_today,
                 "comment_today": self.comment_today})
            self.track_liked_and_comments()

            timer = random.randrange(10, 30)

        except Exception as e:
            print(e)

            self.status = str(e)
            self.return_status(self.status)
            timer = random.randrange(35,55)

            if "this photo has been deleted" in str(e):
                pass

            else:
                self.stop_running_bot = True

        time.sleep(random.randrange(5,8))

        for e in range(1, timer):
            sys.stdout.write(colored(f"\r[ ] liking next post in {e / timer * 100}", "green"))
            sys.stdout.flush()
            self.status = f"liking next post in {round(e / timer * 100)}%"

            self.return_status(self.status)

            if self.stop_running_bot:
                self.status = "stopping bot"
                self.return_status(self.status)
                break
            time.sleep(1)

    def like_hashtag(self,hash_):
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; '
                          'scale=2.00; 828x1792; 165586599) '
        }

        post_response = self.scraper.get(f"https://i.instagram.com/api/v1/tags/web_info/?tag_name={hash_}",
                                         headers=headers)
        medias = post_response.json()['data']['recent']['sections']

        self.seen_users = []

        for section in medias:
            for media in section['layout_content']['medias']:
                # print(media['media'])
                print('')
                post_id = media['media']['pk']
                post_username=media['media']['user']['username']

                self.like_and_comment(post_id,post_username)

                if self.obtained_users_posts:
                    liked=0
                    for user in self.target_usernames:

                        if self.stop_running_bot:
                            self.status = "stopping bot"

                            self.return_status(self.status)
                            break

                        if user in self.seen_users:
                            print(colored(f"\nyou've liked {user} first 5","red"))

                        else:
                            for post in self.obtained_users_posts.get(user):

                                if self.stop_running_bot:
                                    self.status = "stopping bot"

                                    self.return_status(self.status)
                                    break

                                post_id = post
                                post_username = user
                                self.like_and_comment(post_id,post_username)

                                liked+=1

                                if liked==5:
                                    break
                            self.seen_users.append(user)

                if self.stop_running_bot:
                    self.status = "stopping bot"
                    self.return_status(self.status)
                    break

            if self.stop_running_bot:
                self.status = "stopping bot"

                self.return_status(self.status)
                break

    def fetch_gathered_data(self,hashtag=None,usernames=None,comments=None):
        print("populated fields")
        self.hashtags=hashtag
        self.target_usernames=usernames
        self.comments=comments

        random.shuffle(self.hashtags)
        random.shuffle(self.target_usernames)
        random.shuffle(self.comments)

        print("this is the comment",self.comments)

    def stop_bot(self,stop=False,logout=False):
        if stop:
            self.stop_running_bot=True

        if logout:
            self.db.remove(where("credentials") == 'true')

    def get_username_posts(self,username_):
        posts=self.scraper.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username_}")
        found_post=posts.json()["data"]["user"]["edge_owner_to_timeline_media"]["edges"]

        all_posts=[]
        scraped=0
        for post in found_post:

            if self.stop_running_bot:
                self.status = "stopping bot"

                self.return_status(self.status)
                break

            post_id=post["node"]["id"]

            self.status = f"getting {username_} {post_id}"
            self.return_status(self.status)

            all_posts.append(post_id)

            scraped+=1
            if scraped==random.randrange(5,10):
                break

        self.obtained_users_posts.update({username_:all_posts})

        print(self.obtained_users_posts)

    def like_passed_hashtag(self):
        liked_hashtags=0
        while True:
            for user in self.target_usernames:
                if self.stop_running_bot:
                    self.status = "stopping bot"

                    self.return_status(self.status)
                    break

                if "@" in user:
                    user=user.replace("@","")

                self.get_username_posts(user)

                timer=random.randrange(40,65)

                for request_ in range(timer):
                    self.status = f"sending next get request in {round(request_/timer*100)}"
                    self.return_status(self.status)

                    if self.stop_running_bot:
                        self.status = "stopping bot"

                        self.return_status(self.status)
                        break

                    time.sleep(1)

            for hashtag in self.hashtags:

                self.track_liked_and_comments()

                if self.stop_running_bot:
                    print("stopping bot")
                    self.status = "stopping bot"
                    self.return_status(self.status)
                    break

                if "#" in hashtag:
                    hashtag=hashtag.replace("#",'')

                self.status=f"Getting {hashtag} posts {liked_hashtags}"

                self.like_hashtag(hashtag)

                timer_=random.randrange(60,70)

                for e in range(timer_):
                    print(f"Getting next hashtag {round(e/timer_*100)}")

                    self.status = f"Getting next hashtag {round(e/timer_*100)}"
                    self.return_status(self.status)

                    if self.stop_running_bot:
                        print("stopping bot")
                        self.status = "stopping bot"
                        self.return_status(self.status)
                        break

                    time.sleep(1)

                liked_hashtags+=1

            if self.stop_running_bot:
                print("stopping bot")
                self.status="stopping bot"
                self.return_status(self.status)
                break

    def return_status(self,bot_status):
        status=self.db.search(User.status=="true")

        if status:

            self.db.update({"status":"true","current_status":bot_status})

        else:
            self.db.insert({"status":"true","current_status":bot_status})

    def update_liked(self,post_id):
        liked_before = self.db.search(User.seen_post == "true")

        if liked_before:

            seen_posts=liked_before[0].get("post_id")
            if post_id in seen_posts:
                print(f"the bot has interacted with this post before {post_id}")

                self.status = f"⚠the bot has interacted with this post before {post_id}"
                self.return_status(self.status)
                time.sleep(0.4)

                return "seen before"

            else:
                seen_posts.append(post_id)

                self.db.update({"seen_post": "true", "post_id":seen_posts})

                print(colored("updated known posts","yellow"))

                return "updated known posts"

        else:
            self.db.insert({"seen_post": "true", "post_id":[post_id]})

            print(colored("created posts db data", "yellow"))

            return "created posts db data"

    def track_liked_and_comments(self):
        if self.liked_today >= 700:
            print(colored(
                f"\n ⚠ Hey {self.username} you are approaching the maximum limit of 1000 likes per day [ {self.liked_today / self.max_likes * 100}% ] used up",
                "red"))

            self.status = f"⚠ Hey {self.username} you are approaching the maximum limit of 1000 likes per day [ {self.liked_today / self.max_likes * 100}% ] used up"
            self.return_status(self.status)
            time.sleep(0.4)

        if self.liked_today >= self.max_likes:
            print(
                colored(
                    f"\n ⛔ {self.username} you've reached the maximum limit of 1000 likes per day [ {self.liked_today / self.max_likes * 100}% ] used up",
                    "red"))

            self.status=f"⛔ {self.username} you've reached the maximum limit of 1000 likes per day [ {self.liked_today / self.max_likes * 100}% ] used up"
            self.return_status(self.status)
            time.sleep(0.4)

            remaining_timer = self.db.search(User[f"{self.username}_freeze_time"] == "true")

            if remaining_timer:
                timer_ = remaining_timer[0].get("time_stamp")
                timer_ = datetime.datetime.fromtimestamp(timer_)
                time_remaining = timer_ - datetime.datetime.now()

                sleep_mins = time_remaining.seconds
            else:
                sleep_mins = 86400
                sleep_timer_now = datetime.datetime.now() + datetime.timedelta(seconds=sleep_mins)
                self.db.insert({f"{self.username}_freeze_time": "true", "time_stamp": sleep_timer_now.timestamp()})

            self.sleep_bot(timer=sleep_mins, reason="[ max liked posts reached ] sleep mode ")
            self.db.update({f"{self.username}_freeze_time": "false", "time_stamp": 0})

        if self.comment_today >= 100:
            print(colored(
                f"\n ⚠ Hey {self.username} you are approaching the maximum limit of 200 comments per day [ {self.comment_today / self.max_comments * 100} ] used up",
                "blue"))

            self.status = f" ⚠ Hey {self.username} you are approaching the maximum limit of 200 comments per day [ {self.comment_today / self.max_comments * 100} ] used up"
            self.return_status(self.status)
            time.sleep(0.4)

        if self.comment_today >= self.max_comments:
            print(
                colored(
                    f"\n ⛔ {self.username} you've reached the maximum limit of 200 comments per day [ {self.comment_today / self.max_comments * 100}% ] used up",
                    "red"))

            self.status=f"⛔ {self.username} you've reached the maximum limit of 200 comments per day [ {self.comment_today / self.max_comments * 100}% ] used up"

            self.return_status(self.status)
            self.comments.clear()
            time.sleep(0.4)

            '''disable comments'''

    def sleep_bot(self, timer=random.randrange(850, 1220), reason=""):
        sleep_time = timer
        lengths = [e for e in range(0, 10)]
        timer = time.perf_counter()
        char = "▓"
        for e in range(sleep_time):
            percentage = e / sleep_time * 100
            current_time = time.perf_counter() - timer
            time_remaining = datetime.timedelta(seconds=sleep_time - current_time)
            if "max liked posts" in reason:
                sleep_mins = "Remaining Time" + str(time_remaining)
                time_remaining = ""
            else:
                sleep_mins = str(time_remaining).split(":")[1] + " mins"
                time_remaining = ""
            sys.stdout.write(
                colored(
                    f"\r[{sleep_mins}] {reason} sleep Timeout started | progress {time_remaining}{char} {round(percentage, 4)}%",
                    "green"))

            self.status = f"[{sleep_mins}] {reason} sleep Timeout started | progress {time_remaining}{char} {round(percentage, 4)}%"

            self.return_status(self.status)

            sys.stdout.flush()
            char_concatenate = round(percentage / 10) + 1

            char = "▓" * char_concatenate
            if len(char) in lengths:
                print("")
                lengths.remove(len(char))
            time.sleep(1)

            if self.stop_running_bot:
                self.status = "stopping bot"
                self.return_status(self.status)
                break

