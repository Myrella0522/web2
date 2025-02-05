import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='dpg-cu2m28q3esus73ckotgg-a.oregon-postgres.render.com',
        database='projetoma',
        user='projetoma_user',
        password='VYfw8JvPx8UoVURIocBoo9Vb4vkl32xV'
    )
    return con

def inserir_usuario(nome, idade, tipo_sanguineo, email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False

    try:
        sql = f"INSERT INTO usuarios (nome, idade, tipo_sanguineo, email, senha) VALUES ('{nome}', '{idade}', '{tipo_sanguineo}', '{email}', '{senha}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT nome, idade, tipo_sanguineo, email FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset
def inserir_agendamento(hemocentro, data, horario, observacao, email):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False

    try:
        sql = f"INSERT INTO agendamentos (hemocentro, data, horario, observacao, email) VALUES ('{hemocentro}', '{data}', '{horario}', '{observacao}', '{email}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito


def buscar_agendamentos(email):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT hemocentro, data, horario, observacao FROM agendamentos WHERE email = '{email}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset


def listar_doadores():
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute("SELECT nome FROM usuarios")

    recset = cur.fetchall()
    conexao.close()

    return recset

