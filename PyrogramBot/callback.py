from pyrogram import Client, filters

@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "start":
     await msg.message.edit("hi")
