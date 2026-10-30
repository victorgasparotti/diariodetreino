from flask import Flask, render_template, request, redirect, url_for
from models import Treino

app = Flask(__name__)


lista=[]
treino1 = Treino(1,'Supino reto', 3, 10, '2026-10-25')
treino2 = Treino(2,'Supino inclinado', 3, 10, '2026-10-29')
treino3 = Treino(3, 'Crucifixo', 2, 10, '2026-10-25')
lista.append(treino1)
lista.append(treino2)
lista.append(treino3)


@app.route('/')
def inicio():
    treinos_organizados = sorted(lista, key=lambda t: t.data, reverse=True)
    return render_template('lista.html', titulo='Diario de treino', treinos=treinos_organizados )

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/criar', methods=['POST'])
def criar():
    ids=[a.id for a in lista]
    maior_id = max(ids, default=0)
    novo_id = maior_id+1
    
    exercicio=request.form['exercicio']
    series=int(request.form['series'])
    repeticoes=int(request.form['repeticoes'])
    data=request.form['data']

    treino10 = Treino(novo_id,exercicio,series,repeticoes,data )
    lista.append(treino10)
    return redirect(url_for('inicio'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    for i in lista:
        if i.id == id:
            lista.remove(i)
            break
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)

