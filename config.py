from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH")
      API_ID = int(getenv("API_ID", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      FROM_CHANNEL = getenv("FROM_CHANNEL", "")
      TO_CHANNEL = getenv("TO_CHANNEL", "")
      PORT = getenv("PORT", "8080")
