from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random


ALL_PIC = [
 "https://telegra.ph/file/52b71d5a61c904c6a59d1.jpg",
 "https://telegra.ph/file/28a00384a3be4f6c916ba.jpg",
 "https://telegra.ph/file/eb654e5c7ff4d29eab29f.jpg",
 "https://telegra.ph/file/a4796bdcca7ff90a3a3b8.jpg",
 "https://telegra.ph/file/b7b43793368770ca4c7fb.jpg"
]

@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption="എന്റെ പേര് <a href=https://t.me/FluffyPyroGramBot>𝙵𝙻𝚄𝙵𝙵𝚈 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>, 🔰മച്ചാനെ എന്റെ പണി കഴിഞ്ഞിട്ടില്ല അതുകൊണ്ട് RePo✅️ പ്രൈവറ്റ് ആണ് Work കഴിഞ്ഞിട്ട് public ആക്കും ",
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("𝑎𝑑𝑑 𝑚𝑒 𝑡𝑜 𝑦𝑜𝑢𝑟 𝑐ℎ𝑎𝑡", url="http://t.me/EFX_pyrogramBot?startgroup=true"),
          ],[
          InlineKeyboardButton ("𝑐ℎ𝑎𝑛𝑛𝑒𝑙", url="https://t.me/MWcinemase"),
          InlineKeyboardButton ("𝑑𝑒𝑣", url="https://t.me/ATHIF_E_F_X_P_G_OFFLINE"),
          ],[
          InlineKeyboardButton ("ℎ𝑒𝑙𝑝", callback_data="song"),
          ]]
          )
          
        )
