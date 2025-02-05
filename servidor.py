from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'k23jh4kj23h4'


@app.route('/')
def pag_home():
    return render_template('home.html')


@app.route('/info')
def pag_info():
    return render_template('info.html')

@app.route('/lista')
def pag_lista():
    return render_template('listaDoa.html')

@app.route('/pag_user')
def pag_user():
    return render_template('pag_usuario.html')

@app.route('/cadastro')
def pag_cadastro():
    return render_template('cadastro.html')


@app.route('/cadastro', methods=['POST'])
def inserir_usuario():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    tipo_sanguineo = request.form.get('tipo_sanguineo')
    email = request.form.get('email')
    senha = request.form.get('senha')


    if dao.inserir_usuario(nome, idade, tipo_sanguineo, email, senha):
        msgCadastro = 'Cadastro realizado com sucesso!'
    else:
        msgCadastro = 'Ops! Erro ao inserir usuário, tente novamente!'
    return render_template('login.html', mensagem=msgCadastro)


@app.route('/login')
def pag_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)

    if len(resultado) > 0:
        session['login'] = email

        return render_template('pag_usuario.html', usuario=resultado[0])
    else:
        msg = 'Ops! Senha ou email incorretos'
        return render_template('login.html', msglogin=msg)


@app.route('/agendar')
def pag_agendar():
    return render_template('agendamento.html')


@app.route('/agendar', methods=['POST'])
def agendar():
    if 'login' not in session:
        return redirect('/login')

    hemocentro = request.form.get('hemocentro')
    data = request.form.get('data')
    horario = request.form.get('horario')
    observacao = request.form.get('observacao')
    email = session['login']

    if dao.inserir_agendamento(hemocentro, data, horario, observacao, email):
        msgAgendar = 'Agendamento realizado com sucesso!'
        return redirect('/usuario')
    else:
        msgAgendar = 'Ops! Erro ao realizar agendamento, tente novamente.'
        return render_template('agendamento.html', mensagem=msgAgendar)

@app.route('/usuario')
def pag_usuario():
    if 'login' not in session:
        return redirect('/login')

    email = session['login']
    dados_usuario = dao.verificarlogin(email, "")
    historico_agendamentos = dao.buscar_agendamentos(email)

    if not dados_usuario:
        msgDados = 'Usuário não encontrado'
        return render_template("login.html", msgLogin=msgDados)

    return render_template("pag_usuario.html", usuario=dados_usuario[0], agendamentos=historico_agendamentos)


@app.route('/listardoadores')
def listar_doadores():
    usuarios = dao.listar_doadores()
    return render_template('listaDoa.html', lista=usuarios)

@app.route('/logout')
def logout():
    session.pop('login')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
