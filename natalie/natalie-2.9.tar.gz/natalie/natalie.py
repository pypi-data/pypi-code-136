import datetime
import sys
import threading
import time

import requests

# GUI FILE
# IMPORT FUNCTIONS

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
from .ui_main import Ui_MainWindow
from PyQt5.QtCore import *
import os
import pickle
from cryptography import fernet

import pymongo
from .backend_code import *

from tinydb import TinyDB, Query
db = TinyDB('database.json')

db2 = TinyDB('last_data_database.json')
User = Query()

start_login=True
win_set=False
can_login=False
successful_login = False
break_login_thread=False
found_images=False
profile_set=False
bot_running = False

avatar=''.encode()
followers=""
following=""

lost_followers_=0
added_followers_=0

login_fail=""

error_msg=""

last_status=""

recent_follower_stat="gained"

try:
    password = "RU2h08woBk4qlTHs"
    client = pymongo.MongoClient(
        f"mongodb+srv://natalie:{password}@cluster0.pzbl6.mongodb.net/?retryWrites=true&w=majority")
    mongo_db = client.get_database("natalie_app")

except Exception as e:
    error_msg="check your internet connection \n DB connection refused"

cookie_creds=[]

cloud_images={}


hashtags=[]
comments=[]
target_usernames=[]

status=""

known_status=[]

encryption_key = b'tUvzG-BWuh2xQB1k4VKynl4ox_2k9VHCMjRe4-UOQgA='


GLOBAL_STATE=0
max_likes=50
liked=0

loaded_img=False
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox,QSizeGrip
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymongo
import threading

scroll_style_sheet=''' QScrollBar:vertical {
	border: none;
    background: rgb(45, 45, 68);
    width: 14px;
    margin: 15px 0 15px 0;
	border-radius: 0px;
 }

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {	
	background-color: rgb(80, 80, 122);
	min-height: 30px;
	border-radius: 7px;
}
QScrollBar::handle:vertical:hover{	
	background-color: rgb(255, 0, 127);
}
QScrollBar::handle:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {	
	background-color: rgb(255, 0, 127);
}
QScrollBar::sub-line:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-bottom-left-radius: 7px;
	border-bottom-right-radius: 7px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {	
	background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}


'''


