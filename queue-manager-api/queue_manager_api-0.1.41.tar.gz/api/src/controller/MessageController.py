from python_framework import Controller, ControllerMethod, HttpStatus

from enumeration.AccessDomain import AccessDomain
import MessageDto


@Controller(
    url = '/message/emitter',
    tag = 'Message',
    description = 'Message controller'
    # , logRequest = True
    # , logResponse = True
)
class MessageController:

    @ControllerMethod(url = '/',
        apiKeyRequired = [AccessDomain.API, AccessDomain.USER, AccessDomain.ADMIN],
        requestClass = [MessageDto.MessageRequestDto],
        responseClass = [MessageDto.MessageCreationResponseDto]
    )
    def post(self, dto):
        return self.service.message.accept(dto), HttpStatus.ACCEPTED


@Controller(
    url = '/message/emitter',
    tag = 'Message',
    description = 'Message controller'
    # , logRequest = True
    # , logResponse = True
)
class MessageAllController:

    @ControllerMethod(url = '/all',
        apiKeyRequired = [AccessDomain.ADMIN],
        requestParamClass = [MessageDto.MessageQueryRequestDto],
        responseClass = [[MessageDto.MessageQueryResponseDto]]
    )
    def get(self, params=None):
        return self.service.message.findAllByQuery(params), HttpStatus.OK
