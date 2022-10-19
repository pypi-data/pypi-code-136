import asyncio, aiohttp, datetime, json

class SettingsClass:
	def __init__(self, token = None, apiTag = "tgn"):

		self.session = AIO() 
		self.apiSelection = {
			"tgn":"https://edu-tpi.donstu.ru/api/",
			"rnd":"https://edu.donstu.ru/api/"
		}
		self.url_api = self.apiSelection[apiTag]  
		self.params = {} 
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36",
			"Content-Type": "application/json; charset=utf-8"
		}
		if token is not None:
			self.headers["authorization"] = "Bearer {}".format(token)

class AIO:

	async def get(self, url, headers = None, params = None):
		async with aiohttp.ClientSession() as session:
			async with session.get(url=url, headers=headers, params=params) as res:
				if res.status != 200: 
					print('TEXT ERROR:',await res.text())
					return res.status
				return await res.json()

	async def post():
		pass

	async def delete():
		pass

	async def put():
		pass

	async def option():
		pass

class User(SettingsClass):
	
	async def infoAccount(self):
		return await self.session.get(f"{self.url_api}tokenauth", headers=self.headers)

	async def checking_unread_messages(self):
		return await self.session.get(f"{self.url_api}Mail/CheckMail", headers=self.headers)

	async def checking_all_mail(self, page: int = 1):
		return await self.session.get(f"{self.url_api}Mail/InboxMail?page=1&pageEl=15&unreadMessages=false&searchQuery=", headers=self.headers)

	async def read_mail_message(self, messageID):
		for msg in (await self.checking_all_mail())['data']['messages']:
			if msg['messageID'] == messageID:
				return (await self.session.get(f"{self.url_api}Mail/InboxMail?id={msg['id']}", headers=self.headers))['data']['messages'][0]

	async def find_stundent(self, fio):
		return await self.session.get(f"{self.url_api}Mail/Find/Students?fio={fio}", headers=self.headers)

	async def find_teacher(self, fio):
		return await self.session.get(f"{self.url_api}Mail/Find/Prepods?fio={fio}", headers=self.headers)

	async def all_groups_year(self, year: int = datetime.datetime.now().year):
		return await self.session.get(f"{self.url_api}groups?year={year}-{year+1}")

	# TODO: доделать
	async def send_message(self, statusID, from_user, title_message, text_message, type_message: int = 1):

		if statusID == 0:
			usertoID = await self.find_stundent(fio=from_user)['data']['arrStud']
		elif statusID == 1:
			usertoID = await self.find_teacher(fio=from_user)['data']['arrPrep']
		elif statusID == 2:
			pass

		data = {
			"markdownMessage": text_message,
			"htmlMessage": "",
			"message": "",
			"theme": title_message,
			"userToID": usertoID,
			"typeID": type_message,
		}
		req = self.session.post(f"{self.url_api}Mail/InboxMail", data=json.dumps(data), headers=self.headers)

	async def infoUser(self, userID):
		return await  self.session.get(f"{self.url_api}UserInfo/user?userID={userID}", headers=self.headers)

	async def infoStudent(self, studentID):
		return await self.session.get(f"{self.url_api}UserInfo/Student?studentID={studentID}", headers=self.headers)

	async def feed(self, userID):
		return await self.session.get(f"{self.url_api}Feed?userID={userID}&startDate=null", headers=self.headers)

	async def studentMark(self, studentID):
		return await self.session.get(f"{self.url_api}EducationalActivity/StudentAvgMark?studentI={studentID}", headers=self.headers)

	async def statisticsMarks(self, studentID):
		return await self.session.get(f"{self.url_api}EducationalActivity/StatisticsMarksCount?studentID={studentID}", headers=self.headers)

	async def listStudentsDebts(self, studentID):
		return await self.session.get(f"{self.url_api}StudentsDebts/list?studentID={studentID}", headers=self.headers)

	async def journalList(self):
		return await self.session.get(f"{self.url_api}Journals/JournalList", headers=self.headers, params = self.params)

	# TODO: доделать
	async def createChat(self, nameChat):
		data = {
			"channel": False,
			"chatUsers": [],
			"description": "",
			"name": nameChat,
		}

		res = self.session.post(f"{self.url_api}Chats/Chat", data=json.dumps(data), headers=self.headers)
		return res.text

	async def listWorks(self, typeVeref):
		return await self.session.get(f"{self.url_api}Portfolio/Verifier/ListWorks?finished=false&type={typeVeref}", headers=self.headers)

	async def filesList(self, workID):
		return await self.session.get(f"{self.url_api}Portfolio/FilesList?workID={workID}", headers=self.headers)
		
	def TestSend(self, params):
		return await self.session.get(f"{self.url_api}Mail/TestSend", headers=self.headers, params=params)

class Rasp(SettingsClass):

	def __str__(self):
		return "asyncio"

	async def infoRasp(self, groupID, sdate = datetime.datetime.now().strftime("%Y-%m-%d")):
		return await self.session.get(f"{self.url_api}Rasp?idGroup={groupID}&sdate={sdate}", headers=self.headers)

	async def GroupsRasp(self):
		return await self.session.get(f"{self.url_api}raspGrouplist", headers=self.headers)

	async def AudRasp(self, audCode, sdate = datetime.datetime.now().strftime("%Y-%m-%d")):
		return await self.session.get(f"{self.url_api}Rasp?idAudLine={audCode}&sdate={sdate}",headers=self.headers)

	async def AudsRasp(self):
		return await self.session.get(f"{self.url_api}raspAudlist", headers=self.headers)

	async def infoRaspTeacher(self, teacherID, sdate = datetime.datetime.now().strftime("%Y-%m-%d") ):
		return await self.session.get(f"{self.url_api}Rasp?idTeacher={teacherID}&sdate={sdate}", headers=self.headers)

	async def TeachersRasp(self):
		return await self.session.get(f"{self.url_api}raspTeacherlist", headers=self.headers)

class Journals(SettingsClass):

	async def List(self, params = None):
		return await self.session.get(f"{self.url_api}Journals/JournalList", headers=self.headers, params=params)

	async def AnotherTypes(self, journalID):
		return await self.session.get(f"{self.url_api}Journals/AnotherTypes?journalID={journalID}", headers=self.headers)

	async def Journal(self, journalID):
		return await self.session.get(f"{self.url_api}Journals/Journal?journalID={journalID}", headers=self.headers)

	async def JournalDate(self, journalID):
		return await self.session.get(f"{self.url_api}Journals/JournalDate?journalID={int(journalID)}", headers=self.headers)

	async def PostJournalDate(self, data):
		return await self.session.post(f"{self.url_api}Journals/JournalDate", headers=self.headers, data=json.dumps(data))

	async def JournalSave(self, data):
		return await self.session.get(f"{self.url_api}Journals/JournalSave", headers=self.headers, data=json.dumps(data))
