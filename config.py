import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23631217"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "567c6df308dc6901790309499f729d12")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002338165303"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "mimam_officialx")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6139759254"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://samanthasaintf0:samanthasaintf0@cluster0.6fe2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002528229701"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002232443823"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "5"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello, {first},!\n\nI’m your File Store Bot, here to safely store and manage your private files. Upload them to the specified channel, and share them with others using a unique link. Let’s keep your files organized and accessible!</b>")
try:
    ADMINS=[6139759254]
    for x in (os.environ.get("ADMINS", "6139759254").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>🌟 Hello, {first}!\n\nJoin our amazing channels to unlock exclusive content! After joining, simply hit the reload button to access your requested file. Let’s get started!</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>•🦋 with love @MRN_RIPPER ❤</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 ᴏʜ ɴᴏ! ᴡʜᴇʀᴇ'ʀᴇ ʏᴏᴜʀ ʜᴀɴᴅs?!"

ADMINS.append(OWNER_ID)
ADMINS.append(6139759254)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
