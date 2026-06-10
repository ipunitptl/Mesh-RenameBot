from .core.get_config import get_var
from .core.handlers import add_handlers
from .mesh_bot import MeshRenameBot
from . maneuvers.ExecutorManager import ExecutorManager
import logging

from flask import Flask
from threading import Thread
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

Thread(target=run_web, daemon=True).start()

# TODO Add a alert for an extra space recorded

if __name__ == "__main__":

    rbot = MeshRenameBot("MeshRenameBot", get_var("API_ID"), get_var("API_HASH"), 
                         bot_token=get_var("BOT_TOKEN"), workers=200)
    excm = ExecutorManager()
    add_handlers(rbot)
    rbot.run()
