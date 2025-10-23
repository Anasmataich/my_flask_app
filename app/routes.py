from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        name = request.form.get('name', 'Unknown')
        message = f"Hello, {name}! Your message has been received."
    return render_template('index.html', message=message)

