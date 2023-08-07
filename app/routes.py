from app import app
from flask import render_template
from app.forms import contato

@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos')
def contatos():
    dados_formulario = None
    formulario = contato()
    if formulario.validate_on_submit():
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data

        dados_formulario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'mensagem': mensagem
        }
    return render_template('contatos.html',titulo = 'Contatos')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/produtos')
def produtos():
    return render_template('produto.html',titulo = 'Produtos')