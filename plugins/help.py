# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.listasstring import getListAsString


from HelperFunc.message import sendMessage
from config import Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.HELP_COMMANDS))
async def help(client, message: Message):
    if not await AuthUserCheck(message): return
    tumad = message.from_user.mention()
    help_msg = f"<a href='https://github.com/HuzunluArtemis/ShortenerBot'>🍁</a> Esenlikler / Hi {tumad}\n\n"
    apireq = ["shorte.st", "bc.vc", "pubiza", "linkvertise", "bit.ly", "post", "cutt.ly", "adf.ly", "shortcm", "tinycc", "ouo.io"]
    free = ["v.gd", "da.gd", "is.gd", "ttm.sh", "clck.ru", "chilp.it", "osdb", "tinyurl", "owly"]
    apireq = getListAsString(apireq)
    free = getListAsString(free)
    help_msg += "<b>Send link after command:</b>"
    help_msg += f"\n<code>/{Config.SHORT_COMMAND[0]}" + " {link}" + "</code>"
    help_msg += "\n\n<b>Select shortener:</b>"
    help_msg += f"\n<code>/{Config.SHORT_COMMAND[0]} is.gd " + " {link}" + "</code>"
    help_msg += "\n\n<b>By replying to message (including link):</b>"
    help_msg += f"\n<code>/{Config.SHORT_COMMAND[0]}" + " {message}" + "</code>"
    help_msg += "\n\nAll supported domains: " + free 
    help_msg += "\nRequires APIKEY: " + apireq
    if Config.USING_API:
        help_msg += "\n\nThis bot can short all free's and: "
        help_msg += "\nshortest: " + str(bool(Config.shortest))
        help_msg += "\nbcvc: " + str(bool(Config.bcvc))
        help_msg += "\npubiza: " + str(bool(Config.pubiza))
        help_msg += "\nlinkvertise: " + str(bool(Config.linkvertise))
        help_msg += "\nbitly: " + str(bool(Config.bitly))
        help_msg += "\npost: " + str(bool(Config.post))
        help_msg += "\ncuttly: " + str(bool(Config.cuttly))
        help_msg += "\nadfly: " + str(bool(Config.adfly))
        help_msg += "\nshortcm: " + str(bool(Config.shortcm))
        help_msg += "\ntinycc: " + str(bool(Config.tinycc))
        help_msg += "\nouoio: " + str(bool(Config.ouoio))
    if Config.AUTO_SHORT_MOTOR:
        help_msg += f"\n\nThis bot can direct short your urls with {Config.AUTO_SHORT_MOTOR}"
        help_msg += f"\nIf you want to try, send me a link. Yes Only link. without anything."
        help_msg += f"\nYou can use this feature for groups etc."
        if Config.DELETE_AUTO_SHORTENED:
            help_msg += "\nAnd I will delete shortened link. Give me delete permission."
    reply_markup = None
    if Config.UPDATES_CHANNEL:
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(
                text = "🔥 Güncellemeler / Updates",
                url = "https://t.me/" + Config.UPDATES_CHANNEL)
                ]
            ])
    await sendMessage(message,help_msg,reply_markup)
