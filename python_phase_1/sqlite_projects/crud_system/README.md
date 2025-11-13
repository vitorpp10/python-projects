<h1 align="center">Mini-Crud-Employees — Phase 1</h1>

<p align="center">
A basic <b>CRUD (Create, Read, Update, Delete)</b> project built with Python and SQLite.<br>
It focuses on understanding backend logic, modular code design, and simple database operations in a CLI environment.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Editor-VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Phase-1-lightgrey?style=for-the-badge" />
</p>

---

## Project Overview

This is the **first phase** of a personal learning journey into Python backend development.  
It’s a simple terminal-based CRUD system for managing employees — great for beginners exploring data persistence and procedural programming.

---

## File Structure

### `main.py` — User Menu Interface

**Responsibilities:**
- Displays the menu for selecting CRUD operations  
- Validates and processes user input  
- Calls the corresponding database functions  

**Example Menu:**
=== Employee Management System ===

Add Employee

List Employees

Update Employee

Delete Employee

Exit

python
Copy code

---

### `database.py` — Database Layer

**Responsibilities:**
- Handles all SQLite operations  
- Contains logic for creating tables and performing CRUD actions  

**Key Functions:**
```python
def create_table():
    # Creates the employee table if it doesn't exist

def add_employee(name):
    # Inserts a new employee record

def list_employees():
    # Returns all stored employee records

def update_employee(id, new_name):
    # Updates the employee's name by ID

def delete_employee(id):
    # Deletes an employee by ID
🧠 Concepts Practiced
Procedural programming in Python

Modular project structure (UI and DB separated)

Basic SQL operations: INSERT, SELECT, UPDATE, DELETE

Data persistence using SQLite

Input validation and clean CLI interface

User interaction through terminal menus

💻 Demo (Terminal Simulation)
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
🚀 Future Improvements
Planned Feature	Status
Add error handling for duplicates / missing data	🔜
Implement export to CSV/JSON	🔜
Build a GUI version with Tkinter	🔜
Add bilingual documentation (EN/PT-BR)	🔜

🛠️ Tech Stack
Category	Tools / Concepts
Language	Python 3.x
Database Library	sqlite3 (built-in)
IDE	Visual Studio Code
Programming Paradigm	Procedural
Interface Language	English

🌐 Connect with Me
Platform	Link
LinkedIn	Vitor de Pádua
Email	vitorprofissionalpp10@gmail.com

🎯 Project Goal
This CRUD system marks Phase 1 of my Python learning path — focusing on database management, code organization, and CLI design.
It serves as a strong foundation for future projects involving APIs, GUIs, and web frameworks.

<p align="center"><i>“Small projects build great developer stories.”</i></p> <p align="center"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p> ```
