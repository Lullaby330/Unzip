# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID", "6216349"))
    API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6123506894:AAEn69pEzE7qrtYIsvmgIqOV0L7loDvLkEo")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001971221744"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://asubang:asubang@cluster0.gbyc7wo.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5280319640"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2040108421
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 6
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
