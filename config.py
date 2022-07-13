from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4647248"))
API_HASH = getenv("API_HASH", c9f5cc42a060e4425e77f358ccde7121")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","ALIZA")
BOT_USERNAME = getenv("BOT_USERNAME", "Aliza_probot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DREEAM_CLUB")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9f26e5550c80533220d3d.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9f26e5550c80533220d3d.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5082653703").split()))
