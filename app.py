from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
def index():
    return render_template('index.html')

def executa_insert(consultadb):
    con= conecta_db()
    cursor = con.cursor()
    cursor.execute(consultadb)
    con.commit() # Envia as variáveis para o db
    con.close() 
    
    dados = str("insert into public.contato(nome, telefone, email, senha) values('"+nome+","+email+","+senha+"')")
    executa_insert(dados)
  
def conecta_db():
  con = psycopg2.connect(host = 'localhost', database = 'dbbarbeiro', user = "postgres",  password= "postgres", port = 5432)
  return con
    
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
    
@app.route('/fazer-login', methods=['POST'])
def fazerLogin():
    user = request.form.get('email')
    senha = request.form.get('senha')
    
@app.route('/fazer-cadastro', methods=['POST'])
def fazercadastro():
    user = request.form.get('email')
    senha = request.form.get('senha')
    nome = request.form.get('nome')
    def executa_insert():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
