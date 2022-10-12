from copy import copy
from dataclasses import dataclass
import importlib.util
import sys
from typing import Any, Callable, List, Tuple
import grpc
from concurrent import futures

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.collection import ServiceRoleBaseValue, ServiceRoleValue
from pih.const import ServiceCommands, ServiceRoles
import pih.rpcCommandCall_pb2_grpc as pb2_grpc
import pih.rpcCommandCall_pb2 as pb2
from pih.tools import DataTools, EnumTools, ParameterList

@dataclass
class Error(BaseException):
    details: str
    code: Tuple

class RPC:

    @staticmethod
    def create_error(context, message: str = "", code: Any = None) -> Any:
        context.set_details(message)
        context.set_code(code)
        return pb2.rpcCommandResult()

    class UnaryService(pb2_grpc.UnaryServicer):

        def __init__(self, role: ServiceRoles, handler: Callable, *args, **kwargs):
            self.role = role
            self.handler = handler

        def internal_handler(self, command_name: str, parameters: str, context) -> dict:
            print(f"rpc call: {command_name}")
            command: ServiceCommands = EnumTools.get(ServiceCommands, command_name)
            if command is not None:
                if command == ServiceCommands.ping:
                    service_role_info: dict = copy(DataTools.to_data(self.role.value))
                    del service_role_info["modules"]
                    del service_role_info["commands"]
                    return service_role_info
            return self.handler(command_name, ParameterList(parameters), context)

        def rpcCallCommand(self, command, context):
            parameters = command.parameters
            if not DataTools.is_empty(parameters):
                parameters = DataTools.rpc_unrepresent(parameters)
            return pb2.rpcCommandResult(data=DataTools.represent(self.internal_handler(command.name, parameters, context)))

    class Service:


        @staticmethod
        def serve(role: ServiceRoles, handler: Callable, debug: bool = False) -> None:
            from pih.pih import PIH, PR
            PR.init()

            service_role_value: ServiceRoleValue = role.value
            parameter_debug = PIH.SESSION.argv(1)
            if parameter_debug is not None:
                debug = parameter_debug.lower() == "true"
            service_role_value.debug = debug
            service_host: str = PIH.SERVICE.get_host(role)
            service_port: int = PIH.SERVICE.get_port(role)
            service_role_value.pih_version = PIH.VERSION.local()
            service_role_value.pid = PIH.OS.get_pid()
            PIH.VISUAL.service_header(role)
            PR.good(f"Сервис был запущен!")
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            pb2_grpc.add_UnaryServicer_to_server(
                RPC.UnaryService(role, handler), server)
            try:
                server.add_insecure_port(f"{service_host}:{service_port}")
                server.start()
                while role == ServiceRoles.LOG:
                    if PIH.SERVICE.check_availability(ServiceRoles.LOG):
                        break
                PIH.MESSAGE.COMMAND.service_started(role)
                server.wait_for_termination()
            except RuntimeError as error:
                pass
                #PIH.MESSAGE.COMMAND.service_not_started(role)

    class CommandClient():

        def __init__(self, host: str, port: int):
            self.stub = pb2_grpc.UnaryStub(grpc.insecure_channel(f"{host}:{port}"))

        def call_command(self, name: str, parameters: str = None):
            return self.stub.rpcCallCommand(pb2.rpcCommand(name=name, parameters=parameters))

    @staticmethod
    def ping(role: ServiceRoles) -> ServiceRoleBaseValue:
        try:
            return DataTools.fill_data_from_rpc_str(ServiceRoleBaseValue(), RPC.internal_call(role, ServiceCommands.ping))
        except Error:
            return None

    @staticmethod
    def internal_call(role: ServiceRoles, command: ServiceCommands, parameters: Any = None) -> str:
        PIH = sys.modules["pih.pih"].PIH
        PIH.SERVICE.init()
        try:
            if role is None:
                role = PIH.SERVICE.get_role_by_command(command)
            service_host: str = PIH.SERVICE.get_host(role)
            service_port: int = PIH.SERVICE.get_port(role)
            return RPC.CommandClient(service_host, service_port).call_command(command.name, DataTools.rpc_represent(parameters)).data
        except grpc.RpcError as error:
            code: Tuple = error.code()
            details: str = f"\nService host: {service_host}\nService port: {service_port}\nCommand: {command.name}\nDetails: {error.details()}\nCode: {code}"
            PIH.ERROR.rpc_error_handler(details, code, role, command)

    @staticmethod
    def call(command: ServiceCommands, parameters: Any = None) -> str:
        return RPC.internal_call(None, command, parameters)