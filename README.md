# Diário de Treino

Aplicação web para registrar e organizar treinos. Cada usuário pode criar uma conta e manter seus próprios registros de exercícios.

## Acessar o projeto

[Diário de Treino](https://diariodetreino-eaqf.onrender.com/login)

## Funcionalidades

- Cadastro de usuário e login
- Senhas armazenadas com hash
- Criação, edição e exclusão de treinos
- Organização dos registros por data
- Treinos separados por usuário
- Registro de exercício, séries, repetições, peso e data

## Tecnologias

- Python
- Flask
- SQLite
- HTML
- CSS

## Executar localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/victorgasparotti/diariodetreino.git
   cd diariodetreino
2. Crie e ative um ambiente virtual:
   python -m venv venv
   No Windows:
   venv\Scripts\activate
   No macOS ou Linux:
   source venv/bin/activate
3. Instale as dependências:
   pip install -r requirements.txt
4. Crie um arquivo .env na pasta principal do projeto e adicione uma chave secreta:
   SECRET_KEY=coloque-um-valor-secreto-aqui
5. Inicie a aplicação:
   python diario.py
6. Abra http://127.0.0.1:5000 no navegador.
O banco SQLite é criado pelo db.py, importado durante a inicialização da aplicação.
Hospedagem
O projeto está hospedado no Render. O comando de inicialização é:
gunicorn diario:app
Configure SECRET_KEY nas variáveis de ambiente do serviço de hospedagem. Não publique nem compartilhe o valor dessa chave.
Autor
Victor Gasparotti
