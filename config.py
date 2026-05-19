from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

LEAGUES = [
    "EDGE base",
    "EDGE core",
    "EDGE flow",
    "EDGE pro",
    "EDGE prime",
    "EDGE elit",
    "EDGE MIET",
]
