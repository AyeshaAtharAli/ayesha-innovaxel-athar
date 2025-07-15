# 🔗 URL Shortener API – Python Flask + MongoDB

This is a simple URL Shortener RESTful API built using **Python (Flask)** and **MongoDB**. It allows users to generate short URLs, retrieve original URLs, track access statistics, and manage (update/delete) existing short links.

A minimal frontend (HTML + JavaScript) is included to interact with the API visually. Short URLs behave like Bitly and support automatic redirection.

---

## 🚀 Live Demo

🔗 [Click to Try the Live Deployed App](https://5ed486cf-44bb-44e8-8b73-b0ac09b3ff3b-00-5n3brgxwycpk.sisko.replit.dev/)

> (Replace this link with your actual Render deployment URL)

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB (MongoDB Atlas)
- **Frontend:** HTML, JavaScript (served via Flask)
- **Config:** `python-dotenv`

---

## 📁 Project Structure

ayesha-innovaxel-athar/
├── app.py               # Main Flask app with routes
├── models.py            # MongoDB interaction logic
├── utils.py             # Shortcode generator
├── requirements.txt     # Dependency list
├── README.md            # This file (main branch only)
├── .env                 # Local config (should not be pushed)
├── templates/
│   └── index.html       # Frontend form
└── __pycache__/         # Should be ignored (compiled Python)


---

## ⚙️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB (via Atlas)
- **Frontend**: HTML + JavaScript (rendered by Flask)
- **Environment Config**: python-dotenv

---

## 📮 API Endpoints

| Method | Endpoint                 | Description                        |
|--------|--------------------------|------------------------------------|
| POST   | `/shorten`               | Create a short URL                 |
| GET    | `/shorten/<short_code>`  | Get details of a short URL         |
| PUT    | `/shorten/<short_code>`  | Update a short URL                 |
| DELETE | `/shorten/<short_code>`  | Delete a short URL                 |
| GET    | `/stats/<short_code>`    | View access stats                  |
| GET    | `/<short_code>`          | Redirect to original URL           |

---

## 🧪 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/ayesha-innovaxel-athar.git
cd ayesha-innovaxel-athar
git checkout dev

2. Install Dependencies

pip install -r requirements.txt


3. Set Up .env
Create a .env file in the project root:
Use MongoDB Atlas URI for MONGO_URI.

4. Run the App
python app.py

Visit http://localhost:5000 to test the app.

🌍 Deployment Instructions (Render + MongoDB Atlas)
1. MongoDB Setup
Go to https://www.mongodb.com/cloud/atlas

Create a free shared cluster

Create a database url_shortener with collection urls

Create a DB user and whitelist 0.0.0.0/0

Copy your connection URI

2. Deploy on Render
Go to https://render.com

Create a new Web Service

Link your GitHub repo

Use these values:

| Setting       | Value                             |
| ------------- | --------------------------------- |
| Branch        | `dev`                             |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python app.py`                   |
| Runtime       | Python                            |

Add Environment Variables:
MONGO_URI=your_atlas_uri_here
BASE_URL=https://your-render-url.onrender.com

Click Create Web Service and wait for it to deploy.

Notes
.env is excluded from GitHub via .gitignore

main branch contains only the README.md file

Full source code is on the dev branch

👩‍💻 Developer
Ayesha Athar
 GitHub: https://github.com/AyeshaAtharAli/ayesha-innovaxel-athar
 