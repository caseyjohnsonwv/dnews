from flask import Flask
from src import scrape
import env

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY
)

@app.route('/', methods=['GET'])
def home():
    return '<br/>'.join(scrape.associated_press())

if __name__ == '__main__':
    app.run()
