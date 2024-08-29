from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados SQLite
DATABASE = 'agenda.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial: Lista todos os contatos
@app.route('/')
def index():
    conn = get_db_connection()
    contatos = conn.execute('SELECT * FROM pessoa').fetchall()
    conn.close()
    return render_template('index.html', contatos=contatos)

# Adicionar novo contato
@app.route('/add', methods=('GET', 'POST'))
def add_contact():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO pessoa (nome, telefone, email) VALUES (?, ?, ?)', 
                     (nome, telefone, email))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_contact2.html')

# Editar um contato existente
@app.route('/edit/<int:idpessoa>', methods=('GET', 'POST'))
def edit_contact(idpessoa):
    conn = get_db_connection()
    contato = conn.execute('SELECT * FROM pessoa WHERE idpessoa = ?', (idpessoa,)).fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']

        conn.execute('UPDATE pessoa SET nome = ?, telefone = ?, email = ? WHERE idpessoa = ?', 
                     (nome, telefone, email, idpessoa))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit_contact2.html', contato=contato)

# Deletar contato
@app.route('/delete/<int:idpessoa>')
def delete_contact(idpessoa):
    conn = get_db_connection()
    conn.execute('DELETE FROM pessoa WHERE idpessoa = ?', (idpessoa,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
