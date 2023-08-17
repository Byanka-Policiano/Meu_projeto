from app import app, db
from flask import render_template, url_for, request, flash, session, redirect
from app.forms import Contato
from app.models import ContatoModel
from app.forms import Cadastro
from app.models import CadastroModel
import time 


@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    dados_formulario = None
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Seu formulário foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data
        
        novo_contato = ContatoModel(nome=nome, email=email, telefone=telefone, mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()
    return render_template('contatos.html', titulo = 'Contatos',formulario = formulario,dados_formulario = dados_formulario)


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    cadastro = Cadastro()
    print('Acessou a rota de cadastro')
    if cadastro.validate_on_submit():
        flash('Seu cadastro foi realizado com sucesso!')

        nome = cadastro.nome.data 
        sobrenome = cadastro.sobrenome.data
        email = cadastro.email.data
        senha = cadastro.senha.data

        novo_cadastro = CadastroModel(nome=nome, sobrenome=sobrenome, email=email,  senha=senha)
        db.session.add(novo_cadastro)
        db.session.commit()


    return render_template('cadastro.html', titulo = 'Cadastro', cadastro=cadastro)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        senha = request.form.get('senha')

        usuario = CadastroModel.query.filter_by(email = email, senha = senha).first()
        if usuario and usuario.senha == senha:
            session['email'] = usuario.id
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('Email ou senha inválido!')

    return render_template('login.html', titulo = 'Login')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/produtos')
def produtos():
    return render_template('produto.html',titulo = 'Produtos')



