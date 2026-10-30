from flask import Flask
app = Flask(__name__)


@app.route('/')
def home(): return "Home Page"

@app.route('/about')
def about(): return "About Page"

@app.route('/contact')
def contact(): return "Contact Page"

@app.route('/portfolio')
def portfolio(): return "Projects"


if __name__ == '__main__':
    app.run(debug=True)