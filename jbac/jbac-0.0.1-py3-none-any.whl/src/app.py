import os
import sys
import yaml
import json
import requests
import re

from argsy import Argsy
from dotenv import load_dotenv
from pkg_resources import resource_filename


class JBAC:
    def __init__(
        self,
        route: str,
        config_file_path: str = None,
        cert_file_path: str = None,
        verbose: bool = False,
        method: str = "GET",
        user_params: str = None,
        data: str = None,
        data_file_path: str = None,
        graphql_query_file: str = None,
        graphql_vars: str = None,
        dry_run: bool = False,
    ) -> None:
        self._route = route
        self._data_path_file = data_file_path
        self._data = data
        self._graphql_query_file = graphql_query_file
        self._graphql_vars = graphql_vars
        self._url = self._route
        self._config_file_path = os.path.abspath(config_file_path)
        self._config = None
        self._cert_file_path = cert_file_path
        self._verbose = False if verbose is None else True
        self._dry_run = False if dry_run is None else True
        self._method = method
        self._headers = {}
        self._params = {}  # Init params for config updates
        self._user_params = user_params
        self._try_load_config()  # Overlay user params last
        self._try_load_data()
        self._finalize()

    def _print(self, msg: str):
        if self._verbose:
            sys.stderr.write(f"{msg}\n")

    def _subst_env_in_dict_values(self, input_dict: dict):
        result = {}
        for k in input_dict.keys():
            result[k] = self._subst_env(input_dict[k])
        return result

    def _subst_env(self, input_str: str):
        regex = re.compile("(\$\{\s*env\.(\w+)\s*\})")
        found = regex.findall(input_str)

        for match in found:
            to_replace = match[0]
            env_var_name = match[1]
            input_str = input_str.replace(to_replace, os.environ[env_var_name])

        return input_str

    def _finalize(self):
        if self._user_params is not None:
            user_params = {}
            pairs = self._user_params.split(",")
            for pair in pairs:
                parts = pair.split("=")
                key = parts[0]
                value = parts[1]
                user_params[key] = value
            self._params.update(user_params)

    def _try_load_data(self):
        if self._graphql_query_file is not None:
            query_dict = {}
            query_str = open(self._graphql_query_file, "r").read()
            query_str = re.sub(r"\s+", " ", query_str)
            query_dict["query"] = query_str

            if self._graphql_vars is not None:
                query_vars = {}
                pairs = self._graphql_vars.split(",")
                for pair in pairs:
                    parts = pair.split("=")
                    key = parts[0]
                    value = parts[1]
                    query_vars[key] = value
                query_dict["variables"] = query_vars

            self._data = json.dumps(query_dict)

        elif self._data is None:
            if self._data_path_file is not None:
                with open(self._data_path_file, "r") as data_file:
                    self._data = data_file.read()

    def _try_load_config(self):
        self._try_load_config_from_file(path=self._config_file_path)

    def _try_load_config_from_file(self, path: str):
        self._print(f"trying to load config from '{path}'")
        if path is not None:
            self._print("config_file_path is not None")
            if os.path.isfile(path):
                self._print(f"file at '{path}' exists")
                with open(path, "r") as config_yaml:
                    config = yaml.load(config_yaml, Loader=yaml.SafeLoader)

                    if config.get("extends") is not None:
                        self._try_load_config_from_file(path=config.get("extends"))

                    if config.get("method") is not None:
                        self._method = config.get("method")

                    if config.get("headers") is not None:
                        self._headers.update(
                            self._subst_env_in_dict_values(config.get("headers"))
                        )

                    if config.get("params") is not None:
                        self._params.update(config.get("params"))

                    if config.get("cert_file") is not None:
                        self._cert_file_path = config.get("cert_file")

                    if config.get("url") is not None:
                        self._url = f"{ config.get('url').get('base') }{ self._route }"

            else:
                self._print("file at config_file_path does not exist")
        else:
            self._print("config_file_path is None")

    def send(self):
        if self._dry_run:
            return json.dumps(
                dict(request=self._to_dict(), response=dict(dry_run=True))
            )

        self._print(json.dumps(self.__dict__))
        self._response = requests.request(
            method=self._method,
            headers=self._headers,
            params=self._params,
            url=self._url,
            verify=self._cert_file_path,
            data=self._data,
        )
        self._print(str(self._response.__dict__))

        body = None
        try:
            body = json.loads(self._response.content.decode("utf-8"))
        except:
            body = self._response.content.decode("utf-8")

        return json.dumps(
            dict(
                request=self._to_dict(),
                response=dict(
                    status_code=self._response.status_code,
                    headers=dict(self._response.headers),
                    body=body,
                ),
            )
        )

    def _to_dict(self):
        return dict(
            method=self._method,
            route=self._route,
            url=self._url,
            headers=self._headers,
            params=self._params,
            config_file_path=self._config_file_path,
            cert_file_path=self._cert_file_path,
            graphql_query_file=self._graphql_query_file,
            data=self._data,
        )


def main():
    load_dotenv()

    parsed_args = (
        Argsy(config_file_name=resource_filename("src", "cfg/args.yaml"))
        .parse_args(sys.argv[1:])
        .get("args")
    )
    
    print(
        JBAC(
            config_file_path=parsed_args.get("config_file_path"),
            cert_file_path=parsed_args.get("cert_file_path"),
            verbose=parsed_args.get("verbose"),
            method=parsed_args.get("method"),
            route=parsed_args.get("route"),
            user_params=parsed_args.get("params"),
            data=parsed_args.get("data"),
            data_file_path=parsed_args.get("data_file_path"),
            graphql_query_file=parsed_args.get("graphql_query_file"),
            graphql_vars=parsed_args.get("graphql_vars"),
            dry_run=parsed_args.get("dry_run"),
        ).send()
    )
