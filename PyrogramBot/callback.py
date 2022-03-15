from pyrogram import Client, filters

@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "bro":
     await msg.message.edit("hi")




@Client.on_callback_query()
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
