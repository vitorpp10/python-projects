<h1 align="center"> mini-crud-employees — Phase 1 </h1>

<p align="center">
  A basic <b>CRUD (Create, Read, Update, Delete)</b> project built with Python and SQLite.<br>
  Focused on understanding backend logic, modular structure, and database interaction in a CLI environment.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Editor-VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Phase-1-lightgrey?style=for-the-badge" />
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
=== Employee Management System ===
1. Add Employee
2. List Employees
3. Update Employee
4. Delete Employee
5. Exit
2. database.py — Database Layer
Handles all database interactions using Python’s built-in sqlite3 library.
Encapsulates SQL logic in simple functions to maintain clean code separation.

Responsibilities:

Create database and tables (if not existing)

Insert, retrieve, update, and delete employee data

Return query results for the CLI interface

Example methods:

python
Copy code
def create_table():
    # Creates the employee table if it doesn't exist

def add_employee(name):
    # Inserts a new employee into the database

def list_employees():
    # Returns all registered employees

def update_employee(id, new_name):
    # Updates an employee's name based on their ID

def delete_employee(id):
    # Deletes an employee record by ID
Concepts Practiced
Concept	Description
Procedural Programming	Structuring code through functions and modules
SQLite Integration	Performing CRUD operations using SQL commands
Modular Design	Separating UI (menu) and data logic (database)
Data Persistence	Storing and retrieving data locally via SQLite
Input Validation	Ensuring user entries are handled safely
CLI UX	Building an intuitive text-based interface

Demo (Terminal Simulation)
Example of how the CRUD system behaves in the terminal:

bash
Copy code
$ python main.py

=== Employee Management System ===
1. Add Employee
2. List Employees
3. Update Employee
4. Delete Employee
5. Exit

Choose an option: 1
Employee name: Amanda
Employee added successfully!

Choose an option: 2
--- Registered Employees ---
ID: 1 | Name: Amanda

Choose an option: 3
Employee ID to update: 1
New name: Ana
Employee updated successfully!

Choose an option: 4
Employee ID to delete: 1
Employee deleted successfully!

Choose an option: 5
Exiting...
Future Improvements
Planned Feature	Status
Add error handling for duplicates or invalid input	🔜
Implement export to CSV/JSON	🔜
Create GUI version with Tkinter	🔜
Add bilingual documentation (EN/PT-BR)	🔜

Tech Stack
Category	Tools / Concepts
Language	Python 3.x
Database	SQLite (built-in sqlite3 library)
Paradigm	Procedural Programming
IDE	Visual Studio Code
Language	English
Topics	SQL Basics, CLI UX, Modularization, Data Persistence

Connect
Platform	Link
LinkedIn	https://www.linkedin.com/in/vitor-de-padua/
Email	vitorprofissionalpp10@gmail.com

Goal
This mini project represents Phase 1 of my Python learning journey — focused on logic, database handling, and system structure at the command-line level.
It serves as a foundation for future studies involving APIs, GUIs, and web development.

<p align="center"><i>“Small projects build great developer stories.”</i></p>
<p align="center" width="100%"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p> ```
