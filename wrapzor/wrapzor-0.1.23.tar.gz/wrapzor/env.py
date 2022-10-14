import os
from pathlib import Path

ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_PASSWORD = os.getenv("ZOHO_CLIENT_PASSWORD")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_CODE = os.getenv("ZOHO_CODE")
ZOHO_ACCOUNT_DOMAIN = os.getenv("ZOHO_ACCOUNT_DOMAIN", "https://accounts.zoho.eu")
CURRENT_DIR = Path(__file__).parent
HOME = Path.home()

STATIC_DIR = HOME / ".wrapzor"
STATIC_DIR.mkdir(exist_ok=True)

BULKS_DIR = STATIC_DIR / "bulks"
BULKS_DIR.mkdir(exist_ok=True)

TOKENS_DIR = STATIC_DIR / "tokens"
TOKENS_DIR.mkdir(exist_ok=True)
