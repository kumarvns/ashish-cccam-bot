import os
from datetime import datetime
from logging import exception

from main import cline
from telethon.sessions import StringSession
from telethon import TelegramClient,events
import asyncio


try:
    api_id = os.environ.get("API_KEY")
    api_hash = os.environ.get("API_HASH")
    stringsession = os.environ.get("STRING")
    client = TelegramClient(StringSession(stringsession),api_id,api_hash)
    client.start()

    ch = ['🙂','😌','😋','😛','😝','😜','🤪','🤓']

    @client.on(events.NewMessage(outgoing=True))
    async def my_event_handler(event):
        if event.raw_text == ('.fun'):
            c = "You Stupid! "
            for i in ch:
                d = c + i
                await event.edit(d)
                await asyncio.sleep(0.5)

        elif event.raw_text == ".ccam":
            initial_message = await event.edit("**Wait Generating Cline...**")
            final = cline()
            await initial_message.edit(final)

        elif event.raw_text == ".ping":
            start = datetime.now()
            wait = await event.edit("Ping 🥍")
            end = datetime.now()
            ping = round((end - start).microseconds / 1000, 2)
            await wait.edit(f"**Pong!!**\n ms=> `{ping}`")

        elif event.raw_text == ".utube":
            os.system("python3 youtube.py")
    client.run_until_disconnected()
except exception as e:
    print(e)

#find another Commands and requests from tl.telethon.dev
