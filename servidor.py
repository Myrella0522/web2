#importando o flask
from flask import *
import dao

#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('home.html')

@app.route('/agendamento', methods=['POST'])
def agendar():
    email = request.form.get()



#iniciando/rodando o servidor
app.run(debug=True)