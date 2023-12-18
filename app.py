from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/praticas')
def Praticas():  # put application's code here
    return render_template("Praticas.html")

@app.route('/programas')
def programas():  # put application's code here
    return render_template("Programas.html")

@app.route('/vida')
def vida():  # put application's code here
    return render_template("Vida.html")

if __name__ == '__main__':
    app.run()
