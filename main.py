import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from keys import bot_key
import dream
import time
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

dreambot_prompts = [
    "Dreaming...Please hold on, this might take a moment",
    "Dreaming your creation into existence... Just a moment!",
    "Painting with pixels... Your dream image is on its way!",
    "Hold on tight! Dreambot is conjuring your vision.",
    "Let the metamorphosis begin! Your text is transforming into an image.",
    "Shhh... Dreambot is busy translating your dreamscape.",
    "We're working our magic! Your dream image will be ready soon.",
    "Just a brushstroke away from your masterpiece!",
    "Encoding your words into pixels... one moment please.",
    "Dreambot is taking flight! Get ready to see your vision take shape.",
    "Hold your breath! We're bringing your dream to life."
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello.....I can't wait to bring your imaginations to life\nWrite up a description and I'll dream up a picture."
    )


async def run_dreambot(update: Update, context: ContextTypes.DEFAULT_TYPE):

    time.sleep(1)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=random.choice(dreambot_prompts)
    )

    prompt = update.message.text
    dream.text2image(prompt)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="test.jpeg"
    )


async def run_animedreambot(update: Update, context: ContextTypes.DEFAULT_TYPE):

    time.sleep(1)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=random.choice(dreambot_prompts)
    )

    prompt = ' '.join(context.args)
    dream.text2anime(prompt)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="test.jpeg"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = (update.message.text).split()[0]
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Incorrect command: '{command}' is not a valid command"
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(bot_key).build()

    start_handler = CommandHandler('start', start)
    anime_handler = CommandHandler('anime', run_animedreambot)
    image_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), run_dreambot)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)


    application.add_handler(start_handler)
    application.add_handler(anime_handler)
    application.add_handler(image_handler)
    application.add_handler(unknown_handler)

    application.run_polling()