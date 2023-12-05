#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6315953148:AAHxTD8ZboAU30Brpw-ZJl20UcY88CnrEe8" # BOT TOKEN
    API_ID =  28122413 # API ID
    API_HASH = "750432c8e1b221f91fd2c93a92710093" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "NovaSupports" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001816188874 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("6149191605").split()}) #OWNER ID

DB_URL = "mongodb+srv://publicDB:publicDBbyKira@public.twckcqf.mongodb.net/?retryWrites=true&w=majority" # MONGO DB URL

SQL_URL = "" # ELEPHANT SQL URL
