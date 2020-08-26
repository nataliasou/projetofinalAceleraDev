<h1 align="center">🚧 Central de erros 🚧</h1>
<p align="center">Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

A arquitetura do projeto é formada por:

<h3><strong>Backend - API</strong><br></h3>
<ul>Criar endpoints para serem usados pelo frontend da aplicação</ul>
<ul>Criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional
a API deve ser segura, permitindo acesso apenas com um token de autenticação válido</ul></p>

<h4 align="center"> 
	✅  Central Erros - Concluido  ✅
</h4>

### Pré-requisitos

Para executar o projeto no seu computador, você vai precisar instalar as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/downloads/). 
Além disto, caso não tenha, instale um editor como [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)

### ⚙ Rodando o Back-End

```bash
# Clone este repositório
$ git clone <git@github.com:nataliasou/projetofinalAceleraDev.git>

# Abra o projeto no editor

# Instale o requirements.txt
virtualenv venv -p python3
venv\Scripts\activate.bat
pip install -r requirements.txt

# Migre o banco
py manage.py makemigrations
py manage.py migrate

# Execute o servidor
python3 manage.py runserver

# Acesse a aplicação
http://127.0.0.1:8000/

```