from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='./')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        a = request.form['left']
        b = request.form['right']
        c = float(a) + float(b)
        print(type(request))
        print(type(request.form))
        return render_template('add.html', RESULT=str(c))
    return render_template('add.html')


if __name__ == "__main__":
    app.run()

