try:
	import yaml
except ImportError:
	print("'yaml' module not found. Please install")
	exit(1)

class Creds:
	__filepath = None
	__logger = None
	__kvstore = None

	def __init__(self, filepath, logger):
		self.__filepath = filepath
		self.__logger = logger
		self.__kvstore = None
		try:
			self.load_creds()
		except:
			pass

	def creds_filepath(self):
		return self.__filepath

	def load_creds(self):
		try:
			with open(self.__filepath, 'r') as f:
				self.__kvstore = yaml.safe_load(f)
			self.__logger.debug("Loaded user creds from file %s" % (self.__filepath))
			return self.__kvstore
		except FileNotFoundError:
			return None
		except Exception as e:
			raise Exception("Failed to load user creds from %s: %s" % (self.__filepath, str(e)))

	def save_creds(self):
		try:
			with open(self.__filepath, 'w+') as f:
				yaml.dump(self.__kvstore, f)
			self.__logger.debug("Saved user creds to file %s" % (self.__filepath))
		except Exception as e:
			raise Exception("Failed to save user creds to file %s: %s" % (self.__filepath, str(e)))

	def get_cred(self, key):
		try:
			if not self.__kvstore or key not in self.__kvstore:
				return None
			return self.__kvstore[key]
		except Exception as e:
			raise Exception('get_cred(%s): %s' % (key, str(e)))

	def add_or_update_cred(self, key, val):
		try:
			if not self.__kvstore:
				self.__kvstore = {}
			self.__kvstore[key] = val
			self.save_creds()
		except Exception as e:
			raise Exception('add_or_update_cred(%s, %s(: %s' % (key, val, str(e)))

	def delete_cred(self, key):
		try:
			if self.__kvstore and key in self.__kvstore:
				self.__kvstore.pop(key)
				self.save_creds()
		except KeyError:
			pass
