""" Powered by @Google
Available Commands:
.go <query>"""

import asyncio
import os
from re import findall
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
from urllib.parse import quote_plus
from urllib.error import HTTPError
from google_images_download import google_images_download
from gsearch.googlesearch import search
from userbot.utils import admin_cmd


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


@borg.on(admin_cmd("go (.*)"))
async def _(event):
    await event.edit("`UniBorg is Getting Information From Google Please Wait... ✍️🙇`")
    match_ = event.pattern_match.group(1)
    match = quote_plus(match_)
    if not match:
        await event.edit("`I can't search nothing !!`")
        return
    plain_txt = get(f"https://www.startpage.com/do/search?cmd=process_search&query={match}", 'html').text
    soup = BeautifulSoup(plain_txt, "lxml")
    msg = ""
    for result in soup.find_all('a', {'class': 'w-gl__result-title'}):
        title = result.text
        link = result.get('href')
        msg += f"**{title}**{link}\n"
    await event.edit(
        "**Google Search Query:**\n\n`" + match_ + "`\n\n**Results:**\n" + msg,
        link_preview = False)

