from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'k23jh4kj23h4'


@app.route('/')
def pag_home():
    return render_template('home.html')

@app.route('/homeuser')
def pag_user():
    return render_template('homeuser.html')

@app.route('/info')
def pag_info():
    return render_template('info.html')

@app.route('/lista')
def pag_lista():
    return render_template('listaDoa.html')

@app.route('/voltaruser')
def voltaruser():
    return render_template('pag_usuario.html')

@app.route('/voltar')
def voltar():
    return render_template('homeuser.html')

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


@app.route('/listaragendamentos')
def a():
    historico_agendamentos = dao.buscar_agendamentos(session['login'])
    return render_template("listaragendamentos.html", agendamentos=historico_agendamentos)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)


    if len(resultado) > 0:
        historico_agendamentos = dao.buscar_agendamentos(session['login'])
        session['login'] = email
        session['dados'] = resultado[0]
        if len(historico_agendamentos) > 0:
            return render_template("pag_usuario.html", usuario=session['dados'], agendamentos=historico_agendamentos)
        else:
            return render_template('pag_usuario.html', usuario=resultado[0])

    else:
        msg = 'Ops! Senha ou email incorretos'
        return render_template('login.html', msglogin=msg)


@app.route('/agendar', methods=['POST','GET'])
def agendar():

    if request.method == 'GET' and 'login' in session:
        return render_template('agendamento.html')

    if 'login' not in session:
        return redirect('/login')


    hemocentro = request.form.get('hemocentro')
    data = request.form.get('data')
    horario = request.form.get('horario')
    observacao = request.form.get('observacao')
    email = session['login']
    print(hemocentro, data, horario, observacao)

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
    historico_agendamentos = dao.buscar_agendamentos(email)

    if not historico_agendamentos:
        msgDados = 'Dados não  encontrados'
        return render_template("login.html", msgLogin=msgDados)

    return render_template("pag_usuario.html", usuario=session['dados'], agendamentos=historico_agendamentos)


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
