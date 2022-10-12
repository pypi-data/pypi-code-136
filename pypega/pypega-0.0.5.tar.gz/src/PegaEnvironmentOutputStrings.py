## Environment - __print_api_response()
OS_PRINT_API_RESPONSE = "API call to '{method} {url}' returned status HTTP {status_code}"

## Environment - set_logging_level()
OS_API_RESPONSE_LOGGING_LEVEL_SET = "API response logging level set to '{level}'"

## Environment - set_authentication_method()
OS_AUTHENTICATION_METHOD_SET = "Authentication method set to '{authentication_method}'"
OS_AUTHENTICATION_METHOD_INVALID = "Invalid authentication method '{authentication_method} provided"

## Environment - set_base_url()
OS_ENVIRONMENT_URL_SET = "Base URL set to '{url}'"
OS_URL_MUST_START_WITH = "URL must begin with '{must_start_with}' but was specified as '{url}'"
OS_URL_MUST_END_WITH = "URL must end with '{must_end_with}' but was specified as '{url}'"

## Environment - set_application_context()
OS_APPLICATION_CONTEXT_SET = "Application context set to '{application_context}', please ensure the corresponding alias is configured in Pega"

## Environment - set_oauth_authorization_token_url()
OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH = "Authorizaton token URL must begin with '{must_start_with}' but was specified as '{authorization_token_url}'"
OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH = "Authorizaton token URL must end with '{must_end_with}' but was specified as '{authorization_token_url}'"
OS_OAUTH_AUTHORIZATION_TOKEN_URL_SET = "OAuth authorization token URL set to {authorization_token_url}'"

## Environment - set_oauth_authorization_client_id()
OS_OAUTH_CLIENT_ID_SET = "OAuth client ID set to '{client_id}'"

## Environment - set_oauth_client_secret()
OS_OAUTH_CLIENT_SECRET_SET = "OAuth client secret set"

## Environment - set_operator()
OS_OPERATOR_SET = "Operator set as '{operator}'"

## Environment - set_operator_password()
OS_OPERATOR_PASSWORD_SET = "Operator password set"

## Environment - obtain_oauth_token()
OS_OAUTH_TOKEN_OBTAINED = "OAuth token obtained. Token expires at '{token_expires_at}'"

## Environment - Other Oatuh problems
OS_UNABLE_TO_RETRIEVE_OAUTH_TOKEN = "Unable to obtain OAuth token"
OS_AUTHENTICATION_METHOD_MISSING_OR_INVALID = "Authentication method missing or invalid. Use set_authentication_method() method."
OS_OAUTH_AUTHORIZATION_TOKEN_URL_MISSING = "Cannot obtain token as token URL not provided. Use set_oauth_authorization_token_url() method."
OS_OAUTH_CLIENT_ID_MISSING = "Cannot obtain token as client ID not provided. Use set_oauth_client_id() method."
OS_OAUTH_CLIENT_SECRET_MISSING = "Cannot obtain token as client ID not provided. Use set_oauth_client_id() method."

