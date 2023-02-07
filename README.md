# cnab
Desafio back-end

1 .Sobre o desafio

Ao receber um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Precisa-se criar uma maneira para que estes dados sejam importados para um banco de dados.

Tem-se a tarefa de criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

 2 .Techs

Visão Geral das tecnologias usadas no projeto.

Python
DJANGO
django rest_framework
djangorestframework-simplejwt
python-dotenv

3. Instalação e uso 
3.1 Requisitos

    Python a partir da versão 3.11.1 
    Gerenciador de pacotes pip 
    Banco de dados PostgreSQL

3.2 Instalação

3.2.1 - Crie um banco de dados no PostgreSQL 4.2.2 - Após o clone no repositório crie um ambiente de desenvolvimento:

python -m venv venv

3.2.3 - Após a criação do ambiente virtual voce terá que ativ-lo com o seguinte comando

para linux:

source/venv/bin/activate

para windows:

.\venv\Scripts\activate

3.2.4 - Crie um arquivo na raiz do projeto chamado .env e faça as configurações das variáveis de ambiente com base no .env.example do projeto

SECRET_KEY= chave secreta definida pelo seu time de desenvolvimento DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/vibe_database

3.2.5 - Agora que ja ativou o ambiênte de desenvolvimento voce terá que instalar as dependências do projeto

pip install -r requirements.txt

3.2.6 - Após instalar as dependências vamos persistir as migrations no banco de dados

python manage.py migrate

3.2.7 - Para rodar projeto utilize o comando

python manage.py runserver
