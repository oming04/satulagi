#(Ā©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ā Creator : <a JOIN VVIP : <a href='https://t.me/vvipmurahmeriah'>VVIP MURAH</a>\nā PAID PROMOTE : <a href='https://t.me/tontonvid'>PP MURAH</a>\nā Source Code : <a href='https://t.me/tontonvid'>Click Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("š Tutup Jangan Kepo", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass