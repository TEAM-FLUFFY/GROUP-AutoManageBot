from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
  


@Client.on_callback_query()
async def telegraph_cb(bot, msg)
    if msg.data == "tgra"
        await.msg.message.edit(
            text="""<b>HELP:</b> Telegraph▪️

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


    elif msg.data == "start"
        await msg.message.edit(
            text=START_MESSAGE.format(message.from_user.mention),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton ("🗨️𝔾ℝ𝕆𝕌ℙ🗨️", url="https://t.me/DEVELOPERSCHANNEL2022"),
                InlineKeyboardButton ("📂ℂℍ𝔸ℕℕ𝔼𝕃📂", url="https://t.me/DELCHANNEL001")
                ],[
                InlineKeyboardButton ("🔰𝔼𝔻𝕀𝕋𝔼ℝ🔰", url="t.me/TEAM_KERALA"),
                InlineKeyboardButton ("©️ℙ𝔸𝕀𝔻 ℙℝ𝕆𝕄𝕆𝕋𝕀𝕆ℕ", url="t.me/pushpa_Reju")
                ],[
                InlineKeyboardButton ("👨‍💻𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝔼ℝ👨‍💻", url="t.me/TEAM_KERALA"),
                InlineKeyboardButton ("help", callback_data="help")
                ],[
                InlineKeyboardButton ("⚜️𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝔸 ℂℍ𝔸𝕋 𝔾ℝ𝕆𝕌ℙ⚜️", url="http://t.me/FluffyPyroGramBot?startgroup=true")
                ]]
                )
        )
    
