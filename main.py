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
 "https://telegra.ph/file/5f51546ad227831b96a38.jpg",
 "https://telegra.ph/file/56e2c12ed686eeb4513da.jpg",
 "https://telegra.ph/file/266fec5cf211151997303.jpg",
 "https://telegra.ph/file/13527c7b40976c1368cca.jpg"
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
        await query.message.edit(
           text="""🎼Song Download🎼
Song Download Module, For Those Who Love Music

🎈 Command 🎈

- /song [Song Name] - To Download Music 😁

🌀Usage🌀
- Can Be Used By Everyone
- Works in bot pm
𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝘼𝙣𝙮 𝙑𝙞𝙙𝙚𝙤 𝙁𝙧𝙤𝙢 𝙔𝙏.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
/𝘮𝘱4 https://youtu.be/Your Link"""
        )    
              
Dev.run()
