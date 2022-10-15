# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import json
import sys
from dataclasses import dataclass
from json import JSONDecodeError
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

import click
from click import Context

from tabulario.exceptions import InvalidInputError
from tabulario.oauth import ClientOauthTokenResponse, OAuthTokenResponse, TabularOAuth
from tabulario.util import EnhancedJSONEncoder


@dataclass(frozen=True)
class TabularContext:
    environment: str


@click.group()
@click.option("--environment", default="prod")
@click.pass_context
def run(ctx: Context, environment: str):
    ctx.obj = TabularContext(environment=environment)


def _read_stdin() -> Optional[Dict[str, Any]]:
    if not sys.stdin.isatty():
        try:
            raw_json = "\n".join(sys.stdin.readlines())
            if raw_json:
                return json.loads(raw_json)
        except JSONDecodeError as e:
            raise InvalidInputError("Invalid JSON") from e

    return None


def _out(output: Union[OAuthTokenResponse, ClientOauthTokenResponse]):
    click.echo(json.dumps(output, cls=EnhancedJSONEncoder))


@run.command()
@click.pass_obj
@click.argument("credential", required=False)
@click.argument("scopes", required=False, nargs=-1)
def request_token(ctx: TabularContext, credential: Optional[str], scopes: List[str]):
    """Retrieves an access token based on credentials"""
    args = _read_stdin()
    if not args:
        args = {"credential": credential, "scopes": scopes}
    token = TabularOAuth(ctx.environment).request_token(**args)
    _out(token)


@run.command()
@click.pass_obj
@click.argument("service_token", required=False)
@click.argument("service_token_type", required=False)
@click.argument("id_token", required=False)
@click.argument("id_token_type", required=False)
@click.argument("scopes", required=False, nargs=-1)
def request_user_token(
    ctx: TabularContext,
    service_token: Optional[str],
    service_token_type: Optional[str],
    id_token: Optional[str],
    id_token_type: Optional[str],
    scopes: List[str],
):
    """Retrieves a user token based on credentials"""
    args = _read_stdin()
    if not args:
        args = {
            "service_token": service_token,
            "service_token_type": service_token_type,
            "id_token": id_token,
            "id_token_type": id_token_type,
            "scopes": scopes,
        }
    token = TabularOAuth(ctx.environment).request_user_token(**args)
    _out(token)


@run.command()
@click.pass_obj
@click.argument("token", required=False)
@click.argument("token_type", required=False)
@click.argument("scopes", required=False, nargs=-1)
def refresh_token(ctx: TabularContext, token: Optional[str], token_type: Optional[str], scopes: List[str]):
    """Retrieves a fresh token based on an existing token"""
    args = _read_stdin()
    if not args:
        args = {"token": token, "token_type": token_type, "scopes": scopes}

    fresh_token = TabularOAuth(ctx.environment).refresh_token(**args)
    _out(fresh_token)
