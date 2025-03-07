import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, SUPPORT_GROUP
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(
    command(["play", "p", "fuck"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    await message.delete()

    fallen = await message.reply("» 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆⏩⏩..𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭🕊️⃝‌🦋𝐌𝐮𝐬𝐢𝐜")

    chumtiya = message.from_user.mention

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Anonymous"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await fallen.edit(
                        "<b>» 𝐅𝐈𝐑𝐒𝐓𝐈𝐋𝐘 𝐌𝐀𝐊𝐄 𝐌𝐄 admin 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "» ᴀssɪsᴛᴀɴᴛ sᴜᴄᴄᴇssꜰᴜʟʏ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ ʙᴀʙʏ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ sᴏɴɢs​.")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>» 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐈𝐍 𝐂𝐇𝐀𝐓 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭, 𝐉𝐎𝐈𝐍 𝐅𝐈𝐑𝐒𝐓 𝐓𝐈𝐌𝐄 𝐓𝐎 𝐎𝐑𝐃𝐄𝐑 𝐓𝐇𝐄 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐓𝐎 𝐉𝐎𝐈𝐍 𝐘𝐎𝐔𝐑 𝐂𝐇𝐀𝐓     .")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>» ᴀssɪsᴛᴀɴᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜɪs ᴄʜᴀᴛ.</i>\n\nʀᴇᴀsᴏɴ : {e}")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"» 𝐒𝐎𝐑𝐑𝐘 𝐒 𝐑𝐀𝐉𝐏𝐔𝐓, 𝐓𝐑𝐀𝐂𝐊 𝐋𝐎𝐍𝐆𝐄𝐑 𝐓𝐇𝐄𝐍  {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ"
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            title = "NaN"
            duration = "NaN"
            views = "NaN"

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"» 𝐒𝐎𝐑𝐑𝐘 𝐒 𝐑𝐀𝐉𝐏𝐔𝐓, 𝐓𝐑𝐀𝐂𝐊 𝐋𝐎𝐍𝐆𝐄𝐑 𝐓𝐇𝐄𝐍  {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await fallen.edit(
                "» 𝐒𝐎𝐌𝐄 𝐓𝐄𝐗𝐓 𝐓𝐎 𝐒𝐄𝐀𝐑𝐂𝐇 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭🕊️⃝‌🦋 𝐌𝐮𝐬𝐢𝐜"
            )
        await fallen.edit("🔎")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await fallen.edit(
                "» ɴᴏᴛ ғᴏᴜɴᴅ, ᴛʀʏ sᴇᴀʀᴄʜɪɴɢ ᴡɪᴛʜ ᴛʜᴇ sᴏɴɢ ɴᴀᴍᴇ ʙᴀʙʏ"
            )
            print(str(e))
            return

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"» sᴏʀʀʏ ʙᴀʙʏ, ᴛʀᴀᴄᴋ ʟᴏɴɢᴇʀ ᴛʜᴀɴ  {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_text(
            text=f"**» ᴛʀᴀᴄᴋ ǫᴜᴇᴜᴇᴅ ᴀᴛ {position} ʙᴀʙʏ**\n📌 **ᴛɪᴛʟᴇ​ :**[{title[:65]}]({url})\n\n🕕** ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` **ᴍɪɴᴜᴛᴇs**\n💕** ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ​ : **{chumtiya}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• sᴜᴩᴩᴏʀᴛ •", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("» ᴄʟᴏsᴇ «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
        await message.reply_text(
            text=f"** » 𝐍𝐎𝐖 𝐏𝐋𝐀𝐘𝐈𝐍𝐆 𝐒 𝐑𝐚𝐣𝐩𝐮𝐭🕊️⃝‌🦋 𝐌𝐮𝐬𝐢𝐜 «**\n\n **🕊️⃝‌🦋𝐓𝐈𝐓𝐋𝐄​:** [{title[:65]}]({url})\n\n🕕 **🕊️⃝‌🦋𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍:** `{duration}` ᴍɪɴᴜᴛᴇs\n\n💕 **🕊️⃝‌🦋𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃​:** {chumtiya}\n\n💔 **🕊️⃝‌🦋𝐏𝐋𝐀𝐘𝐈𝐍𝐆 𝐈𝐍​:** `{message.chat.title}`\n\n🎥 **🕊️⃝‌🦋𝐒𝐓𝐑𝐄𝐀𝐌 𝐓𝐘𝐏𝐄:** ʏᴏᴜᴛᴜʙᴇ ᴍᴜsɪᴄ\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• sᴜᴩᴩᴏʀᴛ •", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("» ᴄʟᴏsᴇ «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

    return await fallen.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
