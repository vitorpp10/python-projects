<h1 align="center"> Mini-Crud-Employees — Phase 1 </h1>

<p align="center">
  A basic <b>CRUD (Create, Read, Update, Delete)</b> project built with Python and SQLite.<br>
  Focused on understanding backend logic, modular structure, and database interaction in a CLI environment.
</p>

---

### 1. `main.py` — User Menu Interface
Acts as the **entry point** of the system. Displays the CRUD options and connects user actions to database functions.

**Responsibilities:**

- Display the main menu  
- Handle and validate user input  
- Call the corresponding database operation  

Example menu:

```plaintext
def menu():
    print("\n=== Sistema de Funcionários ===")
    print("1. Adicionar funcionário")
    print("2. Listar funcionários")
    print("3. Atualizar funcionário")
    print("4. Excluir funcionário")
    print("5. Sair")
    return input("Escolha uma opção: ")
```
---

*Handles all database interactions using Python’s built-in sqlite3 library.*
*Encapsulates SQL logic in simple functions to maintain clean code separation.*

**Responsibilities:**

- Create database and tables (if not existing)
- Insert, retrieve, update, and delete employee data
- Return query results for the CLI interface

Example methods:

```python
def criar_tabela():
def adicionar_funcionario(nome):
def listar_funcionarios():
def atualizar_funcionario(id, novo_nome):
def excluir_funcionario(id):
```

---

## Concepts Practiced

- Concept Description
- Procedural Programming -> Structuring code through functions and modules
- SQLite Integration -> Performing CRUD operations using SQL commands
- Modular Design -> Separating UI (menu) and data logic (database)
- Data Persistence -> Storing and retrieving data locally via SQLite
- Input Validation -> Ensuring user entries are handled safely
- CLI UX -> Building an intuitive text-based interface

---

## Demo (Terminal Simulation)

Example of how the CRUD system behaves in the terminal:

```bash
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
```

---

## Future Improvements

|​ Planned Feature	Status |​ 
|​ Add error handling for duplicates or invalid input 🔜 |​
|​ Implement export to CSV/JSON 🔜 |​
|​ Create GUI version with Tkinter 🔜 |​
|​ Add bilingual documentation (EN/PT-BR) 🔜 |​ 

## Tech Stack

| Category | Tools / Concepts |
|---|---|
| **Language** | Python 3.x |
| **Database** | SQLite (built-in sqlite3 library) |
| **Paradigm** | Procedural Programming |
| **IDE** | Visual Studio Code |
| **Language** | PT-BR |
| **Topics** | SQL Basics, CLI UX, Modularization, Data Persistence |

## Connect

| Platform | Link |
|-----------|------|
| **LinkedIn** | [https://www.linkedin.com/in/vitor-de-padua/](https://www.linkedin.com/in/vitor-de-padua/) |
| **Email** | vitorprofissionalpp10@gmail.com |

---

## Goal

This mini project represents Phase 1 of my Python learning journey — focused on logic, database handling, and system structure at the command-line level.
It serves as a foundation for future studies involving APIs, GUIs, and web development.
