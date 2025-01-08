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

    if dao.inserir_user(nome, idade, tipo_sanguineo, email, senha):
        msgCadastro = 'Cadastro realizado com sucesso!'
    else:
        msgCadastro = 'Ops! Erro ao inserir usuário, tente novamente!'
    return render_template('cadastro.html', mensagem=msgCadastro)


@app.route('/login')
def pag_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def fazer_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)

    if len(resultado) > 0:
        session['login'] = resultado[0][1]
        return render_template('pag_usuario.html', user=resultado[0][1])
    else:
        msg = 'Ops! Senha ou email incorretos'
        return render_template('login.html', msglogin=msg)


@app.route('/agendar')
def pag_agendar():
    return render_template('agendamento.html')


@app.route('/agendar', methods=['POST'])
def agendar():
    hemocentro = request.form.get('hemocentro')
    data = request.form.get('data')
    horario = request.form.get('horario')
    observacao = request.form.get('observacao')

    if dao.inserir_agendamento(hemocentro, data, horario, observacao):
        msgAgendar = 'Agendamento realizado com sucesso!'
    else:
        msgAgendar = 'Ops! Erro ao realizar agendamento, tente novamente.'

    return render_template('agendamento.html', mensagem=msgAgendar)


@app.route('/usuario')
def pag_usuario(historico_agendamentos=None):
    if 'login' not in session:
        return redirect('/login')
    email = session['login']
    dados_usuario = dao.buscar_dados_usuario(email)
    historico_agendamentos = dao.buscar_agendamentos_usuario(email)

    if not dados_usuario:
        return render_template('erro.html', mensagem="Usuário não encontrado")

    return render_template("pag_usuario.html", usuario = dados_usuario, agendamentos = historico_agendamentos)

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect('/login')

if __name__ == "__main__":
 app.run(debug=True)
