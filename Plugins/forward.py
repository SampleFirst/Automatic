import logging
import asyncio
from pyrogram import Client, filters
from info import FROM_CHANNEL, TO_CHANNEL, AS_COPY

logger = logging.getLogger(__name__)

@Client.on_message(filters.chat)
async def forward(client, message):
    try:
        from_channel = FROM_CHANNEL
        to_channel = TO_CHANNEL
        if message.chat.id == int(from_channel):
            func = message.copy if AS_COPY else message.forward
            await func(int(to_channel))
            await asyncio.sleep(1)
    except Exception as e:
        logger.exception(e)
