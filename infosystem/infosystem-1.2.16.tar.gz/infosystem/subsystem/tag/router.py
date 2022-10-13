from infosystem.common.subsystem import router


class Router(router.Router):

    def __init__(self, collection, routes=[]):
        super().__init__(collection, routes)

    @property
    def routes(self):
        return super().routes + [
            {
                'action': 'get tags from an entity',
                'method': 'GET',
                'url': self.collection_url + '/get_tags_from_entity',
                'callback': 'get_tags_from_entity',
                'bypass': True
            },
        ]