class MainWindow(QMainWindow):
    load_animation=""

    username = ""
    password = ""

    def moveWindow(self,event):
        # RESTORE BEFORE MOVE

        if UIFunctions.returnStatus() == 1:
            UIFunctions.maximize_restore(self)

        # IF LEFT CLICK MOVE WINDOW

        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def get_part_of_day(self,h):
        return (
            "Good morning"
            if 5 <= h <= 11
            else "Good afternoon"
            if 12 <= h <= 16
            else "Good evening"
            if 17 <= h <= 23
            else "Nighty Night"
        )

    def initialize_win(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.status_listwidget.clear()

        self.ui.liked_progressBar.setValue(0)
        self.ui.like_listWidget.clear()

        self.ui.comments_progressbar.setValue(0)
        self.ui.comment_listwidget.clear()

        self.get_last_passed_data()

        # MOVE WINDOW


        # SET TITLE BAR
        self.ui.header_frame.mouseMoveEvent = self.moveWindow

        self.ui.login_header_frame.mouseMoveEvent=self.moveWindow

        UIFunctions.uiDefinitions(self)

        UIFunctions.edit_verical_scrollbar(self)

        UIFunctions.change_avatar(self)

        self.update_worker = UpdateScreen()
        self.update_worker.start()
        self.update_worker.signal.connect(self.update_)

        self.images_worker = TrackImages()
        self.images_worker.start()
        self.images_worker.signal.connect(self.get_images)

        self.followers_worker = TrackFollowers()
        self.followers_worker.start()
        self.followers_worker.signal.connect(self.track_profile_updator)

        self.collected_inputs_worker = Collect_targetusers_hashtags_comments()
        self.collected_inputs_worker.start()
        self.collected_inputs_worker.signal.connect(self.collected_hashtags_and_data)

        self.setWindowTitle("Natalie App")

        th=threading.Thread(target=self.get_creds_thread)
        th.start()

        UIFunctions.set_current_win(self,0)
        UIFunctions.loading_page(self)

        self.ui.pushButton.clicked.connect(self.login_button)

        self.ui.start_button.clicked.connect(self.start_bot)

        self.ui.logout_button.clicked.connect(self.logout)

        self.show()

    def get_last_passed_data(self):
        last_data=db2.search(User.run_data=="yes")
        if last_data:
            last_comment=last_data[0].get("comments")
            last_target_users=last_data[0].get("target_users")
            last_hashtags=last_data[0].get("last_hashtags")

            for hashtag in last_hashtags:
                self.ui.hashtag_input.insertPlainText(f"{hashtag}\n")

            for user in last_target_users:
                self.ui.targetusernames_input.insertPlainText(f"{user}\n")

            for comment in last_comment:
                self.ui.add_comments_input.insertPlainText(f"{comment}\n")

        else:
            pass

    def logout(self):
        global bot_running
        print("logging out")

        if not bot_running:
            self.pop_up_window("you must start the bot and click logout inorder to logout !")

        else:
            self.bot_.stop_bot(stop=True,logout=True)

            UIFunctions.add_scroll_status(self,f"logged out of {self.username} ")

            bot_running=False

            self.pop_up_window("you'll be logged out")

            self.close()

            UIFunctions.set_current_win(self,1)
            UIFunctions.login_page(self)

    def populate_status_(self):
        global status
        while True:
            if bot_running:
                try:
                    status_ = db.search(User.status == "true")

                    if status_:
                        status=status_[0].get("current_status")

                except Exception as e:
                    print(e)

            else:
                db.update({"status": "true", "current_status":f"last run {str(time.ctime())}"})
                break

            time.sleep(0.1)

    def run_main_bot(self,hashtags_,target_usernames_,comments_):
        print("bot is running")

        last_data = db2.search(User.run_data == "yes")

        while "" in comments_:
            comments_.remove("")

        while "" in target_usernames_:
            target_usernames_.remove("")

        while "" in hashtags_:
            hashtags_.remove("")

        print(comments_)
        print(target_usernames_)
        print(hashtags_)

        if last_data:

            db2.update({"run_data":"yes","comments":comments_,"target_users":target_usernames_,"last_hashtags":hashtags_})

        else:
            db2.insert({"run_data": "yes", "comments": comments_, "target_users":target_usernames_,
                       "last_hashtags":hashtags_})

        self.bot_ = MainBot()
        self.bot_.login_user(self.username,self.password,db)
        self.bot_.fetch_gathered_data(hashtags_,target_usernames_,comments_)

        self.bot_.like_passed_hashtag()

    def start_bot(self):
        global bot_running

        if bot_running and self.ui.start_button.text()=="Stop bot":
            print("bot is already running ,stopping the bot")
            self.pop_up_window("you are about to stop the bot")
            self.bot_.stop_bot(stop=True)

            bot_running=False

            self.ui.start_button.setText("Start Bot")

        else:

            found_hashtags=False
            found_users=False

            for hash_ in hashtags:
                if hash_:
                    found_hashtags=True

            for user in target_usernames:
                if user:
                    found_users=True

            if not found_hashtags and not found_users:
                self.pop_up_window("the bot can't run without hashtags or comments!\nspecify some hashtags or target usernames")

            elif found_users and not found_hashtags:
                self.pop_up_window("the bot can't run on target usernames alone \nspecify atleast one hashtag")
                # main_bot_thread=threading.Thread(target=self.run_main_bot,args=(hashtags,target_usernames,comments))
                # main_bot_thread.start()
                #
                # bot_running = True
                #
                # populate_status = threading.Thread(target=self.populate_status_)
                # populate_status.start()
                #
                # self.ui.start_button.setText("Stop bot")

            elif found_hashtags and not found_users:
                self.pop_up_window("the bot will run on hashtags only")

                main_bot_thread = threading.Thread(target=self.run_main_bot, args=(hashtags, target_usernames, comments))
                main_bot_thread.start()

                bot_running = True

                populate_status=threading.Thread(target=self.populate_status_)
                populate_status.start()

                self.ui.start_button.setText("Stop bot")

            elif found_hashtags and found_users:
                self.pop_up_window("the bot will run on both hashtags and target usernames")

                main_bot_thread = threading.Thread(target=self.run_main_bot, args=(hashtags, target_usernames, comments))
                main_bot_thread.start()

                bot_running = True

                populate_status = threading.Thread(target=self.populate_status_)
                populate_status.start()

                self.ui.start_button.setText("Stop bot")

    def collected_hashtags_and_data(self,val):

        global hashtags,comments,target_usernames

        hashtags_inputs=self.ui.hashtag_input.toPlainText().split("\n")
        target_users_inputs=self.ui.targetusernames_input.toPlainText().split("\n")
        comment_inputs=self.ui.add_comments_input.toPlainText().split("\n")

        hashtags=hashtags_inputs
        comments=comment_inputs
        target_usernames=target_users_inputs

        print(hashtags)
        print(comments)
        print(target_usernames)

    def track_profile_updator(self,val):
        global profile_set,status,last_status
        print(val)

        if avatar and not profile_set:

            qp = QtGui.QPixmap()
            qp.loadFromData(avatar)

            self.ui.user_avatar.setPixmap(qp)
            hour_=int(datetime.datetime.now().hour)

            self.ui.username.setText(f"{self.get_part_of_day(hour_)}\n{self.username}")

            #profile_set=True

        new_status = f"you'll be logged in as {self.username} once you click Start Bot !"

        if new_status not in known_status and self.username:
            UIFunctions.add_scroll_status(self,new_status)
            known_status.append(new_status)

        if status and self.username and status !=last_status:
            UIFunctions.add_scroll_status(self, status)
            last_status=status

        if recent_follower_stat=="gained":
            qp = QtGui.QPixmap()
            qp.loadFromData(cloud_images.get("increased"))

            self.ui.stat_indicator.setPixmap(qp)

            self.ui.gaiin_lost.setText(f"{added_followers_} Gained since startup")

        else:
            qp = QtGui.QPixmap()
            qp.loadFromData(cloud_images.get("decreased"))

            self.ui.stat_indicator.setPixmap(qp)

            self.ui.gaiin_lost.setText(f"{lost_followers_} lost since startup")

        print(f"found followers {followers}")
        print(f"fount following {following}")

        self.ui.follower_count.setText(f"{followers}")
        self.ui.following_count.setText(f"{following}")

    def live_follower_and_avatar(self):
        start = time.perf_counter()

        def get_followers(user):
            global lost_followers_,added_followers_,avatar,followers,following,recent_follower_stat
            try:
                lost_followers = 0
                gained_followers = 0
                headers = {
                    'User-Agent': 'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1'

                }

                r = requests.get(f"https://instastories.watch/api/profile?username={user}", headers=headers)
                resp = r.json()

                followers = resp["profileInfo"]["subscriber"]
                following = resp["profileInfo"]["subscription"]
                avatar_url = resp["profileInfo"]["avatar"].split("/proxy/")[1]

                r = requests.get(avatar_url, headers=headers)
                avatar = r.content

                print(avatar_url)

                found_user_data = db.search(User.user == f'{user}')
                if not found_user_data:

                    db.insert({"user": f"{user}", "followers": f'{followers}', "following": f"{following}"})

                    added_followers = 0

                    print('first data loaded')

                else:
                    difference = int(found_user_data[0].get('followers')) - int(followers) + lost_followers

                    added_followers = int(followers) - int(found_user_data[0].get('followers'))

                    if difference >= 1:
                        lost_followers += difference

                        lost_followers_=lost_followers

                        db.update({"user": f"{user}", "followers": f'{followers}', "following": f"{following}",
                                   "lost_followers": lost_followers, "gained_followers": added_followers})

                        recent_follower_stat = "lost"

                    if added_followers > 0:
                        gained_followers += added_followers

                        added_followers_=gained_followers

                        db.update({"user": f"{user}", "followers": f'{followers}', "following": f"{following}",
                                   "lost_followers": lost_followers, "gained_followers": gained_followers})

                        recent_follower_stat="gained"

                print(
                    f"[ time frame ] {datetime.timedelta(seconds=time.perf_counter() - start)}\n[ ] followers {followers} \n[ ] following {following} \n[ ] gained {added_followers} \n[ ] lost {lost_followers}",
                    end="\n\n")

            except Exception as e:
                print(e)

        while True:
            get_followers(user=self.username)
            time.sleep(random.randrange(60,140))

    def get_images(self,val):
        global found_images
        print(val)
        if cloud_images:
            qp = QtGui.QPixmap()
            qp.loadFromData(cloud_images.get("loading_screen_img"))
            self.ui.loading_image.setPixmap(qp)
            print("set loading  screen image")

            qp = QtGui.QPixmap()
            qp.loadFromData(cloud_images.get("login_screen_img"))

            self.ui.image_background.setPixmap(qp)

            qp = QtGui.QPixmap()
            qp.loadFromData(cloud_images.get("increased"))

            self.ui.stat_indicator.setPixmap(qp)

            "loading_image"

            print("set login screen image")

            found_images=True

    def get_creds_thread(self):
        global successful_login
        # simulate some heavy lifting

        #time.sleep(7)

        credential_cookies = mongo_db.get_collection("images")
        images = credential_cookies.find()

        for image in images:

            for key,value in image.items():
                if key !="_id":
                    print(key)
                    cloud_images.update(image)

        time.sleep(7)

        '''wait for thread to add background images'''

        encrypt_creds = fernet.Fernet(encryption_key)

        credentials = db.search(User.credentials == 'true')

        if credentials:
            # print(credentials)
            decrypt_credentials = credentials[0].get("encrypted").encode()

            decrypt_cryptography = encrypt_creds.decrypt(decrypt_credentials)
            decrypt_pickle2 = pickle.loads(decrypt_cryptography)
            self.username = decrypt_pickle2.get("username", "specify a username")
            self.password = decrypt_pickle2.get("password", "specify a password")

            cookie_creds.append(self.username)
            cookie_creds.append(self.password)
            successful_login=True

            print(f"found credentials")

        else:
            cookie_creds.append("no cookies found")
            print("no cookies found")

    def pop_up_window(self,message):
        msg = QMessageBox()
        msg.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(68, 68, 68, 255), stop:1 rgba(52, 52, 52, 255));\n"
                "\n"
                "border-radius:2px;\ncolor:white;")

        msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        msg.setWindowTitle("Natalie App")

        msg.setIcon(QMessageBox.Information)

        if "logged out" in message:

            msg.setText(f"{message} in 10s")

        else:
            msg.setText(message)

        msg.exec_()

    def login_button(self):

        global can_login,successful_login, break_login_thread, login_fail, error_msg
        if not can_login:

            login_fail = ""

            error_msg = ""

            break_login_thread = False
            login_fail = False

            print("login button clicked")
            username=self.ui.username_input.text()
            password=self.ui.password_input.text()

            self.username=username
            self.password=password

            print(username)
            # print(password)

            if not username:
                self.pop_up_window("you've not entered a username")

            if not password:
                self.pop_up_window("you've not entered a password")

            if password and username:
                can_login=True

                self.ui.pushButton.setStyleSheet("*{\n"
                                                 "background-color: rgb(106, 59, 248);\n"
                                                 "color: rgb(234, 234, 234);\n"
                                                 "}\n"
                                                 "\n")
                self.ui.pushButton.setText("Login you in ")

                self.login_worker = ListenLogin()
                self.login_worker.start()
                self.login_worker.signal.connect(self.login_status)

                login_thread=threading.Thread(target=self.populate_cookies_field,args=(username,password))
                login_thread.start()

        else:
            self.ui.pushButton.setStyleSheet("*{\n"
"background-color: rgb(106, 59, 248);\n"
"color: rgb(234, 234, 234);\n"
"}\n"
"\n")
            self.ui.pushButton.setText("Chill broski \n still login in .. ")
            print("there's is a login going on")

    def login_status(self,val):
        global break_login_thread
        print(val)
        if login_fail:

            self.ui.pushButton.setStyleSheet("*{\n"
                                             "background-color: rgb(255, 23, 96);\n"
                                             "color: rgb(234, 234, 234);\n"
                                             "}\n"
                                             "\n"
                                             "*:hover{\n"
                                             "    background-color: rgb(106, 59, 248);\n"
                                             "}")

            self.ui.pushButton.setText("Login")

            break_login_thread = True
            self.pop_up_window(login_fail)

        elif successful_login:
            break_login_thread = True

            UIFunctions.set_current_win(self, 2)
            UIFunctions.main_page(self)
            print("login succeeded")

            self.ui.username.setText(self.username)

            tracking_func = threading.Thread(target=self.live_follower_and_avatar)
            tracking_func.start()

    def populate_cookies_field(self,username,password):
        global successful_login,login_fail,can_login

        while True:
            if can_login:
                bot_=MainBot()
                returned_msg= bot_.login_user(username,password,db)
                if "login failed" not in returned_msg:
                    successful_login=True
                    print("populated cookies")
                    print(returned_msg)
                else:
                    login_fail=returned_msg

                can_login=False

            break

    def update_(self,val):
        global win_set
        progress=round(int(val)/100*100)
        print(val)

        if cookie_creds:

            if "no cookies found" in cookie_creds:
                UIFunctions.set_current_win(self,1)
                UIFunctions.login_page(self)

            elif cookie_creds or successful_login:
                UIFunctions.set_current_win(self, 2)
                UIFunctions.main_page(self)

                self.ui.username.setText(self.username)

                tracking_func=threading.Thread(target=self.live_follower_and_avatar)
                tracking_func.start()

            win_set=True

        self.load_animation+="."

        if len(self.load_animation)>=5:
            self.load_animation=""

        '''check connections'''
        if error_msg:
            self.ui.connection_label.setText(error_msg)

        else:
            self.ui.connection_label.setText(f"Connecting to database {self.load_animation}")
            self.ui.loading_bar.setValue(progress)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class UpdateScreen(QThread):
    signal = pyqtSignal(str)

    def run(self):
        counter=0
        while True:
            self.signal.emit(f"{counter}")
            time.sleep(0.2)
            counter+=1
            if win_set:
                break


