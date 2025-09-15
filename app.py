from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo'

@app.route('/contato')
def contato():
    return 'angela.siqueira@ifrn.edu.br'

if __name__ == '__main__':
    app.run   