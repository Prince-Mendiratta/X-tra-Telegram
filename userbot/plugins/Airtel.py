"""Emoji

Available Commands:

.airtel"""

from telethon import events

import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 19)

    input_str = event.pattern_match.group(1)

    if input_str == "airt":

        await event.edit(input_str)

        animation_chars = [

        

            "`Connecting To Airtel Paid  Network...`",

            "`█ ▇ ▆ ▅ ▄ ▂ ▁`",

            "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",

            "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",

            "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",    

            "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",

            "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",

            "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",

            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",

            "*Optimising Network...*",

            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",

            "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",           

            "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",

            "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",

            "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",

            "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",

            "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",

            "`▁ ▂ ▄ ▅ ▆ ▇ █`",

            "**Airtel Network Boosted....**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 19])
