"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
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
    await alive.edit("`Re Abhi Zinda Hu Malik!` **ψ(｀∇´)ψ**\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n"
                     "`Bot created by:` [SnapDragon] @anubisxx\n"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     
