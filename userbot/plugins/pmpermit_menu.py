#   Copyright 2019 - 2020 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, LESS_SPAMMY
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned message in @XtraTgBot"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         Nudas = ("__ما هو جنسك ಠ_ಠ.__\n"
                  "`1`. ذكر 🧖\n"
                  "`2`. انثى 🧖‍♀\n"
                  "`3`. غير ذلك (حيوان 🌝🌿).\n")
         PM = ("`مرحباََ.. انت الان في قائمة بيرو 👨‍💻🌿 للسيد,`"
               f"{DEFAULTUSER}.\n"
               "هيا لنجعل هذا سلساََ اخبرني لماذا انت هنا.\n"
               "**اختر أحد الأسباب التالية لوجودك هنا رجائاََ ارسل رقم الاختيار (1،2،3،4،5) 🥀:**\n\n"
               "`1`. للدردشة مع سيدي\n"
               "`2`. إرسال رسائل مزعجه إلى سيدي.\n"
               "`3`. لاقتراح علاقه مع سيدي.\n"
               "`4`. للاستفسار عن شيء ما\n"
               "`5`. لطلب شيء من سيدي\n")
         ONE = ("حسنا. تم تسجيل طلبك. لا ترسل رسائل مزعجه الى سيدي. يمكنك توقع الرد في غضون 24 سنة ضوئية. إنه رجل مشغول ، على عكسك على الأرجح.\n\n"
                "**⚠️ سيتم حظرك والإبلاغ عنك إذا قمت بإرسال رسائل غير مرغوب فيها. ⚠️**\n\n"
                "__أرسل__ `start` __للعودة إلى القائمة الرئيسية.__")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**لست مرحاً ، هذا ليس منزلك. اذهب لأزعاج شخص آخر. لقد تم حظرك والإبلاغ عنك حتى إشعار آخر.**")
         FOUR = ("__حسنا. لم يشاهد سيدي رسالتك حتى الآن ، وعادةً ما يرد على الأشخاص الغرباء ، مع ذلك ساقوم بابلاغ سيدي برسالتك🥀 ..__\n __سيرد عندما يعود ، إذا رغب في ذلك ، فهناك بالفعل الكثير من الرسائل المعلقة 😶__\n **من فضلك لا ترسل رسائل مزعجه إلا إذا كنت ترغب في أن يتم حظرك والإبلاغ عنك.**")
         FIVE = ("`حسنا. يرجى الحصول على الأخلاق الأساسية لعدم إزعاج سيدي كثيرا. إذا رغب في مساعدتك فسوف يرد عليك قريبًا.`\n** لا تسأل مرارًا وتكرارًا والا سيتم حظرك والإبلاغ عنك.**")
         LWARN = ("**هذا هو التحذير الأخير الخاص بك. لا ترسل رسالة أخرى وإلا سيتم حظرك والإبلاغ عنك. كن صبور. سيرد عليك سيدي في اسرع وقت ممكن.**\n__أرسل__ `start` __للعودة الى القائمة الرئيسية.__")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "3":
             await borg.send_message(chat, Nudas)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             x = response.text
             if x == "1":
                 await borg.send_message(chat, "**انت غير مرحب بك 🌝🌿. \nغادر على الفور وإلا أصبحت منحرف (دوده 🌚🔥 ). سأرد عليك عندما أتصل بالإنترنت.**")
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "2":
                 await borg.send_message(chat, "`يا إلهي ، أنتِ مرحب بكِ هنا 🌝🥀.`\n\n **من فضلك لا تغمر محادثتي بالرسائل ، سيكون لدينا محادثة لطيفة بمجرد عودتي 🌝🌿**")
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "3":
                 await borg.send_message(chat, "`رجائاً لايسمح بدخول الحيوانات هنا 🌝🌿,\n عليك ان تكون بشراً لاقتراح علاقه مع سيدي 🎭, ان لم تكن فتاة جميلة,\n فلا ترسل المزيد من الرسائل ودع سيدي يرى بنفسه اذا كان يريد الحديث معك.`")
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             else:
                 await borg.send_message(chat, "__لقد قمت بإدخال أمر غير صالح. ارجوك ارسل__ `start` __مرة أخرى أو لا ترسل رسالة أخرى إذا كنت لا ترغب في الحظر والإبلاغ.__")
                 response = await conv.get_response(chat)
                 if not response.text.startswith("start"):
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "5":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`لقد قمت بإدخال أمر غير صالح. ارجوك ارسل start مرة أخرى أو لا ترسل رسالة أخرى إذا كنت لا ترغب في الحظر والإبلاغ.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))


