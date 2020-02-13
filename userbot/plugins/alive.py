""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Hey! I'm alive. All systems online and functioning normally... ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @xditya\n`Database Status: Databases functioning normally!\n\nI will be always with you, my master!\n`"
                     f"`My owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/xditya/X-tra-Telegram)")
