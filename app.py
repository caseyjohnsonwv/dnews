from flask import Flask
import env

app = Flask(__name__)
app.config.update(
    SECRET_KEY = env.APP_SECRET_KEY
)

@app.route('/', methods=['GET'])
def home():
    return "Hello world!"

if __name__ == '__main__':
    app.run()
