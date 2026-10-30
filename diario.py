from flask import Flask, render_template, request, redirect, url_for
from models import Treino
import sqlite3

app = Flask(__name__)


def conectar():
    conexao=sqlite3.connect('meu_banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

lista=[]
treino1 = Treino(1,'Supino reto', 3, 10, 40, '2026-10-25')
treino2 = Treino(2,'Supino inclinado', 3, 10, 90, '2026-10-29')
treino3 = Treino(3, 'Crucifixo', 2, 10, 70, '2026-10-25')
lista.append(treino1)
lista.append(treino2)
lista.append(treino3)


@app.route('/')
def inicio():
    conexao = conectar()
    lista = conexao.execute('SELECT * FROM treinos ORDER BY data DESC').fetchall()
    dias = {}
    for i in lista:
        if i['data'] not in dias:
            dias[i['data']]=[]
        dias[i['data']].append(i)
    conexao.close()
    return render_template('lista.html', titulo='Diario de treino', dias=dias )

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/criar', methods=['POST'])
def criar():
    exercicio=request.form['exercicio']
    series=int(request.form['series'])
    repeticoes=int(request.form['repeticoes'])
    peso=float(request.form['peso'])
    data=request.form['data']
    conexao = conectar()
    conexao.execute('INSERT INTO treinos (exercicio, series, repeticoes, peso, data) VALUES(?,?,?,?,?)',(exercicio, series, repeticoes, peso, data))
    conexao.commit()
    conexao.close()
    return redirect(url_for('inicio'))
    
@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    conexao = conectar()
    treino = conexao.execute('SELECT * FROM treinos WHERE id = ?',(id,)).fetchall()
    conexao.close()
    return render_template('editar.html', treino=treino)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    return redirect(url_for('inicio'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    conexao = conectar()
    conexao.execute('DELETE FROM treinos WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)

