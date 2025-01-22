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
    cur.execute(f"SELECT email, nome FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset

def inserir_agendamento(hemocentro, data, horario, observacao):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False

    try:
        sql = f"INSERT INTO agendamentos (hemocentro, data, horario, observacao) VALUES ('{hemocentro}', '{data}', '{horario}', '{observacao}')"
        cur.execute(sql)
        conexao.commit()
        exito = True
    except psycopg2.Error as e:
        conexao.rollback()
        print(f"Erro ao inserir agendamento: {e}")
    finally:
        conexao.close()

    return exito


def buscar_dados_usuario(email):
    conexao = conectardb()
    cur = conexao.cursor()
    dados_usuario = None
    exito = False

    try:
        sql = f"SELECT nome, idade, tipo_sanguineo, email FROM usuarios WHERE email = '{email}'"
        cur.execute(sql)
        dados_usuario = cur.fetchone()
        exito = True
    except psycopg2.Error as e:
        print(f"Erro ao buscar dados do usuário: {e}")
    finally:
        cur.close()
        conexao.close()

    if exito and dados_usuario:
        return dados_usuario
    else:
        return None



def buscar_agendamentos_usuario(email):
    conexao = conectardb()
    cur = conexao.cursor()
    historico = []
    exito = False

    try:
        sql = f"SELECT hemocentro, data, horario, observacao FROM agendamentos WHERE email = '{email}'"
        cur.execute(sql)
        historico = cur.fetchall()
        exito = True
    except psycopg2.Error as e:
        print(f"Erro ao buscar agendamentos: {e}")
    finally:
        cur.close()
        conexao.close()

    if exito:
        return historico
    else:
        return []
