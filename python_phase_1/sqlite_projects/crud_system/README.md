<h1 align="center">mini-crud-funcionarios — Phase 1</h1> <p align="center"> Basic <b>CRUD (Create, Read, Update, Delete)</b> project in Python using SQLite.<br> Practical exploration of backend logic and database access — from code structure to database management. </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Editor-VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode" /> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Phase-1-lightgrey?style=for-the-badge" /> </p>
1. main.py — User Menu Interface
Responsibilities:

Presents the user with a menu to choose one of the four CRUD operations.

Handles and validates user input.

Calls the correct database functions.

Example menu:

text
=== Sistema de Funcionários ===
1. Adicionar funcionário
2. Listar funcionários
3. Atualizar funcionário
4. Excluir funcionário
5. Sair
2. database.py — Database Layer
Responsibilities:

Handles all database commands using SQLite (included with Python).

Separates logic for creating the table, adding, listing, updating, and deleting records.

Key functions:

python
def criar_tabela():
    # Cria a tabela de funcionários se não existir
def adicionar_funcionario(nome):
    # Insere um novo funcionário
def listar_funcionarios():
    # Retorna todos os registros cadastrados
def atualizar_funcionario(id, novo_nome):
    # Altera o nome de um funcionário pelo id
def excluir_funcionario(id):
    # Remove um funcionário pelo id
Concepts Practiced
Procedural programming in Python

Modular file structure (separating menu and DB logic)

Introduction to SQL commands (INSERT, SELECT, UPDATE, DELETE)

Data persistence with SQLite

Input validation and clear terminal UI

CLI menu interaction

Demo (Terminal Simulation)
bash
$ python main.py

=== Sistema de Funcionários ===
1. Adicionar funcionário
2. Listar funcionários
3. Atualizar funcionário
4. Excluir funcionário
5. Sair
Escolha uma opção: 1
Nome do funcionário: Amanda
Funcionário adicionado!

# ...

Escolha uma opção: 2
--- Funcionários Cadastrados ---
ID: 1 | Nome: Amanda

Escolha uma opção: 3
ID do funcionário a atualizar: 1
Novo nome: Ana
Funcionário atualizado!

Escolha uma opção: 4
ID do funcionário a excluir: 1
Funcionário excluído!

Escolha uma opção: 5
Saindo...
Future Improvements
Planned Feature	Status
Add error handling for duplicates / missing data	🔜
Implement export to CSV/JSON	🔜
GUI version with Tkinter	🔜
Documentation in EN/PT-BR	🔜
Tech Stack
Category	Tools / Concepts
Language	Python 3.x
Library	sqlite3 (built-in)
IDE	Visual Studio Code
Paradigm	Procedural
Language	PT-BR
Connect
Platform	Link
LinkedIn	https://www.linkedin.com/in/vitor-de-padua/
Email	vitorprofissionalpp10@gmail.com
Goal
This CRUD project is a foundational step in my Python journey (Phase 1), putting into practice database handling, separation of concerns, and UI logic at the CLI level. Ideal for students and beginners as a base for future learning in more complex systems.

<p align="center"><i>“Pequenos projetos constroem grandes histórias dev.”</i></p>
<p align="center" width="100%"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p>
