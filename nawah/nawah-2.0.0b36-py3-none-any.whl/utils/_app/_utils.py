"""Provides utilties used to manage Nawah App serving"""

import logging

from nawah.config import Config

logger = logging.getLogger("nawah")


def _populate_routes():
    get_routes = []
    post_routes = []
    for module_name, module in Config.modules.items():
        for func_name, func in module.funcs.items():
            if func.get_func:
                for get_args_set in func.query_attrs or [{}]:
                    get_args = ""
                    if get_args_set:
                        for query_attr in get_args_set:
                            # [TODO] Deprecated check. Remove with release
                            if ":" not in query_attr:
                                get_args += f"/{{{query_attr}}}"
                            else:
                                if query_attr.split(":")[1] != "$eq":
                                    raise Exception(
                                        "Nawah Function '{module_name}.{func_name}' set exposed as "
                                        "GET endpoint must only define Query Attrs with Query "
                                        "Operators $eq"
                                    )
                                get_args += f"/{{{query_attr.split(':')[0]}}}"

                    get_routes.append(f"/{module_name}/{func_name}{get_args}")

            func.post_func = True
            if func.post_func:
                post_routes.append(f"/{module_name}/{func_name}")

    return (get_routes, post_routes)
