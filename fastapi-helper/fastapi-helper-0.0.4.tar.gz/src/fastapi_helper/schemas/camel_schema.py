# -*- coding: utf-8 -*-
#
# class JwtHTTPBearer(HTTPBearer):
#     async def __call__(
#         self,
#         request: Request,
#     ) -> Optional[HTTPAuthorizationCredentials]:
#         authorization: str = request.headers.get("Authorization")
#         scheme, credentials = get_authorization_scheme_param(authorization)
#         if not (authorization and scheme and credentials):
#             if self.auto_error:
#                 raise HTTPException(
#                     status_code=HTTP_403_FORBIDDEN,
#                     detail={
#                         "code": "bearer-001",
#                         "type": "NOT_AUTHENTICATED",
#                         "message": "Not authenticated",
#                     },
#                 )
#             else:
#                 return None
#         if scheme.lower() != "bearer":
#             if self.auto_error:
#                 raise HTTPException(
#                     status_code=HTTP_403_FORBIDDEN,
#                     detail={
#                         "code": "bearer-001",
#                         "type": "NOT_AUTHENTICATED",
#                         "message": "Invalid authentication format",
#                     },
#                 )
#             else:
#                 return None
#         return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)
#
#
# jwt_http_bearer = JwtHTTPBearer()
# jwt_http_bearer_no_error = JwtHTTPBearer(auto_error=False)
#
#
# def as_form(cls: Type[BaseModel]):
#     new_parameters = []
#
#     for field_name, model_field in cls.__fields__.items():
#         model_field: ModelField
#
#         new_parameters.append(
#             inspect.Parameter(
#                 model_field.alias,
#                 inspect.Parameter.POSITIONAL_ONLY,
#                 default=Form(...) if model_field.required else Form(model_field.default),
#                 annotation=model_field.outer_type_,
#             ),
#         )
#
#     async def as_form_func(**data):
#         return cls(**data)
#
#     sig = inspect.signature(as_form_func)
#     sig = sig.replace(parameters=new_parameters)
#     as_form_func.__signature__ = sig  # type: ignore
#     setattr(cls, "as_form", as_form_func)
#     return cls
#
#
# class ApiSchema(PydanticModel):
#     class Config:
#         orm_mode = True
#         orig_model = None
#         alias_generator = camelize
#         allow_population_by_field_name = True
