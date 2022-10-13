import flask

from infosystem.common import utils
from infosystem.common.subsystem import controller
from infosystem.common import exception


class Controller(controller.Controller):

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def get_tags_from_entity(self):
        filters = self._filters_parse()
        filters = self._filters_cleanup(filters)

        try:
            filters = self._parse_list_options(filters)
            tags = self.manager.get_tags_from_entity(**filters)
        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)
        except ValueError:
            raise exception.BadRequest('page or page_size is invalid')

        collection = tags

        response = {self.collection_wrap: collection}

        return flask.Response(response=utils.to_json(response),
                              status=200,
                              mimetype="application/json")
