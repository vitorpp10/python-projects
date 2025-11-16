<h1 align="center"> Tax Calculator Simulator (Polymorphism Study) </h1>
<p align="center">   
A mini-project in Python focused on the practical application of Polymorphism and Abstraction (SOLID principles).

It simulates a product registration system that calculates taxes differently for each category. </p>

<p align="center">   
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />   <img src="https://img.shields.io/badge/Paradigm-OOP-purple?style=for-the-badge" />   
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />   <img src="https://img.shields.io/badge/Focus-Polymorphism-orange?style=for-the-badge" /> 
</p>

---

## Project Structure

- The code is a single-file application that models the relationship between an abstract product class and its concrete subclasses.

---

**1. Abstract and Polymorphic Classes (OOP Core)**

- Defines the business logic for taxes, demonstrating how different classes can respond to the same method call.-

| Class | Type | Responsibility |
|---|---|
| `Produto(ABC)` | Abstract | Defines the core structure (`nome`, `preco`) |
| `ProdutoEletronico` | Subclass | Implements `calcular_imposto()` with a 15% tax rate. |
| `ProdutoAlimenticio` | Subclass | Implements `calcular_imposto()` with a 5% tax rate. |

Polymorphism Example:
```python
def processar_imposto(produto: Produto):
    tax = produto.calcular_imposto()
```

---

**2. Interactive Functions (CLI/UX)**

- The rest of the code focuses on the interactive interface, using delays and colors to enhance the user experience (UX) in the console.

| Function | Purpose | Concepts Applied |
|---|---|
| **main()** | The main loop for menu navigation. | `while True`, `if, else` |
| **criar_produto()** | Data collection with input validation | Object Creation, Exception.. |
| **p(), clear(), p_input()** | Implements the slow typing effect | UX/CLI, `time` |
| **Cores** | Subclass | Constants, UX/CLI Design. | 

---

## Applied OOP and SOLID Concepts

- **Polymorphism** -> The ability of derived classes (`Eletronico`, `Alimenticio`) to respond differently to the same method call (`calcular_imposto`).

- **Abstraction** -> Using the **abstract** class `Produto` and the `@abstractmethod` decorator to enforce a required contract for all subclasses.

- **Liskov Substitution Principle (SOLID)** -> Any function expecting a `Produto` object can seamlessly use its subclasses (`ProdutoEletronico` or `ProdutoAlimenticio`) without breaking functionality.

- **Exception Handling** -> Using `try...except` blocks to handle non-numeric price inputs, ensuring program robustness.

---

## Future Improvements

| **Custom Exceptions**: Implement a custom error class (e.g., `class NegativePriceError(Exception):` ) instead of relying solely on built-in exceptions. |​
| **Persistence**: Save the list of products to a JSON or CSV file so data isn't lost upon closing the program.​ |
| **Refactoring**: Separate the code into multiple files (`model.py`, `cli.py`, `utils.py`) for better modularity.​ |

## Tech Stack

| Category | Tools / Concepts |
|---|---|
| **Language** | Python 3.x |
| **Paradigm** | Object-Oriented Programming |
| **IDE** | Visual Studio Code |
| **Libraries** | `abc`, `os`, `time` |
| **Language** | PT-BR |
| **Topics** | Abstraction, Polymorphism, CLI UX, Exception Handling. |

## Connect

| Platform | Link |
|-----------|------|
| **LinkedIn** | [https://www.linkedin.com/in/vitor-de-padua/](https://www.linkedin.com/in/vitor-de-padua/) |
| **Email** | vitorprofissionalpp10@gmail.com |

---

## Goal

These mini-projects represent my **Phase 1 of learning Python** — a stage focused on logic, algorithms, and real-world problem-solving.  
Each one is a step toward becoming a **proficient and creative Python developer**.

---

<p align="center"><i>“Small progress is still progress.”</i></p>

---

<p align="center" width="100%"> <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" /> </p>
