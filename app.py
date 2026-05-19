from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        return '<h1>Connected to Database Successfully!</h1>'
    except:
        return '<h1>App is running! Database connecting...</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)