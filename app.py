from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo'

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

@app.route('perfil', defaults={'nome': 'fulano'})
@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome)

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x + 1
    return render_template('semestre.html', x=x, y=y)

@app.route('/contato')
def contato():
    nome='maria'
    email='maria@email.com'
    return render_template('contato.html', nome=nome, email=email)

#aula get e post
@app.route('/dados')
def dados():
    return render_template('dados.html')

#POST - x = request.form (dados escondidos, nao sao passados pela url)
#GET - x = request.args (dados a mostra, passados pela url)
@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    telefone = request.form['telefone']
    estado = request.form['estado']
    escolaridade = request.form['esc']
    return f"{nome} - {telefone} - {estado} - {escolaridade}"


if __name__ == '__main__':
    app.run()