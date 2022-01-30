# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from http.client import CONFLICT
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.listasstring import getListAsString
from HelperFunc.message import sendMessage
from HelperFunc.shortMotors import short_url
from config import Config
import time, re, logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.SHORT_COMMAND))
async def shorten(client: Client, message: Message):
    if not await AuthUserCheck(message): return
    help_msg = f"Please read {Config.HELP_COMMANDS[0]}"
    replied = bool(message.reply_to_message)
    url = None
    domain = None
    helpmes = None
    if replied:
        try:
            url = message.reply_to_message.text
            domain = message.text.split(' ')[1]
        except Exception as t:
            LOGGER.warning(str(t))
            helpmes = help_msg
    else:
        try:
            url = message.text.split(' ')[2]
            domain = message.text.split(' ')[1]
        except Exception as t:
            LOGGER.warning(str(t))
            helpmes = help_msg
    if helpmes:
        helpmes = await sendMessage(message, helpmes)
        if Config.AUTO_DEL_SEC:
            time.sleep(Config.AUTO_DEL_SEC)
            return await helpmes.delete()
        else: return
    URL_REGEX = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"
    if not bool(re.findall(URL_REGEX, url)):
        helpmes = "Not a valid URL."
    if helpmes:
        helpmes = await sendMessage(message, helpmes)
        if Config.AUTO_DEL_SEC:
            time.sleep(Config.AUTO_DEL_SEC)
            return await helpmes.delete()
        else: return
    try: await sendMessage(message, short_url(url, domain))
    except Exception as e: LOGGER.warning(e)
    if Config.DELETE_COMMAND_SHORTENED:
        if Config.AUTO_DEL_SEC: time.sleep(Config.AUTO_DEL_SEC)
        try: await message.delete()
        except Exception as e: LOGGER.warning(e)
