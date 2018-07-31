from flask import Flask, request, render_template
from jinja2 import Environment

app = Flask(__name__, template_folder="templates")
Jinja2 = Environment()

@app.route("/")
def index():
    if 'name' in request.args and len(request.args['name']) > 0:
        message = Jinja2.from_string('Happy Birthday to ' + request.args['name'] + '!').render().title()
        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
