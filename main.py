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
            text="""➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../

By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files files.../

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›

➪ /plink ›› 𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄.
➪ /pbatch ›› 𝖴𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆e𝖽𝗂𝖺 𝗅𝗂𝗇𝗄 𝗐𝗂𝗍𝗁 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.
➪ /batch ›› To Create Link For Multiple Post.

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

`/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336`"""   
        )    
              
Dev.run()
