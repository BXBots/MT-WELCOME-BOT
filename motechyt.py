from telegram import Update
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
import os

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

START_MESSAGE = """Hi {}, {}"""

HELP_TEXT = "HI"

def start(updater,context):
 update.effective_message.reply_photo(PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name),reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text=" 👥 channel.",url="https://telegram.dog/Mai_bOTs")],  
                                                [InlineKeyboardButton(text="Creater",url="https://t.me/No_OnE_Kn0wS_Me"),InlineKeyboardButton(text="Mai Source",url="https://github.com/No-OnE-Kn0wS-Me/Filterbot")]]),disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

def help(updater,context):
 updater.message.reply_text(
                            "{}".format(HELP_TEXT),
                            reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text="How To Own", url="https://t.me/Mrk_yt")], [InlineKeyboardButton(text="Join", url="t.me/PR0FESS0R_99")]]),
                            disable_web_page_preview=True,
                            parse_mode=ParseMode.MARKDOWN)
                           
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'👋Hello {member.full_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖'.format(Team), reply_markup=InlineKeyboardMarkup( [[InlineKeyboardButton(text="How To Own", url="https://t.me/Mrk_yt")], [InlineKeyboardButton(text="Join", url="t.me/PR0FESS0R_99")]]), disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
