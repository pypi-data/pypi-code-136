import fastapi, uvicorn, threading, types
from . import models



basic_types = {str, int, float, bool, None, types.NoneType}
"""Basic immutable types that can be sent as-is over the network"""

requested_objects = {}
"""Previously requested objects, from where they can be (re-)retrieved by id"""



class Server:
	# TODO implement some security

	def __init__(self, port: int, namespace):
		"""
		Opens the Python namespace for remote control of objects and variables.
		Without port forwarding works only on internal network, which is probably for the best. \n
		NOTE: Currently not secure in the slightest -
		anyone on the same network can access it just by knowing the port.

		:param port: any unique port for your program (use the same one on client)
		:param namespace: The starting point from the client's POV.
						  Tip: you can use __import__(__name__) if you want the current module.
		"""
		self.port = port
		self.namespace = namespace
		self.fastapi = fastapi.FastAPI()

		@self.fastapi.get('/root')
		def root():
			"""Get the id of the root object"""
			return _object_info(self.namespace)

		@self.fastapi.get('/getattr')
		def get_object_attr(id: int, attribute: str):
			try:
				object = getattr(requested_objects[id], attribute)
			except AttributeError as e:
				raise fastapi.HTTPException(404, str(e))
			return _object_info(object)

		@self.fastapi.get('/iterate')
		def iterate_object(id: int):
			try:
				object = requested_objects[id]
			except KeyError as e:
				raise fastapi.HTTPException(404, str(e))
			return [_object_info(i) for i in object]

		@self.fastapi.post('/call')
		def call_object(id: int, params: models.CallParameters):
			try:
				object = requested_objects[id]
			except KeyError as e:
				raise fastapi.HTTPException(404, str(e))
			result = params.use_on(object)
			return _object_info(result)

	def start(self, log=False):
		if log:
			log_level = None
		else:
			log_level = 'critical'
		uvicorn.run(self.fastapi, host='0.0.0.0', port=self.port, log_level=log_level)

	def start_in_thread(self, log=False):
		threading.Thread(target=self.start, kwargs={'log': log}, daemon=True).start()





def _object_info(object):
	object_id = id(object)
	basic = (type(object) in basic_types)

	requested_objects[object_id] = object
	
	return models.ObjectInfo(
		id=object_id,
		basic=basic,
		value=object if basic else None
	)
