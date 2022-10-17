import jwt
import inspect
from datetime import datetime, timezone
from time import time
from functools import wraps

class ApoJWT():
    """A standard access/refresh JWT implementation that provides convenient decorators and functions
    
    Keyword Arguments (those with asterisks are functions):

    JWT Validation
        secret: Secret string used to encode and decode the access JWT
        exp_period: Length of time in seconds access tokens should be valid for. Default 900 (15 minutes) 
        iss: Issuer string used for additional security. Default ""
        server_audience: List of audiences named from the server hosting the HTTP framework. 
            Audience names are typically base address URLs. Ex: https://example.com
        algorithm: The algorithm to use when encoding/decoding. Default HS256
        admin_permission: Optional permission allowing full access to JWTs carrying this permission. USE CAREFULLY
        * token_finder: Function used to retrieve the access JWT from http request Authorization header. Default None

    Framework Configuration
        async_framework: Tells ApoJWT to use async decorators instead of the normal (FastAPI needs this True). Default False
        * exception_handler: HTTP error handling function given an HTTP code and message as arguments
    """

    def __init__(self, secret: str, exp_period: int=900, iss: str="", server_audience: list=[], algorithm: str="HS256", admin_permission: str=None, template: str=None, async_framework: bool=False, token_finder=None, exception_handler=None):        
        self.__exp_period = int(exp_period)
        self.__refresh_exp_period = 0
        self.__iss = str(iss)
        self.__algorithm = algorithm
        self.__secret = str(secret)
        self.__server_aud = list(server_audience)
        self.__admin_perm = admin_permission
        self.__refresh_flag = False
        self.__refresh_f = None
        self.__refresh_secret = None

        if template == "flask":
            from flask_template import create_flask_template
            self.__async = False
            self.__token_f, self.__exception_handler = create_flask_template()
        elif template == "fastapi":
            from fastapi_template import create_fastapi_template 
            self.__async = True
            self.__token_f, self.__exception_handler = create_fastapi_template()
        else:
            self.__async = async_framework
            self.__token_f = token_finder
            self.__exception_handler = exception_handler


    def config_refresh(self, refresh_secret: str, refresh_exp_period: int=86400, refresh_finder=None):
        """Configures ApoJWT for use with refresh tokens

        refresh_secret: Secret string used to encode and decode the refresh JWT
        refresh_finder: Function used to retrieve the refresh JWT from an http-only cookie. Default None
        refresh_exp_period: Number of seconds for the refresh token to be valid. Default 86400 (1 day)
        """

        self.__refresh_flag = True
        self.__refresh_secret = refresh_secret
        self.__refresh_exp_period = refresh_exp_period
        self.__refresh_f = refresh_finder

    def token_required(self, fn):
        """Verifies a JWT and all its claims
        
        auth_header: http "Authorization" request header (contains the JWT)

        Raises an exception if any claims are invalid
            - expired token
            - invalid secret
            - invalid issuer
        """
        if self.__async is True:
            @wraps(fn)
            async def wrapper(*args, **kwargs):
                if self.__token_f is None:
                    raise TypeError("ApoJWT requires the token_finder attribute to be defined for validating JWTs")
                try:
                    token = self.__token_f(*args, **kwargs)
                except Exception as e:
                    if self.__exception_handler is None:
                        raise jwt.exceptions.InvalidTokenError(f"JWT is missing - Token Finder failed: {e}")
                    else:
                        kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"JWT is missing - Token Finder failed: {e}")
                        self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                        self.__exception_handler(*args, **kwargs)
                        raise NotImplementedError("ApoJWT Exception Handler must not return control")
                token_dict = self.__decode(token, *args, **kwargs)
                kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                self.__form_kwargs(fn, kwarg_dict, kwargs)
                return await fn(*args, **kwargs)
            return wrapper
        else:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if self.__token_f is None:
                    raise TypeError("ApoJWT requires the token_finder attribute to be defined for validating JWTs")
                try:
                    token = self.__token_f(*args, **kwargs)
                except Exception as e:
                    if self.__exception_handler is None:
                        raise jwt.exceptions.InvalidTokenError(f"JWT is missing - Token Finder failed: {e}")
                    else:
                        kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"JWT is missing - Token Finder failed: {e}")
                        self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                        self.__exception_handler(*args, **kwargs)
                        raise NotImplementedError("ApoJWT Exception Handler must not return control")
                token_dict = self.__decode(token, *args, **kwargs)
                kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                self.__form_kwargs(fn, kwarg_dict, kwargs)
                return fn(*args, **kwargs)
            return wrapper
        

    def permission_required(self, permission: str):
        """Verifies a JWT and ensures it contains the correct permission for the resource
    
        permission: permission string that will be fed into permission_formatter if defined

        Raises an exception if any claims are invalid
            - expired token
            - invalid secret
            - invalid issuer
            - invalid audience
        """
        def permission_decorated(fn):
            if self.__async is True:
                @wraps(fn)
                async def wrapper(*args, **kwargs):
                    if self.__token_f is None:
                        raise TypeError("ApoJWT requires the token_finder attribute to be defined for validating JWTs")
                    try:
                        token = self.__token_f(*args, **kwargs)
                    except Exception as e:
                        if self.__exception_handler is None:
                            raise jwt.exceptions.InvalidTokenError(f"JWT is missing - Token Finder failed: {e}")
                        else:
                            kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"JWT is missing - Token Finder failed: {e}")
                            self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                            self.__exception_handler(*args, **kwargs)
                            raise NotImplementedError("ApoJWT Exception Handler must not return control")
                    token_dict = self.__decode(token, *args, **kwargs)
                    decoded_permissions = token_dict["perms"]
                    if self.__admin_perm is not None and self.__admin_perm in decoded_permissions:
                        kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                        self.__form_kwargs(fn, kwarg_dict, kwargs)
                        return await fn(*args, **kwargs)

                    formatted_perm = permission if self.__permission_formatter is None else self.__permission_formatter(permission=permission, *args, **kwargs)                        
                    if formatted_perm not in decoded_permissions:
                        if self.__exception_handler is None:
                            raise jwt.exceptions.InvalidTokenError(f"403: JWT is not authorized for this action")
                        else:
                            kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=403, msg="JWT is not authorized for this action")
                            self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                            self.__exception_handler(*args, **kwargs)
                            raise NotImplementedError("ApoJWT Exception Handler must not return control")
                    kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                    self.__form_kwargs(fn, kwarg_dict, kwargs)
                    return await fn(*args, **kwargs)
                return wrapper
            else: 
                @wraps(fn)
                def wrapper(*args, **kwargs):
                    if self.__token_f is None:
                        raise TypeError("ApoJWT requires the token_finder attribute to be defined for validating JWTs")
                    try:
                        token = self.__token_f(*args, **kwargs)
                    except Exception as e:
                        if self.__exception_handler is None:
                            raise jwt.exceptions.InvalidTokenError(f"JWT is missing - Token Finder failed: {e}")
                        else:
                            kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"JWT is missing - Token Finder failed: {e}")
                            self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                            self.__exception_handler(*args, **kwargs)
                            raise NotImplementedError("ApoJWT Exception Handler must not return control")
                    token_dict = self.__decode(token, *args, **kwargs)
                    decoded_permissions = token_dict["perms"]
                    if self.__admin_perm is not None and self.__admin_perm in decoded_permissions:
                        kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                        self.__form_kwargs(fn, kwarg_dict, kwargs)
                        return fn(*args, **kwargs)

                    formatted_perm = permission if self.__permission_formatter is None else self.__permission_formatter(permission, *args, **kwargs)
                    if formatted_perm not in decoded_permissions:
                        if self.__exception_handler is None:
                            raise jwt.exceptions.InvalidTokenError(f"403: JWT is not authorized for this action")
                        else:
                            kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=403, msg="JWT is not authorized for this action", *args, **kwargs)
                            self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                            self.__exception_handler(*args, **kwargs)
                            raise NotImplementedError("ApoJWT Exception Handler must not return control")
                    kwarg_dict = dict(token_data=token_dict["data"], token_subject=token_dict["sub"])
                    self.__form_kwargs(fn, kwarg_dict, kwargs)
                    return fn(*args, **kwargs)
                return wrapper
        return permission_decorated


    def refresh(self, fn):
        """Verifies a refresh token and returns the refresh data"""
        if self.__async is True:
            @wraps(fn)
            async def wrapper(*args, **kwargs):
                if self.__refresh_f is None:
                    raise NotImplementedError("ApoJWT requires the refresh_finder attribute to be defined for refreshing JWTs")
                if "refresh_data" in kwargs.keys():
                    kwargs.pop("refresh_data")
                try:
                    ref_token = self.__refresh_f(*args, **kwargs)
                except Exception as e:
                    if self.__exception_handler is None:
                        raise jwt.exceptions.InvalidTokenError(f"Refresh JWT is missing - Refresh Token Finder failed: {e}")
                    else:
                        kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"Refresh JWT is missing - Refresh Token Finder failed: {e}")
                        self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                        self.__exception_handler(*args, **kwargs)
                        raise NotImplementedError("ApoJWT Exception Handler must not return control")
                refresh_payload = self.__decode(ref_token, secret=self.__refresh_secret, *args, **kwargs)
                kwarg_dict = dict(refresh_data=refresh_payload["data"])
                self.__form_kwargs(fn, kwarg_dict, kwargs)
                return await fn(*args, **kwargs)
            return wrapper
        else:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if self.__refresh_f is None:
                    raise NotImplementedError("ApoJWT requires the refresh_finder attribute to be defined for refreshing JWTs")
                if "refesh_data" in kwargs.keys():
                    kwargs.pop("refresh_data")
                try:
                    ref_token = self.__refresh_f(*args, **kwargs)
                except Exception as e:
                    if self.__exception_handler is None:
                        raise jwt.exceptions.InvalidTokenError(f"Refresh JWT is missing - Refresh Token Finder failed: {e}")
                    else:
                        kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"Refresh JWT is missing - Refresh Token Finder failed: {e}")
                        self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                        self.__exception_handler(*args, **kwargs)
                        raise NotImplementedError("ApoJWT Exception Handler must not return control")
                refresh_payload = self.__decode(ref_token, secret=self.__refresh_secret, *args, **kwargs)
                kwarg_dict = dict(refresh_data=refresh_payload["data"])
                self.__form_kwargs(fn, kwarg_dict, kwargs)
                return fn(*args, **kwargs)
            return wrapper
        

    def create_token(self, sub: str="", permissions: list[str]=[], data: dict=dict(), refresh_data: dict=dict()):
        """Encodes and returns an access JWT and optionally a refresh JWT

        sub: Subject of the JWT (typically some reference to the user of JWT)
        permissions: List of permissions to assign to token
        data: Any additional information that is needed
        refresh_data: If refresh is configured, this additional data is stored with the refresh token

        JWT will contain the following claims:
            - exp: Expiration Time
            - nbf: Not Before Time
            - iss: Issuer
            - aud: Audience
            - iat: Issued At
        """
        exp = int(time()) + self.__exp_period
        payload = {
            "exp": int(exp),
            "sub": str(sub),
            "nbf": datetime.now(tz=timezone.utc),
            "iss": self.__iss,
            "aud": list(self.__server_aud),
            "iat": datetime.now(tz=timezone.utc),
            "data": data,
            "perms": list(permissions)
        }
        access_token = jwt.encode(payload, self.__secret, algorithm=self.__algorithm)
        if self.__refresh_flag is True:
            if self.__refresh_secret is None:
                raise ValueError("The refresh secret must be assigned using config_refresh")
            ref_exp = int(time()) + self.__refresh_exp_period
            refresh_payload = {
                "exp": ref_exp,
                "nbf": datetime.now(tz=timezone.utc),
                "iss": self.__iss,
                "aud": list(self.__server_aud),
                "iat": datetime.now(tz=timezone.utc),
                "data": refresh_data
            }
            refresh_token = jwt.encode(refresh_payload, self.__refresh_secret, algorithm=self.__algorithm)
            return access_token, refresh_token
        return access_token


    def __decode(self, token, secret=None, *args, **kwargs):
        """Decodes the active jwt and returns the result"""
        not_implemented = NotImplementedError("ApoJWT Exception Handler must not return control")
        if secret is None:
            secret = self.__secret
        try:
            decoded = jwt.decode(token, secret, issuer=self.__iss, audience=self.__server_aud, algorithms=[self.__algorithm])
            return decoded
        except jwt.exceptions.InvalidSignatureError:
            if self.__exception_handler is None:
                raise jwt.exceptions.InvalidSignatureError(f"401: JWT signature is invalid")
            else:
                kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg="JWT signature is invalid")
                self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                self.__exception_handler(*args, **kwargs)
                raise not_implemented
        except jwt.exceptions.ExpiredSignatureError:
            if self.__exception_handler is None:
                raise jwt.exceptions.ExpiredSignatureError(f"403: JWT signature has expired")
            else:
                kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=403, msg="JWT signature has expired")
                self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                self.__exception_handler(*args, **kwargs)
                raise not_implemented
        except jwt.exceptions.InvalidIssuerError:
            if self.__exception_handler is None:
                raise jwt.exceptions.InvalidIssuerError(f"401: JWT issuer is invalid")
            else:
                kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg="JWT issuer is invalid")
                self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                self.__exception_handler(*args, **kwargs)
                raise not_implemented
        except jwt.exceptions.InvalidAudienceError:
            if self.__exception_handler is None:
                raise jwt.exceptions.InvalidAudienceError(f"401: JWT audience is invalid")
            else:
                kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg="JWT audience is invalid")
                self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                self.__exception_handler(*args, **kwargs)
                raise not_implemented
        except jwt.exceptions.InvalidTokenError as e:
            if self.__exception_handler is None:
                raise jwt.exceptions.InvalidTokenError(f"401: JWT is invalid")
            else:
                kwarg_dict = dict(token_data=dict(), token_subject="", access_token="", code=401, msg=f"JWT is invalid: {e}")
                self.__form_kwargs(self.__exception_handler, kwarg_dict, kwargs)
                self.__exception_handler(*args, **kwargs)
                raise not_implemented


    def __form_kwargs(self, fn, new_kwargs: dict, kwargs):
        """Inspects the function 'fn' and decides which new_kwargs should be sent as keyword arguments"""
        fn_args = list(inspect.signature(fn).parameters.keys())
        for key in new_kwargs.keys():
            if key in fn_args:
                kwargs[key] = new_kwargs[key]