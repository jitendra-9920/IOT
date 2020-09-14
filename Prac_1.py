import telepot
token= '1171634261:AAH0HEa2onyiDDn-T7F3BA7FztrN6BG0pu4'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
content_type, chat_ty DCpe, chat_id = telepot.glance(msg)
print(content_type, chat_type, chat_id)

if content_type == 'text':
bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
