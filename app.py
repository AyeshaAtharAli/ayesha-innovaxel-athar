from flask import Flask, request, jsonify, render_template, redirect
from datetime import datetime
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Import your custom modules
from utils import generate_short_code
from models import (
    create_url_record,
    get_url_by_shortcode,
    update_url,
    delete_url,
    increment_access_count
)

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Home route — serves frontend page
@app.route('/')
def home():
    return render_template('index.html')

# ✅ POST /shorten: Create a short URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    short_code = generate_short_code()
    create_url_record(url, short_code)
    now = datetime.utcnow().isoformat() + "Z"

    return jsonify({
        "url": url,
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now
    }), 201

# ✅ GET /shorten/<short_code>: Retrieve original URL
@app.route('/shorten/<short_code>', methods=['GET'])
def retrieve_url(short_code):
    record = get_url_by_shortcode(short_code)
    if not record:
        return jsonify({"error": "Short URL not found"}), 404

    increment_access_count(short_code)
    record['_id'] = str(record['_id'])  # Convert ObjectId to string
    return jsonify(record), 200

# ✅ PUT /shorten/<short_code>: Update existing URL
@app.route('/shorten/<short_code>', methods=['PUT'])
def update_short_url(short_code):
    data = request.json
    new_url = data.get("url")
    if not new_url:
        return jsonify({"error": "Missing URL"}), 400

    updated = update_url(short_code, new_url)
    if not updated:
        return jsonify({"error": "Short URL not found"}), 404

    updated['_id'] = str(updated['_id'])
    updated['updatedAt'] = datetime.utcnow().isoformat() + "Z"
    return jsonify(updated), 200

# ✅ DELETE /shorten/<short_code>: Delete a short URL
@app.route('/shorten/<short_code>', methods=['DELETE'])
def delete_short_url(short_code):
    result = delete_url(short_code)
    if result.deleted_count == 0:
        return jsonify({"error": "Short URL not found"}), 404
    return '', 204

# ✅ GET /stats/<short_code>: Get usage stats
@app.route('/stats/<short_code>', methods=['GET'])
def get_url_stats(short_code):
    record = get_url_by_shortcode(short_code)
    if not record:
        return jsonify({"error": "Short URL not found"}), 404
    record['_id'] = str(record['_id'])
    return jsonify(record), 200

# ✅ Optional: Redirect /<short_code> to original URL
@app.route('/<short_code>')
def redirect_to_original(short_code):
    record = get_url_by_shortcode(short_code)
    if record:
        increment_access_count(short_code)
        return redirect(record['url'])
    else:
        return "Short URL not found", 404

# ✅ Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
