from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from shizuka import SHIZUKA, START_IMG

SHIZUKA_START = f"I am Shizuka 『しずか』, An Intelligent ChatBot.[⠀]({START_IMG})"


@SHIZUKA.on_message(filters.command(["start"], prefixes=["/", "!"]) & ~filters.edited)
async def info(client, message):
    buttons = [
        [
            InlineKeyboardButton(
                text="Go inline", switch_inline_query_current_chat="Star_xrobot "
            ),
        ],
        [
            InlineKeyboardButton(
                "Support", url="https://t.me/mondoclub"
            ),
            InlineKeyboardButton(
                "Maintained by", url="https://t.me/luckyclub16"
            ),
        ],
    ]
    await SHIZUKA.send_message(
        chat_id=message.chat.id,
        text=SHIZUKA_START,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
