# 🧮 Simple Python Calculator

> A simple command-line calculator built with **Python** that performs common arithmetic operations with input validation, error handling, reset functionality, and program termination controls.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/Interface-CLI-111111?style=for-the-badge\&logo=gnubash\&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

---

## 📖 About The Project

**Simple Python Calculator** is a command-line application developed using Python to perform basic mathematical calculations.

The project was created to practice fundamental Python programming concepts such as **conditional statements, loops, functions, user input, arithmetic operators, and exception handling**.

The calculator provides a simple interactive experience where users can select an operation, enter two numbers, view the result, reset the calculator, or terminate the program.

---

## ✨ Features

### ➕ Basic Arithmetic

Supports the following mathematical operations:

| Operator | Operation      |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `^`      | Power          |
| `%`      | Remainder      |

### 🔄 Reset Calculator

Use:

```text
$
```

to reset the calculator and start a new calculation.

### ❌ Terminate Program

Use:

```text
#
```

to terminate the application.

### 🛡️ Error Handling

The program handles:

* Invalid operation selections
* Invalid numeric input
* Division by zero
* Incorrect user input

### 🖥️ Interactive CLI

The calculator provides clear instructions and feedback directly through the terminal.

---

## ⚙️ How It Works

```text
             ┌──────────────────┐
             │      Start       │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  Select Operation│
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Enter Two Numbers│
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Perform Operation│
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Display Result   │
             └────────┬─────────┘
                      │
                ┌─────┴─────┐
                │           │
              Reset       Exit
                │           │
                ▼           ▼
             Continue      End
```

---

## 🛠️ Technologies & Concepts

| Technology / Concept       | Usage                             |
| -------------------------- | --------------------------------- |
| 🐍 Python 3.x              | Core programming language         |
| 🔢 Arithmetic Operators    | Mathematical calculations         |
| 🔀 Conditional Statements  | Operation selection               |
| 🔁 Loops                   | Continuous calculator interaction |
| 🧩 Functions               | Organizing calculator operations  |
| 🛡️ Exception Handling     | Managing invalid input and errors |
| 🖥️ Command-Line Interface | User interaction                  |

---

## 📁 Project Structure

```text
Simple-Python-Calculator/
│
├── 🐍 calculator.py
└── 📄 README.md
```

### `calculator.py`

Contains the complete calculator implementation, including:

* Arithmetic operations
* User input handling
* Error handling
* Reset functionality
* Program termination

---

## 🚀 Getting Started

### Prerequisites

Make sure **Python 3.x** is installed on your computer.

Check your Python version:

```bash
python --version
```

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/K-Chethika/Simple-Python-Calculator.git
```

### 2️⃣ Navigate to the Project

```bash
cd Simple-Python-Calculator
```

### 3️⃣ Run the Calculator

```bash
python calculator.py
```

---

## 💻 Example

```text
================================
      SIMPLE PYTHON CALCULATOR
================================

Select an operation:

+  Addition
-  Subtraction
*  Multiplication
/  Division
^  Power
%  Remainder

Enter operation: +
Enter first number: 25
Enter second number: 15

Result: 40
```

### Reset

```text
Enter operation: $

Calculator reset successfully.
```

### Exit

```text
Enter operation: #

Program terminated.
```

---

## 🧠 Key Learning Outcomes

This project helped strengthen my understanding of:

* Python fundamentals
* Functions and program structure
* Conditional logic
* Loops and repetition
* Arithmetic operations
* User input handling
* Exception handling
* Building interactive CLI applications
* Writing simple and maintainable Python programs

---

## 📌 Project Highlights

```text
✔ Python CLI Application
✔ Basic Arithmetic Operations
✔ Power & Remainder Operations
✔ Input Validation
✔ Error Handling
✔ Division-by-Zero Handling
✔ Reset Functionality
✔ Program Termination
✔ Interactive User Interface
```

---

## 👩‍💻 Author

### Kavindi Chethika

**Software Engineering Undergraduate | Aspiring AI Engineer**

**GitHub:** [K-Chethika](https://github.com/K-Chethika)

**LinkedIn:** [Kavindi Chethika](https://www.linkedin.com/in/kavindi-chethika/)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

## 📄 License

This project is created for educational and portfolio purposes.
