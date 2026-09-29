# Project Statement: Automated Password Manager & Generator

## 1. Problem Statement
In the modern digital environment, users manage numerous accounts across social, academic, and professional platforms. Due to cognitive overload, users frequently fall back on unsafe practices, such as reusing simple passwords across multiple platforms or keeping plain-text logs on their devices. These habits significantly increase susceptibility to cyber threats, credential stuffing, and unauthorized data access. 

Furthermore, many commercial password managers require cloud synchronization, paid subscriptions, or complex setup procedures, which can discourage non-technical or privacy-minded users who prefer simple, offline credential management.

## 2. Scope of the Project
The **Automated Password Manager & Generator** provides a lightweight, local, modular Python application focused on baseline credential lifecycle management.

### **In Scope:**
- Interactive Command-Line Interface (CLI) navigation.
- Master key access validation.
- Dynamic password synthesis based on user-defined constraints (length, upper/lower case, numbers, special characters).
- Deterministic password strength assessment algorithms.
- Local text file (`vault.txt`) data persistence using custom character masking logic.

### **Out of Scope:**
- Cloud databases, multi-device sync, and network socket communication.
- Graphical User Interfaces (GUI) or browser extensions.
- Advanced industrial encryption standards (e.g., AES-256 or bcrypt) beyond the scope of local demonstration masking.



## 3. Target Users
- **Students & Academics**: Seeking a clean, easy-to-use toolkit to organize account credentials locally.
- **Privacy Enthusiasts**: Users who prefer offline, lightweight software without third-party network connectivity.
- **Developers & Testers**: Individuals requiring quick generation of random test keys and mock credentials during software development.



## 4. High-Level Features

| Feature Module | Description |
| :--- | :--- |
| **Authentication Module** | Enforces master access verification before granting access to vault functions. |
| **Generator Engine** | Utilizes configurable character pools to generate unpredictable, high-entropy password strings. |
| **Strength Evaluator** | Grades passwords into discrete risk categories (**Weak**, **Medium**, **Strong**) based on length and character set composition. |
| **Obfuscation / Masking Engine** | Implements standard cipher masking on strings during write operations and reverses the transform upon read calls. |
| **Vault File Manager** | Reads and appends formatted record entries (`site,username,masked_password`) directly to local text storage. |

