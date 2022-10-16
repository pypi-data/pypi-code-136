import pydantic, typing
from . import server, client



class ObjectInfo(pydantic.BaseModel):

	id: int
	basic: bool
	value: typing.Any



class Arg(pydantic.BaseModel):

	value: typing.Any
	remote_object: bool = False

	@classmethod
	def generate(cls, value):
		if type(value) == client.RemoteObject:
			return cls(value=value.___id___, remote_object=True)
		else:
			return cls(value=value, remote_object=False)

	def parse(self):
		if self.remote_object:
			return server.requested_objects[self.value]
		else:
			return self.value



class CallParameters(pydantic.BaseModel):

	args: list[Arg]
	kwargs: dict[str, Arg]

	def use_on(self, object):
		args = [a.parse() for a in self.args]
		kwargs = {key: arg.parse() for (key, arg) in self.kwargs.items()}
		return object(*args, **kwargs)