class ListenLogin(QThread):
    signal = pyqtSignal(str)

    def run(self):
        counter=0
        while True:
            self.signal.emit(f"listening for login{counter}")
            time.sleep(0.2)
            counter+=1
            if break_login_thread:
                print("block login thread")
                break

            else:
                print("dont block login")


class TrackImages(QThread):
    signal = pyqtSignal(str)

    def run(self):
        counter = 0
        while True:
            self.signal.emit(f"Waiting for images{counter}")
            time.sleep(0.2)
            counter += 1
            if found_images:
                print("block login thread")
                break


class TrackFollowers(QThread):
    signal = pyqtSignal(str)

    def run(self):
        counter = 0
        while True:
            self.signal.emit(f"Tracking followers,following,profile avatar update{counter}")
            time.sleep(0.3)
            counter += 1


class Collect_targetusers_hashtags_comments(QThread):
    signal = pyqtSignal(str)

    def run(self):
        counter = 0
        while True:
            self.signal.emit(f"collecting inputs {counter}")
            time.sleep(0.4)
            counter += 1


class UIFunctions(MainWindow):
    ## ==> MAXIMIZE RESTORE FUNCTION

    def maximize_restore(self):
        global GLOBAL_STATE

        status = GLOBAL_STATE

        self.ui.close_button.setToolTip("close")
        self.ui.close_button_4.setToolTip("close")

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            # self.ui.main_frame.setContentsMargins(0, 0, 0, 0)
            # self.ui.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.restore_button.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            # self.ui.main_frame.setContentsMargins(10, 10, 10, 10)
            # self.ui.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")

            self.ui.minimize_button.setToolTip("minimize")

            self.ui.minimize_button_4.setToolTip("minimize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.main_frame.setGraphicsEffect(self.shadow)

        self.ui.login_header_frame.setGraphicsEffect(self.shadow)

        # # MAXIMIZE / RESTORE
        self.ui.restore_button.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        #
        # # MINIMIZE
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        #
        # # CLOSE
        self.ui.close_button.clicked.connect(lambda: self.close())

        '''login page'''

        # # MAXIMIZE / RESTORE
        # self.ui.restore_button_4.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        #
        # # MINIMIZE
        self.ui.minimize_button_4.clicked.connect(lambda: self.showMinimized())
        #
        # # CLOSE
        self.ui.close_button_4.clicked.connect(lambda: self.close())

        # ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.footer_frame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def change_avatar(self):

        self.ui.user_avatar.setStyleSheet('''*{border:2px solid  rgb(17, 120, 255);}\n
                                            *:hover{border:3px solid rgb(255, 23, 96);}''')

    def loading_page(self):
        self.setStyleSheet("\n"
"background-color: rgba(59, 59, 59,0);\n"
"border-radius:5px;")

        self.resize(670, 331)

        self.ui.loading_image.setGeometry(QtCore.QRect(30,10, 651, 331))

        self.ui.loading_bar.setGeometry(QtCore.QRect(180,150, 343, 24))

        self.ui.connection_label.setGeometry(QtCore.QRect(240,240, 241, 61))

    def set_current_win(self,win):
        self.ui.stackedWidget.setCurrentIndex(win)

    def login_page(self):
        self.move(500,100)

        self.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,0);\n"
                           "border-radius:5px;")

        self.ui.login_header_frame.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,255);\n"
                           "border-radius:5px;")

        self.resize(451,737)

        self.ui.login_body_frame.setMaximumSize(QtCore.QSize(451,737))

    def main_page(self):
        self.move(500, 100)

        self.ui.hashtag_title.setStyleSheet("border:none;")
        self.ui.commented_title_2.setStyleSheet("border:none;")

        self.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,35);\n"
                           "border-radius:5px;")

        self.ui.header_frame.setStyleSheet("\n"
                                           "background-color: rgba(59, 59, 59,255);\n"
                                           "border-radius:5px;")

        self.resize(542,614)
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))

    def set_blur(self):
        self.blur_effect = QGraphicsBlurEffect()

        # setting blur radius
        self.blur_effect.setBlurRadius(4)

        self.ui.hashtag_frame.setGraphicsEffect(self.blur_effect)

    def edit_verical_scrollbar(self):

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        # setting vertical scroll bar to it
        self.ui.hashtag_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.add_comments_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.targetusernames_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.like_listWidget.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.comment_listwidget.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.status_listwidget.setVerticalScrollBar(scroll_bar)

    def add_scroll_status(self,value):

        print('''      .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
 jgs  `-._   ````    _.-'
          ``-------''''')

        self.ui.status_listwidget.setStyleSheet("color: rgb(0,170,255)")
        self.ui.status_listwidget.addItem(value)
        self.ui.status_listwidget.scrollToBottom()

        if "successfully liked" in value:
            print(f"found liking in value {value}")
            value=value.split("|")
            bar_val=int(value[1])

            self.ui.liked_progressBar.setValue(bar_val)

            self.ui.like_listWidget.addItem(value[0])
            self.ui.like_listWidget.scrollToBottom()

        if "maximum limit of 1000 likes" in value:
            bar_val=round(float(value.split("[")[1].split("]")[0].replace("%","")))

            self.ui.liked_progressBar.setValue(bar_val)

            self.ui.like_listWidget.addItem(value)
            self.ui.like_listWidget.scrollToBottom()

        if "like function" in value:
            value=value.split("sleep")[0]

            self.ui.like_listWidget.addItem(value)
            self.ui.like_listWidget.scrollToBottom()

        if "successfully commented" in value:
            value =value.split("|")
            bar_val=int(value[1])
            self.ui.comments_progressbar.setValue(bar_val)

            self.ui.comment_listwidget.addItem(value[0])

            self.ui.comment_listwidget.scrollToBottom()

        if "maximum limit of 200 comments" in value:
            bar_val = round(float(value.split("[")[1].split("]")[0].replace("%", "")))

            self.ui.comments_progressbar.setValue(bar_val)

            self.ui.comment_listwidget.addItem(value)

            self.ui.comment_listwidget.scrollToBottom()

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE


def start():
    app = QApplication(sys.argv)
    m=MainWindow()
    m.initialize_win()

    os._exit(app.exec_())

    m.update()



