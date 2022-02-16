with open("xnew.txt", "w") as m:
  m.write("Ankit X xnkit\n"*10**10)
  m.close()
await bot.send_message(chat, file="xnew.txt")
