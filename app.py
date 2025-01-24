from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello and welcome to Franz's Azure Web App!"  # Use double quotes to avoid conflict with single quote

if __name__ == '__main__':
    app.run()
