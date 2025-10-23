from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])  # <--- إضافة POST هنا
    def index():
        if request.method == 'POST':
            name = request.form.get('name')
            return f"Hello, {name}!"
        return "<h2>Flask Form</h2>"

    return app
