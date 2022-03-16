from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "bro":
     await msg.message.edit("hi")




