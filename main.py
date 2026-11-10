import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import yt_dlp
TOKEN = os.getenv("TELEGRAM_TOKEN")
logging.basicConfig(level=logging.INFO)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ابعتلي رابط فيديو من تيك توك، انستا، فيس او يوتيوب")
async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    if not url.startswith("http"):
        await update.message.reply_text("ابعت رابط صحيح")
        return
    await update.message.reply_text("جاري التحميل... ⏳")
    try:
        ydl_opts = {'format': 'mp4/best', 'outtmpl': 'video.%(ext)s', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        await update.message.reply_video(video=open(filename, 'rb'))
        os.remove(filename)
    except Exception:
        await update.message.reply_text("ما قدرت حمل الفيد
