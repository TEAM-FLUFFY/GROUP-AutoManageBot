from pyrogram import Client

PyrogramBot = Client(
    "PyrogramBot",
    api_hash="d9647913e97bf2f6a66d978290284028",
    api_id="17946666",
    bot_token="5125014420:AAEK2E9aj-q9FHZknW_hrisJvCuONx0XPtU",
    plugins=dict(root="PyrogramBot")
  )

Client.run()
