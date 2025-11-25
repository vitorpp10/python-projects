<h1 align="center"> LojaCLI — Profit Margin CLI Tool </h1> 
<p align="center"> 
A Python-based command-line tool designed to calculate profit margins and store transaction history using file persistence. 
  
Built with a focus on clean CLI UX, error handling, and foundational data persistence strategies. </p> 
  
<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Type-CLI-black?style=for-the-badge" /> <img src="https://img.shields.io/badge/Status-Active-yellow?style=for-the-badge" /> <img src="https://img.shields.io/badge/Focus-Profit%20Calculation-orange?style=for-the-badge" /> 
</p>

---

# Project Structure

- LojaCLI is a lightweight and efficient command-line application that automates the calculation of profit margins (Sale - Cost) while keeping a persistent record of all operations.

---

# The project demonstrates:

- Practical file manipulation in Python
- Error handling with try/except
- CLI user experience enhancements
- Modular and clean function-based design

---

# Features
1. Profit Margin Calculation
  - The user inputs the cost and sale values, and the system automatically calculates the resulting profit.

2. Transaction History Logging
  - Every successful calculation is saved in a .txt file, enabling long-term tracking and data review.

3. Custom UX Functions (CLI Effects)
  - LojaCLI includes custom functions that enhance the console experience:

| Function: | 
  > p()
  > i()
  > clear()
  > record_transaction()

| Purpose: |
  > Slow typing effect for messages
  > Slow typing input prompt
  > Clears the terminal screen
  > Saves operations to `.txt`

| Concepts Involved: |
  > UX, time.sleep()
  > UX, input handling
  > OS operations
  > File I/O

4. Robust Error Handling
  - The program prevents crashes by validating numeric input and handling invalid entries with clear feedback.

---

# How to Use

1. Run the main script:

```python loja_cli.py```


2. Follow the on-screen options to:
- Enter cost and sale values
- Calculate profit
- Automatically register the transaction
- View or edit transaction logs

3. A file named `transactions.txt` will be created/updated automatically.

---

# Technical Breakdown

**1. CLI/UX Core**
Although simple, the project introduces foundational UX patterns for terminal-based apps.

| Component: |
  > Typing effect
  > Input validation
  > File persistence


| Description: |
  > Creates a more interactive experience
  > Ensures clean numeric operations
  > Stores historical data reliably

---

# Roadmap (Next Steps)

| Upgrade |	Description |
|---|---|
| **Migrate to SQL Database** |	Replace `.txt` storage with SQLite or PostgreSQL. |
| **Web Interface (Flask)** |	Transform the CLI tool into a basic web dashboard. |
| **Modular Refactoring**|	Split code into `utils.py`, `database.py`, `cli.py`, etc.
| **Analytics Dashboard**	| Add profit charts and data visualization.


# Tech Stack

| Category | Skills |
|---|---|
| **Language** | Python 3.x |
| **Paradigm** | Procedural Programming |
| **Persistence** |	Text File (.txt) |
| **Libraries** |	`os`, `time` |
| **Topics** |	CLI UX, Exception Handling, File I/O |

---

## Connect

| Platform | Link |
|-----------|------|
| **LinkedIn** | [https://www.linkedin.com/in/vitor-de-padua/](https://www.linkedin.com/in/vitor-de-padua/) |
| **Email** | vitorprofissionalpp10@gmail.com |

---

## Goal

LojaCLI v0.5 is part of my ongoing journey toward becoming a more skilled Python developer — focusing on foundational concepts like data handling, automation, and UX for terminal applications.

Every iteration of this project moves it closer to a more complete and professional software solution.

---

<p align="center"><i>“Small progress is still progress.”</i></p> <p align="center"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p>
