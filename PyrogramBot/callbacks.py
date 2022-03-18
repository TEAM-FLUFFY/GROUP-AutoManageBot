from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
  


@Client.on_callback_query()
async def telegraph_cb(bot, msg)
    if msg.data == "start"
        await.msg.message.edit(
            text="""▫️HELP: Telegraph▪️

Do as you wish with telegra.ph module!

USAGE:

🤧 /telegraph - Send me Picture or Vide Under (5MB)

NOTE:

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="start")
               ]]
               )
        )
