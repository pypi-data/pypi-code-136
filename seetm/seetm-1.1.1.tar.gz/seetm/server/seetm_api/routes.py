import json
import logging

from flask import (
    send_from_directory,
    request,
)
from flask_cors import cross_origin

from seetm.server.seetm_api import blueprint
from seetm.server.seetm_api.utils.server_configs import ServerConfigs
from seetm.shared.constants import (
    ServerConfigType,
    TOKEN_TO_TOKEN_MAP_PATH,
    FilePermission,
    Encoding,
)

logger = logging.getLogger(__name__)


@blueprint.route("/", strict_slashes=False, methods=['GET'])
@blueprint.route("/status", strict_slashes=False, methods=['GET'])
@cross_origin()
def api_status():
    logger.debug("Status API endpoint was called")
    return {
        "endpoint": "/api/seetm/",
        "status": "ok",
        "environment": "production",
    }


@blueprint.route("/maps", strict_slashes=False, methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def maps():
    logger.debug("Maps API endpoint was called")
    if request.method == "GET":
        try:
            with open(
                    file=TOKEN_TO_TOKEN_MAP_PATH,
                    mode=FilePermission.READ,
                    encoding=Encoding.UTF8
            ) as token_to_token_map_file:
                token_to_token_maps = json.load(fp=token_to_token_map_file)

            return {"status": "success", "maps": token_to_token_maps}, 200
        except Exception as e:
            logger.error(f"Exception occurred while retrieving the maps. {e}")
            return {"status": "error"}, 700

    elif request.method == "POST":
        try:
            request_data = request.get_json()
            map_ = request_data['map']

            with open(
                    file=TOKEN_TO_TOKEN_MAP_PATH,
                    mode=FilePermission.READ,
                    encoding=Encoding.UTF8
            ) as token_to_token_map_file:
                token_to_token_maps = json.load(fp=token_to_token_map_file)

            token_to_token_maps.update(map_)
            with open(TOKEN_TO_TOKEN_MAP_PATH, encoding=Encoding.UTF8, mode=FilePermission.WRITE) as updated_map:
                json.dump(token_to_token_maps, updated_map, ensure_ascii=False, indent=4)

            return {"status": "success", "maps": token_to_token_maps}, 200
        except Exception as e:
            logger.error(f"Exception occurred while persisting the map. {e}")
            return {"status": "error"}, 701

    elif request.method == "DELETE":
        try:
            request_data = request.get_json()
            base_token = request_data["base_token"]

            with open(
                    file=TOKEN_TO_TOKEN_MAP_PATH,
                    mode=FilePermission.READ,
                    encoding=Encoding.UTF8
            ) as token_to_token_map_file:
                token_to_token_maps = json.load(fp=token_to_token_map_file)

            if base_token in token_to_token_maps:
                del token_to_token_maps[base_token]

            with open(TOKEN_TO_TOKEN_MAP_PATH, encoding=Encoding.UTF8, mode=FilePermission.WRITE) as updated_map:
                json.dump(token_to_token_maps, updated_map, ensure_ascii=False, indent=4)

            return {"status": "success", "maps": token_to_token_maps}, 200
        except Exception as e:
            logger.exception(f"Exception occurred while deleting the map. {e}")
            return {"status": "error"}, 702

    elif request.method == "PUT":
        try:
            request_data = request.get_json()
            previous_base_token = request_data["previous_base_token"]
            updated_map = request_data["updated_map"]

            with open(
                    file=TOKEN_TO_TOKEN_MAP_PATH,
                    mode=FilePermission.READ,
                    encoding=Encoding.UTF8
            ) as token_to_token_map_file:
                token_to_token_maps = json.load(fp=token_to_token_map_file)

            print(token_to_token_maps)
            if previous_base_token in token_to_token_maps:
                del token_to_token_maps[previous_base_token]

            if list(updated_map.keys())[0] in token_to_token_maps:
                del token_to_token_maps[list(updated_map.keys())[0]]

            token_to_token_maps.update(updated_map)
            with open(TOKEN_TO_TOKEN_MAP_PATH, encoding=Encoding.UTF8, mode=FilePermission.WRITE) as updated_map:
                json.dump(token_to_token_maps, updated_map, ensure_ascii=False, indent=4)

            return {"status": "success", "maps": token_to_token_maps}, 200
        except Exception as e:
            logger.exception(f"Exception occurred while deleting the map. {e}")
            return {"status": "error"}, 703


@blueprint.route("/configs", strict_slashes=False, methods=['GET', 'POST'])
@cross_origin()
def configs():
    logger.debug("Configs API endpoint was called")
    server_configs = ServerConfigs()

    if request.method == 'POST':
        return {}
    else:
        try:
            server_configs_json = server_configs.retrieve(
                config_type=ServerConfigType.JSON,
                custom_configs=True
            )
            return {"status": "success", "configs": server_configs_json}
        except Exception as e:
            logger.error(f"Exception occurred while retrieving the server configurations. {e}")
            return {"status": "error"}


@blueprint.route("/<path:path>", strict_slashes=False)
@cross_origin()
def api_static_files(path):
    logger.debug("API static files are served")
    if path != 'seetm.png':
        return {"status": "error", "message": "Not Authorized"}, 403
    return send_from_directory(directory=blueprint.static_folder, path=path), 200
