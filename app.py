from flask import Flask
from src import scrape
import env

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY
)

@app.route('/', methods=['GET'])
def home():
    links = scrape.associated_press()
    output = ""
    for link in links:
        output += "<a href=\"{link}\">{link}</a><br/><br/>".format(link=link)
    return output

if __name__ == '__main__':
    app.run()
