<h1 align="center"> Python Projects — Phase 1</h1>

<p align="center">
  A collection of <b>Python mini-projects</b> built during my Computer Science learning journey.<br>
  From algorithms to small utilities — every line of code here represents progress. 
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Editor-VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Phase-1-lightgrey?style=for-the-badge" />
</p>

---

### 1. `account.py` — Account 
Implements the `ContaBancaria` class, representing individual bank accounts.

**Responsibilities:**

- Store account holder and balance
- Allow deposits and withdrawals with balance checks

Example method:
```python
def sacar(self, valor):
    if valor > self._saldo:
        print(f"Saldo insuficiente. Saldo atual: R${self._saldo:.2f}")
    else:
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
``````

---

### 2. `bank.py` — Bank Management
Implements the Banco class — the “manager” that connects users and accounts.

Responsibilities:

Create new accounts
Prevent duplicate accounts
Find existing accounts by holder name

Example method:

```python
Copy code
def abrir_conta(self, titular, saldo_inicial=0):
    if self.buscar_conta(titular):
        print(f"ERRO: {titular} já possui uma conta neste banco.")
        return None
    nova_conta = ContaBancaria(titular, saldo_inicial)
    self.contas.append(nova_conta)
    return nova_conta
```

---

### 3. `main.py` — User Interface (CLI)
The entry point of the system. It connects everything through an interactive, text-based interface.

Features:

Account creation flow
Menu navigation with deposit, withdrawal, and balance options
Smooth text animations for a better UX
Cross-platform screen clearing

Example Menu:

```plaintext
Copy code
--- Menu Principal | Banco Digital Dev ---
1. Depositar
2. Sacar
3. Ver Saldo
4. Sair
```
---

## Concepts Practiced

- Concept Description
- Classes & Objects	-> Models entities: bank and accounts
- Encapsulation -> Protects balance variable _saldo
- Composition -> Banco manages multiple ContaBancaria objects
- Error Handling -> Prevents invalid input or operations
- UX Design (CLI) -> Realistic text delays, feedback, and flow

---

## Demo (Terminal Simulation)

Example of how the user interacts with the Bank Simulator through the command line:

```bash
Copy code
$ python main.py

------------------------------
Bem-vindo! Vamos criar sua conta para começar.

Digite seu nome completo: João Silva
Digite seu depósito inicial (ex: 100.50): 250.00
Conta criada, acessando seu menu...

--- Menu Principal | Banco Digital Dev ---
Olá, João Silva!

O que deseja fazer?
  1. Depositar
  2. Sacar
  3. Ver Saldo
  4. Sair

Digite sua opção (1-4): 1
Digite o valor para depósito: 100.00
Processando depósito...
Depósito de R$100.00 realizado.
Saldo atual de João Silva igual a R$350.00.

Pressione ENTER para voltar ao menu...

--- Menu Principal | Banco Digital Dev ---
Olá, João Silva!

O que deseja fazer?
  1. Depositar
  2. Sacar
  3. Ver Saldo
  4. Sair

Digite sua opção (1-4): 2
Digite o valor para saque: 50.00
Verificando fundos e processando saque...
Saque de R$50.00 realizado com sucesso.
Saldo atual de João Silva igual a R$300.00.

Pressione ENTER para voltar ao menu...
```
---

## Future Improvements

| Add persistent storage (SQLite or JSON) |​
| Implement account authentication (username/password)​ |
| Introduce transaction history with timestamps​ |
| Add multi-user session support​ |
| Create a GUI version with tkinter or customtkinter ​| 

## Tech Stack

| Category | Tools / Concepts |
|---|---|
| **Language** | Python 3.x |
| **Paradigm** | Object-Oriented Programming |
| **IDE** | Visual Studio Code |
| **Libraries** | `os`, `time` |
| **Language** | PT-BR |
| **Topics** | Encapsulation, CLI UX, Composition, Modular Design |

## Connect

| Platform | Link |
|-----------|------|
| **LinkedIn** | [https://www.linkedin.com/in/vitor-de-padua/](https://www.linkedin.com/in/vitor-de-padua/) |
| **Email** | vitorprofissionalpp10@gmail.com |
| **beecrowd Profile** | [https://judge.beecrowd.com/en/profile/1188964](https://judge.beecrowd.com/en/profile/1188964) |

---

## Goal

These mini-projects represent my **Phase 1 of learning Python** — a stage focused on logic, algorithms, and real-world problem-solving.  
Each one is a step toward becoming a **proficient and creative Python developer**.

---

<p align="center"><i>“Every small project builds a big foundation.”</i></p>

---

<p align="center" width="100%"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p>
