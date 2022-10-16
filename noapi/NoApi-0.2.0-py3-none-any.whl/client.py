import requests
from . import models



# noinspection PyProtectedMember
class RemoteObject:

	# The three-underscore (tunder?) methods and variables:
	#
	# Their purpose is to be seperated from a method on the actual remote object.
	# When an attribute is called, and it's surrounded by '___', it gets called on this object,
	# instead of being sent to the server.

	def __init__(self, id: int, client):
		self.___id___ = id
		self.___client___ = client


	def __getattribute__(self, name: str):
		methods = {}
		if name.startswith('___') and name.endswith('___') or name in {'__call__', '__init__', '__iter__'}:
			return object.__getattribute__(self, name)
		else:
			return self.___client___.___call_server___('get', 'getattr', id=self.___id___, attribute=name)


	# TODO also set attribute


	def __call__(self, *args, **kwargs):
		args = [models.Arg.generate(a) for a in args]
		kwargs = {key: models.Arg.generate(a) for (key, a) in kwargs.items()}
		return self.___client___.___call_server___('post', 'call', id=self.___id___,
		                                           data=models.CallParameters(args=args, kwargs=kwargs).dict())


	def __iter__(self):
		list = self.___client___.___call_server___('get', 'iterate', id=self.___id___)
		return list.__iter__()

	def __getitem__(self, item):
		return self.__getitem__(item)





class Client(RemoteObject):

	def __init__(self, server_address: str, port: int):
		"""
		Gateway to variables and objects on a remote machine
		
		:param server_address: address/ip of the server
		:param port: a unique port for your program (use the same one on server)
		"""
		self.___server_address___ = f"{server_address}:{port}"
		if not self.___server_address___.startswith('http'):  # TODO figure out https
			self.___server_address___ = 'http://' + self.___server_address___
		self.___session___ = requests.Session()
		self.___cached_root_id___ = None
		super().__init__(0, self)


	def ___call_server___(self, method: str, function: str, data=None, **params):
		method = getattr(self.___session___, method)
		url = f'{self.___server_address___}/{function}'
		response = method(url, json=data, params=params)
		json = response.json()

		match response.status_code:
			case 200:
				def parse(json):
					object = models.ObjectInfo.construct(None, **json)
					if object.basic:
						return object.value
					else:
						return RemoteObject(object.id, self)

				if isinstance(json, list):
					return [parse(i) for i in json]
				else:
					return parse(json)

			case 404:
				raise ObjectNotFoundError(response)
			case _:
				raise InternalNoApiError(response)

	@property
	def ___id___(self):
		if self.___cached_root_id___ is None:
			self.___cached_root_id___ = self.___call_server___('get', 'root').___id___
		return self.___cached_root_id___

	@___id___.setter
	def ___id___(self, id: int):
		pass





class ServerError(BaseException):
	def __init__(self, message, server_response: requests.Response):
		super().__init__(f"{message} (message: {server_response.json()['detail']})")


class ObjectNotFoundError(ServerError):
	def __init__(self, response: requests.Response):
		super().__init__(f"object not found on server", response)

class InternalNoApiError(ServerError):
	def __init__(self, response: requests.Response):
		super().__init__(f"Internal error with NoApi server - {response.status_code}", response)
