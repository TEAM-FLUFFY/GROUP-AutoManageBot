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
        caption="ℎ𝑒𝑦 𝑑𝑒𝑎𝑟 {user.mention}",
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("𝑎𝑑𝑑 𝑚𝑒 𝑡𝑜 𝑦𝑜𝑢𝑟 𝑐ℎ𝑎𝑡", url="http://t.me/EFX_pyrogramBot?startgroup=true"),
          ],[
          InlineKeyboardButton ("𝑐ℎ𝑎𝑛𝑛𝑒𝑙", url="https://t.me/MWcinemase"),
          InlineKeyboardButton ("𝑑𝑒𝑣", url="https://t.me/ATHIF_E_F_X_P_G_OFFLINE"),
          ],[
          InlineKeyboardButton ("ℎ𝑒𝑙𝑝", callback_data="hellp"),
          ]]
          )
          
        )


@Client.on_callback_query()
async def callback(bot,query: CallbackQuery):
    if query.data == "hellp":
        await query.message.edit_text(
            text="""➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../
By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files
⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›
➪ /plink ›› 𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄.
➪ /pbatch ›› 𝖴𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆e𝖽𝗂𝖺 b𝗅𝗂𝗇𝗄 𝗐𝗂𝗍𝗁 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.
➪ /batch ›› To Create Link For Multiple Post.
⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›
`/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336`"""   
        )
