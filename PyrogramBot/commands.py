from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


ALL_PIC = [
 "https://telegra.ph/file/5f51546ad227831b96a38.jpg",
 "https://telegra.ph/file/56e2c12ed686eeb4513da.jpg",
 "https://telegra.ph/file/266fec5cf211151997303.jpg",
 "https://telegra.ph/file/13527c7b40976c1368cca.jpg"
]

@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption="എന്റെ പേര് <a href=https://t.me/FluffyPyroGramBot>𝙵𝙻𝚄𝙵𝙵𝚈 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>, 🔰മച്ചാനെ എന്റെ പണി കഴിഞ്ഞിട്ടില്ല അതുകൊണ്ട് RePo✅️ പ്രൈവറ്റ് ആണ് Work കഴിഞ്ഞിട്ട് public ആക്കും ",
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("🗨️𝔾ℝ𝕆𝕌ℙ🗨️", url="https://t.me/DEVELOPERSCHANNEL2022"),
          InlineKeyboardButton ("📂ℂℍ𝔸ℕℕ𝔼𝕃📂", url="https://t.me/DELCHANNEL001"),
          ],[
          InlineKeyboardButton ("🔰𝔼𝔻𝕀𝕋𝔼ℝ🔰", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("©️ℙ𝔸𝕀𝔻 ℙℝ𝕆𝕄𝕆𝕋𝕀𝕆ℕ", url="t.me/pushpa_Reju"),
          ],[
          InlineKeyboardButton ("👨‍💻𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝔼ℝ👨‍💻", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("🟡𝔹ℝ𝕆𝕋ℍ𝔼ℝ 𝔹𝕆𝕋🟡", url="t.me/SAZUKI_FILTER_BOT"),
          ],[
          InlineKeyboardButton ("⚜️𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝔸 ℂℍ𝔸𝕋 𝔾ℝ𝕆𝕌ℙ⚜️", url="http://t.me/FluffyPyroGramBot?startgroup=true"),
          ]]
          )
          
        )
