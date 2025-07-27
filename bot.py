#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")  # El token se obtiene de la variable de entorno

if not BOT_TOKEN:
    raise RuntimeError("Error: La variable de entorno BOT_TOKEN no está configurada.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot desplegado en Render.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/start - Iniciar el bot\n"
        "/help - Mostrar esta ayuda"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Bot iniciado. Corriendo en Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
