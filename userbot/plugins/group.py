from userbot.utils import register

@register(outgoing=True, pattern="^.group$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("Hey there... Get in touch with me and show some love...\nJoin our community:\n\n[Channel](http://t.me/giveaways_24hrs)\n\n[Chat_Group](http://t.me/giveaways24hrsdiscuss)")
