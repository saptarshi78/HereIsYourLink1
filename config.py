# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def GetVarOrNone(var):
    var = os.environ.get(var, '')
    if len(var) < 3: return None
    return var


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    if not BOT_USERNAME.startswith('@'): BOT_USERNAME = '@' + BOT_USERNAME # bu satıra dokunmayın.
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", '')
    if len(UPDATES_CHANNEL) < 2: UPDATES_CHANNEL = None
    OWNER_ID = int(os.environ.get('OWNER_ID', 0)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    AUTH_IDS.append(OWNER_ID)
    LOG_COMMAND = os.environ.get('LOG_COMMAND','log')
    LOG_COMMAND = [LOG_COMMAND, LOG_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    SHORT_COMMAND = os.environ.get('SHORT_COMMAND','short')
    SHORT_COMMAND = [SHORT_COMMAND, SHORT_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.

    # shortener apis + # find better way
    
    shortest = GetVarOrNone("shortest")
    bcvc = GetVarOrNone("bcvc")
    pubiza = GetVarOrNone("pubiza")
    linkvertise = GetVarOrNone("linkvertise")
    bitly = GetVarOrNone("bitly")
    post = GetVarOrNone("post")
    cuttly = GetVarOrNone("cuttly")
    adfly = GetVarOrNone("adfly")
    shortcm = GetVarOrNone("shortcm")
    tinycc = GetVarOrNone("tinycc")
    ouoio = GetVarOrNone("ouoio")

    # shortener apis -

    # settings +

    try: AUTO_DEL_SEC =  int(os.environ.get('AUTO_DEL_SEC', '10'))
    except: AUTO_DEL_SEC = 0
    if AUTO_DEL_SEC == 0: AUTO_DEL_SEC = None
    AUTO_SHORT_MOTOR = GetVarOrNone("AUTO_SHORT_MOTOR")
    DELETE_AUTO_SHORTENED = os.environ.get('DELETE_AUTO_SHORTENED', 'False').lower() == 'true'
    DELETE_COMMAND_SHORTENED = os.environ.get('DELETE_COMMAND_SHORTENED', 'False').lower() == 'true'

    # settings -

    botStartTime = time.time() # dont touch
    HELP_COMMANDS = ["start", "help", "about", "yardım", "h", "y",
        f"start{BOT_USERNAME}", f"help{BOT_USERNAME}", f"about{BOT_USERNAME}",
        f"yardım{BOT_USERNAME}", f"h{BOT_USERNAME}", f"y{BOT_USERNAME}"]
    USING_API = bool(shortest or bcvc or pubiza or linkvertise or bitly or post or cuttly or adfly or shortcm or tinycc or ouoio)

    