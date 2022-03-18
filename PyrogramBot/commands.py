from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
ℎ𝑒𝑦 𝑑𝑒𝑎𝑟 {} 𝑏𝑟𝑜 𝑖𝑎𝑚 𝑇𝑔𝑟𝑎𝑝ℎ 𝑉2𝑏𝑜𝑡
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/6c890b13e27c0f219a015.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝙳𝙴𝚅", url="https://t.me/KAAVAL_KAARAN_tg"),
            InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴?", callback_data="use") 
            ]]
            )
        )



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "use":
        await msg.answer("""𝙸𝚃'𝚂 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴. 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙰𝙽𝚈 𝙿𝙸𝙲𝚃𝚄𝚁𝙴𝚂 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾𝚂 𝙱𝙴𝙻𝙾𝚆 5𝙼𝙱 𝙰𝙽𝙳 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝙶𝙴𝚃𝚃𝙷𝙴 𝚃𝙶𝚁𝙰𝙿𝙷 𝙻𝙸𝙽𝙺
""", show_alert=True)
