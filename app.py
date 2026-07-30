from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> موقعي يعمل على GitHub! </h1>"

if name == '__main__':
    app.run()
