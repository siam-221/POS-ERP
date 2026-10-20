import os
# ===== এখানে সেটিং বদলান =====
SOURCES = [
    {"name": "Alien Tees", "url": "https://media-cdn.storex.dev/alienteesbd/facebook-catalog-products/datafeed.csv?85894503"},
    {"name": "Bodyfitters", "url": "https://media-cdn.storex.dev/bodyfittersbd/facebook-catalog-products/datafeed.csv?23607050"},
]
SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")
ADMIN_USER = os.environ.get("ADMIN_USER", "admin")      # প্রথমবার চালালে এই অ্যাডমিন তৈরি হবে
ADMIN_PASS = os.environ.get("ADMIN_PASS", "alien@123")  # চালু করার আগেই বদলে নিন
CACHE_TTL = 600  # সেকেন্ড: কত পর পর CSV ও স্টক রিফ্রেশ হবে
STOCK_TTL = 60  # সেকেন্ড: গুগল শিট থেকে স্টক কত পর পর নতুন করে আনবে
