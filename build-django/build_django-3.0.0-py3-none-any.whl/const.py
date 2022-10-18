GITIGNORE: str = '/venv\n/static\n/media\n__pycache__\n*.sqlite*\n*.log\n.env'

ENV_EXAMPLE: str = '''
SECRET_KEY=

# List of comma separated values
ALLOWED_HOSTS=

# Remove if production
DEBUG=
'''

REQUIRED_PACKAGES: list[str] = (
    'wheel',
    'django',
    'django-environ',
    'gunicorn'
)
