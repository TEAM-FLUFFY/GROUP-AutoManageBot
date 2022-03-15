from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

Dev=Client(
      "PG",
      bot_token="5125014420:AAEK2E9aj-q9FHZknW_hrisJvCuONx0XPtU",
      api_id="17946666",
      api_hash="d9647913e97bf2f6a66d978290284028",
)


ALL_PIC = [
 "https://telegra.ph/file/52b71d5a61c904c6a59d1.jpg",
 "https://telegra.ph/file/28a00384a3be4f6c916ba.jpg",
 "https://telegra.ph/file/eb654e5c7ff4d29eab29f.jpg",
 "https://telegra.ph/file/a4796bdcca7ff90a3a3b8.jpg",
 "https://telegra.ph/file/b7b43793368770ca4c7fb.jpg"
]

@Dev.on_message(filters.command("start"))
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
          InlineKeyboardButton ("help", callback_data="song"),
          ],[
          InlineKeyboardButton ("⚜️𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝔸 ℂℍ𝔸𝕋 𝔾ℝ𝕆𝕌ℙ⚜️", url="http://t.me/FluffyPyroGramBot?startgroup=true"),
          ]]
          )
          
        )
    
           

@Dev.on_callback_query()
async def callback(bot,query:  CallbackQuery):
    if query.data == "song":
        await query.message.edit_text(
            text="ˣˣˣ 𝑡𝑒𝑛𝑡𝑎𝑐𝑡𝑖𝑜𝑛"   
        )    
              
Dev.run()
