# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.listasstring import getListAsString
from HelperFunc.message import sendMessage
from HelperFunc.shortMotors import short_url
from config import Config
import re, logging, time


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.text)
async def shorten(client: Client, message: Message):
    if not Config.AUTO_SHORT_MOTOR: return
    if not await AuthUserCheck(message): return
    url = message.text
    domain = Config.AUTO_SHORT_MOTOR
    URL_REGEX = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"
    if not bool(re.findall(URL_REGEX, url)): return
    try: await sendMessage(message, short_url(url, domain))
    except Exception as e: LOGGER.warning(e)
    if Config.DELETE_AUTO_SHORTENED:
        if Config.AUTO_DEL_SEC: time.sleep(Config.AUTO_DEL_SEC)
        try: await message.delete()
        except Exception as e: LOGGER.warning(e)
