from drf_spectacular.utils import OpenApiParameter

STANDARD_REGISTRATION_POST_PARAMETERS = [
    OpenApiParameter(
        name="email",
        description="E-mail",
        required=True,
        type=str,
    ),
    OpenApiParameter(
        name="password",
        description="Password",
        required=True,
        type=str,
    ),
    OpenApiParameter(
        name="repeat_password",
        description="Repeat password",
        required=True,
        type=str,
    ),
]

STANDARD_LOGIN_POST_PARAMETERS = [
    OpenApiParameter(
        name="email",
        description="E-mail",
        required=True,
        type=str,
    ),
    OpenApiParameter(
        name="password",
        description="Password",
        required=True,
        type=str,
    ),
]

REMIND_PASSWORD_POST_PARAMETERS = [
    OpenApiParameter(
        name="email",
        description="E-mail",
        required=True,
        type=str,
    ),
]

SOCIAL_AUTH_POST_PARAMETERS = [
    OpenApiParameter(
        name="token",
        description="Social authorization token",
        required=True,
        type=str,
    ),
]
