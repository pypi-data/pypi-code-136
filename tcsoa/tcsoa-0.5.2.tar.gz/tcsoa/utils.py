from dataclasses import field, dataclass
from typing import Dict, List, Optional

from tcsoa.config import TcSoaConfig


class TcBaseObj(object):
    def __getitem__(self, item):
        """ Makes the object subscriptable - you may use dict index access """
        return getattr(self, item)


@dataclass
class TcBoClass(TcBaseObj):
    uid: str = ''
    objectID: str = ''
    type: str = ''
    className: str = ''
    props: Dict[str, Dict[str, List[str]]] = field(default_factory=dict)

    def prop(self, prop_name, db_value=False) -> List[Optional[str]]:
        if TcSoaConfig.global_obj_cache_enabled:
            prop = TcSoaConfig.internal_get_prop(self.uid, prop_name)
        else:
            prop = None
            if self.props and prop_name in self.props:
                prop = self.props[prop_name]
        if prop:
            attr = 'dbValues' if db_value else 'uiValues'
            if attr in prop:
                if 'isNulls' in prop:
                    return [None if prop['isNulls'][idx] else val for idx, val in enumerate(prop[attr])]
                return prop[attr]
        return [None]


class TcService:
    @classmethod
    def execute_soa_method(cls, method_name, library, service_date, service_name, params, response_cls):
        service_id = f'{library}-{service_date.replace("_", "-")}-{service_name}'
        return TcSoaConfig.backend.execute(service_id, method_name, params, response_cls)
