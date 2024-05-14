import logging
import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config

logger = logging.getLogger(__name__)

@channelforward.on_message(filters.channel)
async def forward(client, message):
    try:
        from_channel = Config.FROM_CHANNEL
        to_channel = Config.TO_CHANNEL
        if message.chat.id == int(from_channel):
            func = message.copy if Config.AS_COPY else message.forward
            await func(int(to_channel))
            logger.info(f"Forwarded a message from {from_channel} to {to_channel}")
            await asyncio.sleep(1)
    except Exception as e:
        logger.exception(e)
