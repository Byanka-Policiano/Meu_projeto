from app import app, db, bcrypt
from flask import render_template, url_for, request, flash, session, redirect
from app.forms import Contato
from app.models import ContatoModel
from app.forms import Cadastro
from app.models import CadastroModel
from flask_bcrypt import check_password_hash
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
    print('Acessou a rota de cadastro!')
    if cadastro.validate_on_submit():
        flash('Seu cadastro foi realizado com sucesso!')
        nome = cadastro.nome.data
        sobrenome = cadastro.sobrenome.data
        email = cadastro.email.data
        telefone = cadastro.telefone.data
        cpf = cadastro.cpf.data
        endereco = cadastro.endereco.data
        bairro = cadastro.bairro.data
        cidade = cadastro.cidade.data
        uf = cadastro.uf.data
        senha = cadastro.senha.data
        hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        novo_cadastro = CadastroModel(nome = nome, sobrenome = sobrenome, email = email, telefone = telefone, cpf = cpf, endereco = endereco, bairro = bairro, cidade = cidade, uf = uf, senha = hash_senha)
        db.session.add(novo_cadastro)
        db.session.commit() 

    return render_template('cadastro.html', tituto = 'Cadastro',cadastro = cadastro)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        senha = request.form.get('senha') 
        usuario = CadastroModel.query.filter_by(email=email).first()

        print("Email digitado:", email)
        print("Senha digitada:", senha)
        
        if usuario:
            print("Hash de senha no banco de dados:", usuario.senha)
            if bcrypt.check_password_hash(usuario.senha, senha):
                print("Senha válida. Efetuando login...")
                session['email'] = usuario.email
                session['nome'] = usuario.nome
                session['sobrenome'] = usuario.sobrenome
                session['cidade'] = usuario.cidade
                session['uf'] = usuario.uf

                time.sleep(2)
                return redirect(url_for('index'))
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")
            flash('E-mail ou senha inválido!')

    return render_template('login.html', titulo='Login')





@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/produtos')
def produtos():
    return render_template('produto.html',titulo = 'Produtos')

@app.route('/editar', methods={'POST','GET'})
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.sobrenome = request.form.get('sobrenome')
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')
        usuario.cpf = request.form.get('cpf')
        usuario.endereco = request.form.get('endereco')
        usuario.bairro = request.form.get('bairro')
        usuario.cidade = request.form.get('cidade')
        usuario.uf = request.form.get('uf')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit() 
        session['email'] = usuario.email
        session['nome'] = usuario.nome
        session['sobrenome'] = usuario.sobrenome
        session['telefone'] = usuario.telefone
        session['cpf'] = usuario.cpf
        session['endereco'] = usuario.endereco
        session['bairro'] = usuario.bairro
        session['cidade'] = usuario.cidade
        session['uf'] = usuario.uf
        session['senha'] = usuario.senha
        flash('Seus dados foram atualizados com sucesso!')

    return render_template('editar.html',titulo = 'Editar')


@app.route('/sair')
def sair():
     session['email'] = None
     session['nome'] = None
     session['sobrenome'] = None
     session['senha'] = None
     return redirect(url_for('login'))

@app.route('/excluir_conta', methods=['GET'])
def excluir_conta():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    db.session.delete(usuario)
    db.session.commit()
    session.clear()

    flash('Sua conta foi excluida com sucesso!')
    return redirect(url_for('cadastro'))