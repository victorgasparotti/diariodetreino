from diario import app, conectar
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    conexao = conectar()
    lista = conexao.execute('SELECT * FROM treinos WHERE usuario_id = ? ORDER BY data DESC',(session['usuario_id'],)).fetchall()
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
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    exercicio=request.form['exercicio']
    series=int(request.form['series'])
    repeticoes=int(request.form['repeticoes'])
    peso=float(request.form['peso'])
    data=request.form['data']
    conexao = conectar()
    conexao.execute('INSERT INTO treinos (usuario_id, exercicio, series, repeticoes, peso, data) VALUES(?,?,?,?,?,?)',(session['usuario_id'],exercicio, series, repeticoes, peso, data))
    conexao.commit()
    conexao.close()
    return redirect(url_for('inicio'))
    
@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    conexao = conectar()
    treino = conexao.execute('SELECT * FROM treinos WHERE id = ? AND usuario_id = ?' , (id,session['usuario_id'])).fetchone()
    conexao.close()
    return render_template('editar.html', treino=treino)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    try:
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        exercicio=request.form['exercicio']
        series=int(request.form['series'])
        repeticoes=int(request.form['repeticoes'])
        peso=float(request.form['peso'])
        data=request.form['data']
        id = int(request.form['id'])
        if series >=1 and repeticoes >= 1 and peso >=0 and data.strip():
            conexao = conectar()
            conexao.execute('''
                UPDATE treinos
                SET exercicio = ?, series = ?, repeticoes = ?, peso = ?, data = ?
                WHERE id = ?
            ''',(exercicio,series,repeticoes,peso,data,id))
            conexao.commit()
            conexao.close()
            return redirect(url_for('inicio'))
        else:
            flash('Dados inválidos')
            conexao = conectar()
            treino = conexao.execute('SELECT * FROM treinos WHERE id = ?',(id,)).fetchone()
            conexao.close()
            return render_template('editar.html', treino=treino)
    except ValueError:
        flash('Erro! Digite números válidos')
        conexao = conectar()
        treino = conexao.execute('SELECT * FROM treinos WHERE id = ? AND usuario_id = ?', (id,session['usuario_id'])).fetchone()
        conexao.close()
        return render_template('editar.html', treino=treino)
        
@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    conexao = conectar()
    conexao.execute('DELETE FROM treinos WHERE id = ? AND usuario_id = ?' , (id,session['usuario_id']))
    conexao.commit()
    conexao.close()
    return redirect(url_for('inicio'))

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method=='POST':
        nome_usuario=request.form['nome_usuario']
        senha=request.form['senha']
        hashed_password=generate_password_hash(senha)
        conexao = conectar()
        conexao.execute('INSERT INTO usuarios (nome_usuario,senha) VALUES(?,?)',(nome_usuario,hashed_password))
        conexao.commit()
        conexao.close()
        return redirect(url_for('inicio'))
    elif request.method=='GET':
        return render_template('cadastro.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        nome_usuario = request.form['nome_usuario']
        senha=request.form['senha']
    conexao = conectar()
    usuario = conexao.execute('SELECT * FROM usuarios WHERE nome_usuario = ?',(nome_usuario,)).fetchone()
    conexao.close()
    if usuario:
        if check_password_hash(usuario['senha'],senha):
            session['usuario_id'] = usuario['id']
            return redirect(url_for('inicio'))
        else:
            flash('Usuário ou senha inválidos')
            return render_template('login.html')
    else:
        flash('Usuário ou senha inválidos')
        return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_id', None)
    flash('Logout feito com sucesso')
    return redirect(url_for('inicio'))


