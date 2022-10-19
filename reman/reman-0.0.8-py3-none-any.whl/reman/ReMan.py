from ast import Raise
import mariadb
import sys

class ReMan(object):
	def __init__(self):
		self.connection = None
		self.cursor = None

	def __del__(self):
		if (self.cursor != None):
			self.cursor.close()
		if (self.connection != None):
			self.connection.close()

	def getDBConnection(self):
		try:
			if (self.connection == None):
				self.connection = mariadb.connect(
					user="reman",
					password="reman",
					host="10.58.3.179",
					database="REMAN")
			return self.connection
		except Exception as e:
			print(f"Failed to connect database, error: {e}")
			sys.exit(1)

	def getDBCursor(self):
		try:
			if (self.cursor == None):
				self.cursor = self.getDBConnection().cursor()
			return self.cursor
		except Exception as e:
			print(f"Failed to get database cursor, error: {e}")
			sys.exit(1)

	def getUserChannels(self, releaseName):
		result = None
		try:
			cursor = self.getDBCursor()
			cursor.execute("SELECT users.name, channels.name "
							"FROM ReleaseChannel as rc "
							"INNER JOIN Channels as channels ON rc.channelId = channels.id "
							"INNER JOIN Users as users ON users.id = channels.userId "
							"INNER JOIN Releases as releases ON  rc.releaseId = releases.id "
							f"WHERE releases.name = '{releaseName}'"
							)
			result = self.getDBCursor().fetchall()
		except Exception as e:
			print(f"Failed to get user/channel of {releaseName}, error: {e}")
		return result

	def getChannel(self, releaseName, userName):
		result = None
		try:
			cursor = self.getDBCursor()
			cursor.execute("SELECT channels.name "
							"FROM ReleaseChannel as rc "
							"INNER JOIN Channels as channels ON rc.channelId = channels.id "
							"INNER JOIN Users as users ON users.id = channels.userId "
							"INNER JOIN Releases as releases ON  rc.releaseId = releases.id "
							f"WHERE releases.name = '{releaseName}' "
							f"AND users.name = '{userName}'"
							)
			rows = self.getDBCursor().fetchall()
			if (len(rows) == 1):
				result = rows[0][0]
			else:
				print("None or multiple version! " + len(rows))
		except Exception as e:
			print(f"Failed to get user/channel of {releaseName}, error: {e}")
		return result

	def createRelease(self, originReleaseName, newReleaseName):
		self.getReleaseId(newReleaseName)
		if self.getReleaseId(newReleaseName):
			print("release already exists")
			return
		existingChannels = None
		if originReleaseName:
			existingChannels = self.getUserChannels(originReleaseName)
			if not existingChannels:
				print("Cannot create release from {originReleaseName}")
				raise
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"INSERT INTO Releases (name) VALUES ('{newReleaseName}')")
		except Exception as e:
			print(f"Failed to create {originReleaseName}, error: {e}")
			self.getDBConnection().rollback()
			raise
		# if originReleaseName is provided, copy all channels from it to the new release
		if originReleaseName:
			newReleaseId = self.getReleaseId(newReleaseName)
			print(f"## newReleaseId: {newReleaseId}")
			try:
				for channel in existingChannels:
					channelId = self.getChannelId(channel[1], self.getUserId(channel[0]))
					cursor.execute(f"INSERT INTO ReleaseChannel (releaseId, channelId) VALUES ({newReleaseId}, {channelId})")
			except:
				print(f"failed to insert channel {channel[1]} in release, error: {e}")
				self.getDBConnection().rollback()
				raise
		self.getDBConnection().commit()

	def getReleaseId(self, releaseName):
		result = None
		try:
			cursor = self.getDBCursor()
			print(f"getting id for rel: {str(releaseName)}")
			command = f"SELECT id FROM Releases WHERE name = '{str(releaseName)}'"
			cursor.execute(command)
			rows = self.getDBCursor().fetchall()
			print(f"command: {command}")
			if (len(rows) == 1):
				result = rows[0][0]
			else:
				print("None or multiple releseIds! " + len(rows))
		except Exception as e:
			print(f"Failed to get releaseId of {releaseName}, error: {e}")
		print(f"--> getReleaseId {result}")
		return result

	def createUser(self, userName):
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"INSERT INTO Users (name) VALUES ('{userName}')")
		except Exception as e:
			print(f"Failed to create user {userName}, error: {e}")
			self.getDBConnection().rollback()
			raise
		self.getDBConnection().commit()
	
	def getUserId(self, userName):
		result = None
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"SELECT id FROM Users WHERE name = '{userName}'")
			rows = self.getDBCursor().fetchall()
			if (len(rows) == 1):
				result = rows[0][0]
			else:
				print("None or multiple userIds! " + len(rows))
		except Exception as e:
			print(f"Failed to get userId of {userName}, error: {e}")
		return result

	def createChannel(self, userName, channelName):
		userId = self.getUserId(userName)
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"INSERT INTO Channels (name, userId) VALUES ('{channelName}', {userId})")
		except Exception as e:
			print(f"Failed to create channel {channelName}, error: {e}")
			self.getDBConnection().rollback()
			raise
		self.getDBConnection().commit()
	
	def getChannelId(self, channelName, userId):
		result = None
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"SELECT id FROM Channels WHERE name = '{channelName}' AND userId = {userId}")
			rows = self.getDBCursor().fetchall()
			if (len(rows) == 1):
				result = rows[0][0]
			else:
				print("None or multiple channelIds! " + len(rows))
		except Exception as e:
			print(f"Failed to get id of {channelName}, error: {e}")
		return result

	def linkReleaseChannel(self, releaseName, userName, channelName):
		releaseId = self.getReleaseId(releaseName)
		channelId = self.getChannelId(channelName, self.getUserId(userName))
		previousChannelId = self.getChannelId(self.getChannel(releaseName, userName), self.getUserId(userName))
		try:
			cursor = self.getDBCursor()
			cursor.execute(f"UPDATE ReleaseChannel Set channelId = {channelId} "
							f"WHERE releaseId = {releaseId} and channelId = {previousChannelId}")
		except:
			print("Failed to set new cahnnel for release")
			self.getDBConnection().rollback()
			raise
		self.getDBConnection().commit()