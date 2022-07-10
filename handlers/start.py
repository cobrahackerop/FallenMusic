import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), 𝐀 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 𝐕𝐂 𝐏𝐋𝐀𝐘𝐄𝐑 𝐁𝐎𝐓 𝐅𝐎𝐑 𝐆𝐑𝐎𝐔𝐏 𝐕𝐂 🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭...

🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝐌𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 𝐔𝐬𝐞 𝐭𝐡𝐢𝐬 𝐭𝐲𝐩𝐢𝐧𝐠 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐭𝐨 𝐡𝐚𝐧𝐝𝐥𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★ Join   : [@ROYAL_FAMILYS]
┣★ ᴍᴀᴅᴇ ʙʏ: [🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭](t.me/{me})
┣★ join   : [@A_to_Zallbots]
┗━━━━━━━━━━━━━━┛

💞   🕊️⃝‌🦋𝐈𝐅 𝐘𝐎𝐔 𝐇𝐀𝐕𝐄 𝐀𝐍𝐘 𝐐𝐔𝐄𝐒𝐓𝐈𝐎𝐍𝐒 𝐀𝐁𝐎𝐔𝐓 𝐌𝐄 𝐓𝐇𝐄𝐍 𝐃𝐌 𝐓𝐎 𝐌𝐘  [ᴏᴡɴᴇʀ](t.me/{me}) 🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 𝐀𝐃𝐃 𝐌𝐄 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "💔 𝐎𝐖𝐍𝐄𝐑  💔", url=f"https://t.me/s_rajputt"
                    ),
                    InlineKeyboardButton(
                        "🍒 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 ɪɴʟɪɴᴇ 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "🤯 𝐒𝐎𝐔𝐑𝐂𝐄 🤯", url="https://github.com/srahput1234/FallenMusic"
                    )]
            ]
       ),
    )

