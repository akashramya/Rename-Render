# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23742095")

API_HASH = os.environ.get("API_HASH", "cdcf91cf0d034dfdadeb35375c28b96c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6844667179:AAGuHlUI7baF3iWQcu1t3F8Ha4bY9PVEDHI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "all_anime_in_tamil_ak") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Rename ak")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://akashfree253:9791577816ak@cluster0.tdamywz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1544613549').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
