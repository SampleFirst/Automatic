from pyrogram import Client, filters


@Client.on_message(filters.channel & filters.text)
async def delete_aut_messages(client, message):
    if "@Auto_Forward_Messages_Bot" in message.text:
        await message.delete()
    elif "Url not found in post!" in message.text:
        await message.delete()
    elif "We could not locate an affiliate" in message.text:
        await message.delete()
    elif "No Deal Found !" in message.text:
        await message.delete()

