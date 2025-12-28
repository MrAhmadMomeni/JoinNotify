from pypresence import Presence
import time

# =======================
# تنظیمات اصلی
CLIENT_ID = "1453703231673864192"  # ← جایگزین با Application ID
DETAILS = "من کنت مولاه فهذا علی مولاه"   # متن بالایی
STATE = "مولا امیرالمومنین علی بن ابی طالب (علیه السلام)"     # متن پایین
LARGE_IMAGE = "Emam-Ali"            # اسم آیکن آپلود شده
LARGE_TEXT = "Emam-Ali"     # هاور آیکن
BUTTONS = [{"label": "بیشتر بدانید", "url": "https://bot-sazan.site/aliebnabitaleb.html"}]  # دکمه لینک
# =======================

# اتصال به Discord RPC
RPC = Presence(CLIENT_ID)
RPC.connect()

# زمان شروع تایمر
start_time = int(time.time()) - 1525200

# فعال کردن Rich Presence
RPC.update(
    details=DETAILS,
    state=STATE,
    large_image=LARGE_IMAGE,
    large_text=LARGE_TEXT,
    start=start_time,
    buttons=BUTTONS
)

# حلقه برای آپدیت هر 15 ثانیه
while True:
    time.sleep(15)