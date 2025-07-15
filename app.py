from dotenv import load_dotenv
load_dotenv()


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "URL Shortener API"

if __name__ == '__main__':
    app.run(debug=True)
