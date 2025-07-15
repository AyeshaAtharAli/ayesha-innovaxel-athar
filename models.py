from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database()
collection = db.urls

# ✅ 1. Create a new URL record
def create_url_record(original_url, short_code):
    now = datetime.utcnow()
    return collection.insert_one({
        "url": original_url,
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    })

# ✅ 2. Get a URL by shortcode
def get_url_by_shortcode(short_code):
    return collection.find_one({"shortCode": short_code})

# ✅ 3. Update a URL
def update_url(short_code, new_url):
    now = datetime.utcnow()
    return collection.find_one_and_update(
        {"shortCode": short_code},
        {"$set": {"url": new_url, "updatedAt": now}},
        return_document=True
    )

# ✅ 4. Delete a URL
def delete_url(short_code):
    return collection.delete_one({"shortCode": short_code})

# ✅ 5. Increment access count
def increment_access_count(short_code):
    return collection.update_one(
        {"shortCode": short_code},
        {"$inc": {"accessCount": 1}}
    )
