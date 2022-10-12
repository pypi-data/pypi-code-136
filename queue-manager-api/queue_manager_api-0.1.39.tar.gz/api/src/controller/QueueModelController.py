from python_framework import Controller, ControllerMethod, HttpStatus

from enumeration.AccessDomain import AccessDomain
import QueueDto


@Controller(
    url = '/queue',
    tag = 'Queue',
    description = 'Queue controller'
    # , logRequest = True
    # , logResponse = True
)
class QueueModelController:

    @ControllerMethod(url = '/',
        apiKeyRequired = [AccessDomain.API],
        requestClass = [QueueDto.QueueRequestDto],
        responseClass = [QueueDto.QueueResponseDto]
    )
    def post(self, dto):
        return self.service.queueModel.createOrUpdate(dto), HttpStatus.CREATED


@Controller(
    url = '/queue/all',
    tag = 'Queue',
    description = 'Queue controller'
    # , logRequest = True
    # , logResponse = True
)
class QueueModelAllController:

    @ControllerMethod(url = '/',
        apiKeyRequired = [AccessDomain.API],
        responseClass = [[QueueDto.QueueResponseDto]]
    )
    def get(self):
        return self.service.queueModel.findAllByOrigin(), HttpStatus.OK
