import asyncio
from pyrogram import Client
from helpers.filters import command
from config import SUDO_USERS, BOT_NAME as bn, BOT_USERNAME as lel, PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"𝗛𝗘'𝗟𝗟 {message.from_user.mention()},\n🅱🅾🆃 [{bn}](t.me/{lel}) 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐃𝐨𝐧'𝐭📵 𝐓𝐫𝐲 𝐓𝐨 [𝐒𝐩𝐚𝐦] 𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐘𝐨𝐮𝐫 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐁𝐚𝐧 𝐅𝐫𝐨𝐦 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦. \n\n𝐌𝐲 𝐌𝐢𝐬𝐭𝐞𝐫 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐒𝐦𝐬 𝐑𝐞𝐩𝐥𝐲 𝐓𝐡𝐞𝐧 𝐀𝐮𝐭𝐨 𝐈𝐦𝐩𝐫𝐨𝐯𝐞𝐝 𝐓𝐡𝐢𝐬 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝓑𝔂 [🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭](t.me/{OWNER_USERNAME}).\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥱 ʙᴏᴛ 🥱", url=f"https://t.me/{lel}"
                    ),
                    InlineKeyboardButton(
                        "💖 sᴜᴩᴩᴏʀᴛ 💖", url="https://github.com/srahput1234/FallenMusic"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💞 ᴏᴡɴᴇʀ​​ 💞", url=f"https://t.me/{OWNER_USERNAME}"
                    )]
            ]
        ),

    )
            return


@Client.on_message(filters.command(["pm", "pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("» ᴘᴍ ᴘᴇʀᴍɪᴛ ᴇɴᴀʙʟᴇᴅ ʙᴀʙʏ.")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("» ᴘᴍ ᴘᴇʀᴍɪᴛ ᴅɪsᴀʙʟᴇᴅ ʙᴀʙʏ.")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("» 𝓝𝓸𝔀 𝔂𝓸𝓾 𝓬𝓪𝓷 𝓶𝓼𝓰 𝓽𝓸  🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 ..")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", ["!", ".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("» ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", ["!", ".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("» ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​.")
        return
    message.continue_propagation()
