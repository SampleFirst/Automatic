import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
AS_COPY = is_enabled((environ.get('AS_COPY', "True")), True)
FROM_CHANNEL = int(environ.get('FROM_CHANNEL', 0))
TO_CHANNEL = int(environ.get('TO_CHANNEL', 0))
PORT = environ.get("PORT", "8080")
