import telebot
import os
import magic
from utils import get_extension_from_mime
# token bot 
API_TOKEN = "6752827817:AAFk9rg2C07hO8mmdde_B8IgUqi8RtbhViI"

bot = telebot.TeleBot(API_TOKEN)
file_magic = magic.Magic(mime=True)
# file magic object for detecting file extension 


@bot.message_handler(content_types=['document', 'photo', 'video', 'audio'])
def handle_files(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        file_name = message.document.file_name or f"file_{file_info.file_unique_id}"
    elif message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = f"photo_{file_info.file_unique_id}"
    elif message.video:
        file_info = bot.get_file(message.video.file_id)
        file_name = f"video_{file_info.file_unique_id}"
    elif message.audio:
        file_info = bot.get_file(message.audio.file_id)
        file_name = f"audio_{file_info.file_unique_id}"
    else:
        bot.reply_to(message, "نوع فایل پشتیبانی نمی‌شود.")
        return

    downloaded_file = bot.download_file(file_info.file_path)

    if not file_name or '.' not in file_name:
        # if there was not a file name or it didnt have a file extension  
        mime_type = file_magic.from_buffer(downloaded_file)
        extension = get_extension_from_mime(mime_type)
        file_name += extension if extension else ''
    
    with open(f'downloaded_files/{file_name}', 'wb') as new_file:
        new_file.write(downloaded_file)
    
    bot.reply_to(message, "فایل دانلود شد!")

bot.polling()


