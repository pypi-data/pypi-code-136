from re import findall
from random import randint, choice
from json import loads, dumps, JSONDecodeError
from base64 import b64encode
from datetime import datetime
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, urlsafe_b64decode
from time import time
from urllib.parse import unquote
from requests import post,get
import aiohttp
from datetime import datetime
import urllib.request
from urllib import request,parse
from pathlib import Path

class encryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('UTF-8'), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result                

print_BoT = """ -\U0001f506- LiBrary DaRk - BoT RuBika (version 2.0.0)

 -\U0001F92B- Channel Rubika : rubika.ir/DARK_BOT_RUBIKA
  
در حـال فعـال شـدن |  منتظر بمـانیـد ...                                   

 . . . . . . . . . . . . . . . . . ."""

Error_auth = "شناسه اکانت اشتباه وارد شده است !"
            
class clients:
	web = {
		"app_name": "Main",
		"app_version": "4.1.2",
		"platform": "Web",
		"package": "web.rubika.ir",
		"lang_code": "fa"
	}
	android = {
	    "app_name":"Main",
		"app_version":"2.98",
		"pla(tform":"Android",
		"package":"ir.resaneh1.iptv",
		"lang_code":"en"
	}
	
answered = ['message_ids']

get_url = lambda url_number: f"https:/1/messengerg2c{url_number}.iranlms.ir/"

        
class RoBoT:
	def __init__(self,account):
		self.auth = account
		self.enc = encryption(account)
		print(print_BoT)				
		
		if len(self.auth) < 32:print(Error_auth),exit()
			
		if len(self.auth) > 32:print(Error_auth),exit()
				
	def excute(self, method, platform="web"):
		if platform == "web":
			while True:
				try:
					requests = self.enc.decrypt(post(
					json = {
						"api_version": "5",
						"auth": self.auth,
						"data_enc": self.enc.encrypt(dumps(method))},url=get_url(17)).json()["data_enc"])
					break
				except:continue
			return loads(requests)

	def Send_Message(self, guid, text, reply_to_message_id=None, metadata: list=None):
		method = {
			"method":"sendMessage",
			"input":{
				"object_guid": guid,
				"rnd": str(randint(100000,900000)),
				"text": text,
				"reply_to_message_id": reply_to_message_id
			},
			"client": clients.web
		}
		if metadata is not None:
			method["input"]["metadata"] = {"meta_data_parts": metadata}
			
		return self.excute(method)["data"]["message_update"]

	def Delete_message(self, guid, message_ids: list):
		method = {
			"method": "deleteMessages",
			"input":{
				"object_guid": guid,
				"message_ids": message_ids,
				"type": "Global"
			},
			"client": clients.web
		}
		return self.excute(method)										
	
	def Edit_Message(self, guid, message_id, new_text, metadata: list=None):
		method = {
			"method": "editMessage",
			"input":{
				"message_id": message_id,
				"object_guid": guid,
				"text": new_text 
			},
			"client": clients.web
		}
		if metadata is not None:
			method["input"]["metadata"] = {"meta_data_parts": metadata}
			
		return self.excute(method)

	def Get_info(self, guid):
		method = None

		if guid.startswith('u'):
			method = {
				"method": "getUserInfo",
				"input":{
					"user_guid": guid
				},
				"client": clients.web
			}
		elif guid.startswith('g'):
			method = {
				"method": "getGroupInfo",
				"input":{
					"group_guid": guid
				},
				"client": clients.web
			}
		elif guid.startswith('c'):
			method = {
				"method": "getChannelInfo",
				"input":{
					"channel_guid": guid
				},
				"client": clients.web
			}
		return self.excute(method).get("data")
	
	
	def Get_username_info(self, username):
		method = {
		    "method":"getObjectByUsername",
		    "input":{
		        "username":username
			},
			"client": clients.web
		}
		return self.excute(method)
		
 
	def chats_update(self):
		time_stamp = round(datetime.today().timestamp()) - 200
		method = {
			"method": "getChatsUpdates",
			"input":{
				"state": str(time_stamp),
			},
			"client": clients.web
		}
		return self.excute(method).get("data").get("chats")
		
		
	def get_message_info(self, guid, message_ids):
		method = {
			"method": "getMessagesByID",
			"input":{
				"object_guid": guid,
				"message_ids": message_ids
			},
			"client": clients.web
		}
		return self.excute(method).get("data").get("messages")
		
		
	def Join_group(self, link):
		method = {
			"method": "joinGroup",
			"input":{
				"hash_link": link.split('/')[-1]
			},
			"client": clients.web
		}
		return self.excute(method)
		
		
	def Leave_Group(self, guid):
		method = {
			"method":"leaveGroup",
			"input":{
				"group_guid": guid
			},
			"client": clients.web
		}
		return self.excute(method)
		
		
	def Block_User(self, guid):
		method = {
			"method": "setBlockUser",
			"input":{
				"action": "Block",
				"user_guid": guid
			},
			"client": clients.web
		}
		return self.excute(method)

	def Un_Block(self, guid):
		method = {
			"method": "setBlockUser",
			"input":{
				"action": "Unblock",
				"user_guid": guid
			},
			"client": clients.web
		}
		return self.excute(method)
		
	def Add_Channel(self, chat_id, user_ids):
		method = {
			"method": "addChannelMembers",
			"input":{
		        "channel_guid": chat_id,
				"member_guids": user_ids
			},
			"client": clients.web
		}
		return self.excute(method)

	def Set_GroupTimer(self, chat_id, time):
		method = {
			"method":"editGroupInfo",
			"input":{
				"group_guid": chat_id,
				"slow_mode": time,
				"updated_parameters":["slow_mode"]
			},
			"client": clients.web
		}
		return self.excute(method)

				
	def Forward_Messages(self, from_guid, message_ids: list, to_guid):
		method = {
			"method": "forwardMessages",
			"input":{
				"from_object_guid": from_guid,
				"message_ids": message_ids,
				"rnd": str(randint(100000,900000)),
				"to_object_guid": to_guid
			},
			"client": clients.web
		}
		return self.excute(method)
		
	def Delete_ChatHistory(self, chat_id, msg_id):
		method = {
			"method":"deleteChatHistory",
			"input":{
				"last_message_id": msg_id,
				"object_guid": chat_id
			},
			"client": clients.android
		}
		return self.excute(method)

	def UnBan_GroupMember(self, chat_id, user_id):
		method = {
		    "method":"banGroupMember",
		    "input":{
		        "group_guid": chat_id,
				"member_guid": user_id,
				"action":"Unset"
			},
			"client": clients.android
		}
		return self.excute(method)
		
	def Ban_GroupMember(self, chat_id, user_id):
		method = {
		    "method":"banGroupMember",
		    "input":{
		        "group_guid": chat_id,
				"member_guid": user_id,
				"action":"Set"
			},
			"client": clients.android
		}
		return self.excute(method)			
		
	def Set_GroupAdmin(self, chat_id, user_id):
		method = {
			"method":"setGroupAdmin",
			"input":{
				"group_guid": chat_id,
				"access_list":["PinMessages","DeleteGlobalAllMessages","BanMember","SetMemberAccess"],
				"action": "SetAdmin",
				"member_guid": user_id
			},
			"client": clients.android
		}
		return self.excute(method)					

	def Delete_GroupAdmin(self,chat_id,user_id):
		method = {
			"method":"setGroupAdmin",
			"input":{
				"group_guid": chat_id,
				"action": "UnsetAdmin",
				"member_guid": user_id
			},
			"client": clients.android
		}
		return self.excute(method)			
		
	def logout(self):
		method = {
			"method":"logout",
			"input":{},
			"client": clients.android
		}
		return self.excute(method)

	def Join_Channel(self, link):
		hashLink = link.split("/")[-1]
		method = {
			"method":"joinChannelByLink",
			"input":{
				"hash_link": hashLink
			},
			"client": clients.web
		}
		return self.excute(method)
		
	def Join_ChannelByID(self, chat_id):
		method = {
			"method":"joinChannelAction",
			"input":{
				"action": "Join",
				"channel_guid": chat_id
			},
			"client": clients.web
		}
		return self.excute(method)
						
	def Leave_Channel(self, chat_id):
		method = {
			"method":"joinChannelAction",
			"input":{
				"action": "Leave",
				"channel_guid": chat_id
			},
			"client": clients.web
		}
		return self.excute(method)

	def Start_VoiceChat(self, chat_id):
		method = {
			"method":"createGroupVoiceChat",
			"input":{
				"chat_guid":chat_id
			},
			"client": clients.web
		}
		return self.excute(method)

	def Edit_VoiceChat(self,chat_id,voice_chat_id, title):
		method = {
			"method":"setGroupVoiceChatSetting",
			"input":{
				"chat_guid":chat_id,
				"voice_chat_id" : voice_chat_id,
				"title" : title ,
				"updated_parameters": ["title"]
			},
			"client": clients.web
		}
		return self.excute(method)

	def Finish_VoiceChat(self, chat_id, voice_chat_id):
		method = {
			"method":"discardGroupVoiceChat",
			"input":{
				"chat_guid":chat_id,
				"voice_chat_id" : voice_chat_id
			},
			"client": clients.web
		}
		return self.excute(method)
		
	def Group_Link(self, chat_id):
		method = {
			"method":"getGroupLink",
			"input":{
				"group_guid":chat_id
			},
			"client": clients.web
		}
		return self.excute(method).get("data").get("join_link")

	def Send_Poll(self, chat_id, question, options):
		method = {
			"method":"createPoll",
			"input":{
				"allows_multiple_answers": False,
				"is_anonymous": True,
				"object_guid":chat_id,
				"options": options,
				"question": question,
				"rnd":f"{randint(100000,999999999)}",
				"type": "Regular"
			},
			"client": clients.web
		}
		return self.excute(method)

	def Add_Number_Phone(self, first_num, last_num, numberPhone):
		method = {
			"method":"addAddressBook",
			"input":{
				"first_name":first_num,
				"last_name":last_num,
				"phone":numberPhone
			},
			"client": clients.android
		}
		return self.excute(method)

	def Pin_Message(self, chat_id, message_id):
		method = {
			"method":"setPinMessage",
			"input":{
				"action":"Pin",
			 	"message_id": message_id,
			 	"object_guid": chat_id
			},
			"client": clients.android
		}
		return self.excute(method)
		
		
	def UnPin_Message(self, chat_id, message_id):
		method = {
			"method":"setPinMessage",
			"input":{
				"action":"Unpin",
			 	"message_id": message_id,
			 	"object_guid": chat_id
			},
			"client": clients.android
		}
		return self.excute(method)
		
		
	def Get_Messages(self, chat_id, min_id):
		method = {
		    "method":"getMessagesInterval",
		    "input":{
		        "object_guid":chat_id,
		        "middle_message_id":min_id
			},
			"client": clients.android
		}
		return self.excute(method)
		
	def GetGroup_Admins(self, chat_id):
		method = {
			"method":"getGroupAdminMembers",
			"input":{
				"group_guid":chat_id
			},
			"client": clients.android
		}
		return self.excute(method)

	def getLinkFromAppUrl(self, app_url):
		method = {
			"method":"getLinkFromAppUrl",
			"input":{
				"app_url":app_url
			},
			"client": clients.android
		}
		return self.excute(method).get("data").get("link").get("open_chat_data")
		
	def getChats(self, start_id=None):
		method = {
		    "method":"getChats",
		    "input":{
		        "start_id":start_id
			},
			"client": clients.web
		}
		return self.excute(method).get("data").get("messages")
		
		
	def getGroupMembers(self, chat_id, start_id=None):
		method = {
			"method":"getGroupAllMembers",
			"input":{
				"group_guid": chat_id,
				"start_id": start_id
			},
			"client": clients.web
		}
		return self.excute(method)