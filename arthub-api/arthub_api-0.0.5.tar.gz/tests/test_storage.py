import pytest
import logging
from arthub_api import arthub_api_config
from arthub_api import (
    OpenAPI,
    Storage,
    api_config_qq
)
import time

open_api = OpenAPI(api_config_qq)
storage = Storage(open_api)


def on_api_failed(res):
    logging.error("[TEST][STORAGE] \"%s\" failed, error: %s" % (res.url, res.error_message()))


def on_operation_failed(operation, error_message):
    logging.error("[TEST][STORAGE] %s failed, error: %s" % (operation, error_message))


@pytest.mark.run(order=1)
def test_login():
    res = open_api.login(arthub_api_config.account_email, arthub_api_config.password)
    if not res.is_succeeded():
        on_api_failed(res)
        pytest.exit("login failed, exit test", returncode=1)

    logging.info("[TEST][STORAGE] \"%s\" success, token: %s" % (res.url, res.results.get(0)["arthub_token"]))


@pytest.mark.run(order=2)
def test_transfer(tmp_path):
    # download
    since = time.time()
    res = storage.download_by_path(asset_hub="trial",
                                   remote_node_path="sdk_test/storage_test/download",
                                   local_dir_path=str(tmp_path),
                                   same_name_override=False)
    if not res.is_succeeded():
        on_operation_failed("download", res.error_message())
        assert 0
    local_downloaded_path = res.data[0]
    logging.info("[TEST][STORAGE] download success, local downloaded path: %s, spend: %f s"
                 % (local_downloaded_path, time.time() - since))
    since = time.time()

    # upload downloaded dir
    res = storage.upload_to_directory_by_path(asset_hub="trial",
                                              remote_dir_path="sdk_test/storage_test/upload",
                                              local_path=local_downloaded_path,
                                              tags_to_create=["sdk_test"],
                                              same_name_override=False,
                                              need_convert=True)
    if not res.is_succeeded():
        on_operation_failed("upload", res.error_message())
        assert 0
    logging.info("[TEST][STORAGE] upload success, remote uploaded id: %d, spend: %f s"
                 % (res.data[0], time.time() - since))


def test_get_node_by_path():
    res = storage.get_node_by_path(asset_hub="trial", remote_node_path="sdk_test/storage_test/download")
    if not res.is_succeeded():
        on_operation_failed("get remote node info", res.error_message())
        assert 0
    logging.info("[TEST][STORAGE] get remote node info success, id: %d, type: %s" % (res.data["id"], res.data["type"]))


def test_delete_node_by_path():
    res = storage.delete_node_by_path(asset_hub="trial", remote_node_path="sdk_test/storage_test/upload")
    if not res.is_succeeded():
        on_operation_failed("delete remote node info", res.error_message())
        assert 0
    logging.info("[TEST][STORAGE] delete remote node %d success" % res.data)
