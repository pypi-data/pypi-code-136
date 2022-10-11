# -----------------------------------------------------------------------------
# REQUIRED VALUES
# -----------------------------------------------------------------------------
# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# SECURITY WARNING: Change this and keep it a secret in production!
SECRET_KEY = 'lomd0acr0q_o@p6i-ub66xl)k^6$)@-@$8zk&a#w#2_%try_zq'

# Name of machine running the application
ALLOWED_HOSTS = ['localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# SSO URL
CAS_SERVER_URL = 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login'

# `````````````````
# FINTI
# `````````````````
# REQUIRED: Finti URL and Token:
FINTI_TOKEN = '2144402c-586e-44fc-bd0c-62b31e98394d'  # Test Token
FINTI_URL = 'https://sf-dev.oit.pdx.edu'

# Finti URLs (for reference)
# -  http://127.0.0.1:5000
# -  http://localhost:8888
# -  https://ws-dev.oit.pdx.edu
# -  https://ws-stage.oit.pdx.edu
# -  https://ws.oit.pdx.edu

# As-of psu-base 0.11.0, Finti responses can be cached for offline development
FINTI_SIMULATE_WHEN_POSSIBLE = True     # Use cached calls when possible, call Finti when not cached
FINTI_SAVE_RESPONSES = True             # Save/record actual Finti responses for offline use?

# Also saves time for slow connections:
DISABLE_GRAVATAR = True

# Required for sending email:
EMAIL_HOST_USER = 'cefr-app-mail'
EMAIL_HOST_PASSWORD = 'EuDFxamEfm7y'

# -----------------------------------------------------------------------------
# OPTIONAL VALUES
# -----------------------------------------------------------------------------

# You may want to disable elevated developer access while running locally
# ELEVATE_DEVELOPER_ACCESS = False

# You may want to extend session expiration during local development
SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours

