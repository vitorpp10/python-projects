<h1 align="center"> Python Projects — Phase 1</h1>

<p align="center">
  A collection of <b>Python mini-projects</b> built during my Computer Science learning journey.<br>
  From algorithms to small utilities — every line of code here represents progress. 
</p>

---

## About this Repository

This repository represents the **first phase** of learning in Python — documenting early projects and a transition toward **Object-Oriented Programming (OOP)**.  
The goal is to show **clear progression** in code organization, problem-solving, and structure.

It’s designed for:  
- A **minimal and readable UX**  
- **Quick setup** and execution  
- A **simple, scalable structure** as the repository grows  

---

## Tracks

### Basic Projects  
Short, foundational scripts to practice:  
- Logic and control flow  
- User input/output  
- Core data structures (lists, dictionaries, etc.)  

### OOP Projects  
Intermediate exercises to explore:  
- Classes and objects  
- Encapsulation and clean architecture  
- Reusability and scalability in design

### SQLites Projects
A practical, beginner-friendly command-line project to practice:
- Building a simple employee manager (CRUD: Create, Read, Update, Delete)
- Using Python with SQLite for persistent storage
- Implementing modular structure (separating UI/menu and data/database functions)
- Handling real-world data and safe user input in the terminal

---

## Structure

python-projects/
│
└── python-phase-1/
│
├── basic_projects/
│ ├── cpf_algorithm.py
│ ├── cpf_generator.py
│ ├── list_market.py
│ ├── list_market_2_0.py
│ └── mini_calculator.py
│
├── oop_projects/
│ └── bank_simulator_PT-BR/
│ ├── pycache/
│ ├── account.py
│ ├── bank.py
│ └── main.py
│
│
├── sqlite_projects/
│ └── crud_system_PT-BR/
│ ├── database.py
│ └── main.py
│
└── README.md

Projects are grouped by **difficulty level**, keeping navigation intuitive as the repository evolves.

---

## Getting Started

Run the projects easily using **Python 3.x** and a **virtual environment** for clean isolation and reproducibility.

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-projects.git
cd python-projects/python-phase-1

# Create virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# Create virtual environment (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate
Run a Project
bash

# Example: run a script from the basic_projects folder
python basic_projects/list_market_2_0.py
```

---

## Roadmap

**Next Steps**:

- Python + SQL: persistence, querying, and small CRUD apps connecting logic with real data
- Quality upgrades: unit tests, linting, and packaging for better structure and reliability
- CLI/UX polish: clearer messages, consistent flags, and friendly terminal error handling

**Learning Status**:

- Currently in continuous practice and exploration, actively improving through feedback and iteration.
- Phase 1 exists to demonstrate early progress, while building a foundation for more advanced, intermediate work.

---

## Tech Stack

| Category | Concepts / Tools |
|-----------|------------------|
| **Language** | Python 3.x |
| **Programming** | Procedural Programming, OOP, Data Structures, CLI I/O |
| **Environment** | Virtual env (venv) |
| **Planned** | pytest, pylint, SQL (SQLite/PostgreSQL), packaging |
