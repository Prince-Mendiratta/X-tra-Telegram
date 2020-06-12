"""COMMAND : .lovestory"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="lovestory"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit("Starting asf")

    animation_chars = [

            "1 鉂わ笍 love story",
            "  馃槓             馃槙 \n/馃憰\         <馃憲\ \n 馃憱               /|",    
            "  馃槈          馃槼 \n/馃憰\       /馃憲\ \n  馃憱            /|",
            "  馃槡            馃槖 \n/馃憰\         <馃憲> \n  馃憱             /|",
            "  馃槏         鈽猴笍 \n/馃憰\      /馃憲\ \n  馃憱          /|",
            "  馃槏          馃槏 \n/馃憰\       /馃憲\ \n  馃憱           /|",
            "  馃槝   馃槉 \n /馃憰\/馃憲\ \n   馃憱   /|",
            " 馃槼  馃榿 \n /|\ /馃憴\ \n /     / |",    
            "馃槇    /馃槹\ \n<|\      馃憴 \n /馃崋    / |",
            "馃槄 \n/(),鉁婐煒� \n /\         _/\\/|",
            "馃槑 \n/\\_,__馃槴 \n  //    //       \\",
            "馃槚 \n/\\_,馃挦_馃構  \n  //         //        \\",
            "  馃槶      鈽猴笍 \n  /|\   /(馃懚)\ \n  /!\   / \ ",
            "The End 馃槀..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
