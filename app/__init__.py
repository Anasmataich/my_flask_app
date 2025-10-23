from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h2>Flask Form</h2>"

    return app
