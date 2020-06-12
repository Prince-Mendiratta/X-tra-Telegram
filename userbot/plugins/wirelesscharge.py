# For @UniBorg

"""Countdown Commands

.wchar"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(q?w)char'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n**Realme VOOC 5.0 Wireless Charging Started...**\nDevice Detected: `Realme 3 PRO`\nBattery Percentage: '

 j=21

 k=0

 for j in range(j):

  await e.edit(txt + str(k))

  k=k+5

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("**Realme VOOC 5.0 Wireless Charging Completed...**\nDevice Detected: `Realme 3 PRO`\nBattery Percentage: 100%",)


