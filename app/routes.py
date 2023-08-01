from app import app

@app.route('/')
def index():
    return '''

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Currículo - Byanka Policiano Santos</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, 'Arial', sans-serif;
            line-height: 1.6;
            margin: 30px;
            background-color: #ffd9e3; /* Fundo rosa claro */
        }

        h1 {
            color: #e60073; /* Rosa mais forte para o título */
            font-family: 'Pacifico', cursive; /* Fonte similar à Barbie */
            text-align: center;
            font-size: 40px;
            margin-bottom: 20px;
            text-shadow: 2px 2px #ff80bf; /* Sombra no título */
        }

        h2 {
            color: #ff80bf; /* Rosa médio para os subtítulos */
            font-size: 24px;
            margin-top: 30px;
            margin-bottom: 10px;
            font-family: 'Comic Sans MS', cursive, 'Arial', sans-serif;
        }

        p {
            color: #333;
            font-size: 18px;
            text-align: justify;
        }

        .highlight {
            background-color: #ff80bf; /* Destaque em rosa médio */
            color: #fff; /* Texto em branco */
            padding: 3px 5px;
            border-radius: 5px;
        }

        .skill-list {
            list-style-type: none;
            padding: 0;
            margin: 10px 0;
        }

        .skill-list li {
            margin: 5px 0;
        }
    </style>
    <!-- Importando a fonte 'Pacifico' da Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
</head>
<body>
    <h1>Currículo Vitae</h1>

    <h2>Informações Pessoais</h2>
    <p><strong>Nome:</strong> Byanka Policiano Santos</p>
    <p><strong>Data de Nascimento:</strong> 10 de janeiro de 1995</p>
    <p><strong>Endereço:</strong> Rua das Flores, 123 - Cidade dos Sonhos, Estado Encantado</p>
    <p><strong>Telefone:</strong> (99) 9999-9999</p>
    <p><strong>Email:</strong> byanka.policiano@email.com</p>

    <h2>Objetivo</h2>
    <p>Busco uma posição em uma empresa que me permita desenvolver minhas habilidades e contribuir para o crescimento da organização.</p>

    <h2>Formação Acadêmica</h2>
    <p><strong>Graduação em Ciências da Imaginação</strong></p>
    <p>Universidade dos Sonhos, Estado Encantado</p>
    <p>Ano de conclusão: 2017</p>

    <h2>Experiência Profissional</h2>
    <p><strong>Assistente de Encantamento</strong></p>
    <p>Empresa Mágica Ltda, Estado Encantado</p>
    <p>Período: 2018 - Presente</p>
    <p>Responsabilidades: Contribuir para a realização de sonhos e encantar clientes em todos os momentos.</p>

    <h2>Idiomas</h2>
    <ul class="skill-list">
        <li><strong>Inglês:</strong> Avançado</li>
        <li><strong>Espanhol:</strong> Intermediário</li>
    </ul>

    <h2>Habilidades</h2>
    <ul class="skill-list">
        <li>Comunicação</li>
        <li>Trabalho em Equipe</li>
        <li>Criatividade</li>
        <li>Persistência</li>
        <li>Magia</li>
    </ul>

    <p><strong>Outras habilidades:</strong> <span class="highlight">Encantar crianças</span>, <span class="highlight">Organizar festas</span>, <span class="highlight">Fazer penteados glamorosos</span>.</p>
</body>
</html>




'''

@app.route('/contato')
def contato():
    return 'Meu contato: (84)98638-2768'

@app.route('/sobre')
def sobre():
    return 'Meu nome é Byanka, eu tenho 18 anos e estou cursando o 3º ano do ensino médio.'