from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="🌿 𝐇ᴇʟᴘ 🦋", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="🌿 𝐒ᴜᴘᴘᴏʀᴛ 🦋", url=f"https://t.me/THE_GLACEON"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🌿 𝐆ʀᴏᴜᴘ 💕", url=f"https://t.me/GLACEON_CHATS"),
            InlineKeyboardButton(text="🌿 𝐂ʜᴀɴɴᴇʟ 🦋", url=f"https://t.me/THE_GLACEON"),
        ],
        [
            InlineKeyboardButton(text="🌿 𝐇ᴇʟᴘ 🦋", callback_data="settings_back_helper"),
        ],
    ]
    return buttons
