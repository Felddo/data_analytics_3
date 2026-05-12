import telebot
from agent import run_agent
import os

TOKEN = токен
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет!\n"
        "Отправь мне файл в формате CSV или XLSX, и я напишу тебе о чем он"
    )


@bot.message_handler(content_types=['document'])
def handle_document(message):
    document = message.document
    file_name = document.file_name

    if not (file_name.lower().split(".")[-1] == "csv" or file_name.lower().split(".")[-1] == 'xlsx'):
        bot.reply_to(
            message,
            "Неподдерживаемый формат.\n"
            "Пожалуйста, отправь файл только в формате CSV или XLSX."
        )
        return

    file_path = f"./{file_name}"
    try:
        file_info = bot.get_file(document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(file_path, "wb") as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, f"Файл '{document.file_name}' принят")
        bot.send_message(message.chat.id,"Анализирую...")
        ans = run_agent(file_path)
        bot.send_message(message.chat.id, ans['text'])

        os.remove(file_path)

    except Exception as e:
        bot.reply_to(message, f"Ошибка при обработке файла: {e}")

print("Готовый")
bot.infinity_polling()
