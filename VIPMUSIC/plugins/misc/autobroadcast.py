import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = "{AUTO_GCAST}" if AUTO_GCAST else False


MESSAGE = f"""**🦋𝐁𝐞𝐬𝐭💥𝐌𝐮𝐬𝐢𝐜🔺𝐁𝐨𝐭🌸24𝐱7🧿𝐒𝐭𝐚𝐲🤞𝐎𝐧𝐥𝐢𝐧𝐞🏓
✨ 𝐆ʀᴏᴜᴘs + 𝐂ʜᴀɴɴᴇʟs 𝐕ᴄ. 💌

🎧 𝐏ʟᴀʏ + 𝐕ᴘʟᴀʏ + 𝐂ᴘʟᴀʏ 🎧

➥ 𝐒ᴜᴘᴘᴏʀᴛᴇᴅ 𝐖ᴇʟᴄᴏᴍᴇ - 𝐋ᴇғᴛ 𝐍ᴏᴛɪᴄᴇ, 𝐓ᴀɢᴀʟʟ, 𝐕ᴄᴛᴀɢ, 𝐁ᴀɴ - 𝐌ᴜᴛᴇ, 𝐒ʜᴀʏʀɪ, 𝐋ʏʀɪᴄs, 𝐒ᴏɴɢ - 𝐕ɪᴅᴇᴏ 𝐃ᴏᴡɴʟᴏᴀᴅ, 𝐄ᴛᴄ... 💕

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🌿 𝐊ɪᴅɴᴀᴘ 𝐌ᴇ 🌿", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE


async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=caption, reply_markup=BUTTON)
                    await asyncio.sleep(5)  # Sleep for 5 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    while True:
        await send_message_to_chats()

        # Wait for 200000 seconds before next broadcast
        await asyncio.sleep(200000)

# Start the continuous broadcast loop if AUTO_BROADCAST is True
if AUTO_GCASTS:  
    asyncio.create_task(continuous_broadcast())

