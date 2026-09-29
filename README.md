# Automated Password Manager & Generator (`Automated_Password_Manager-Generator`)

A modular, CLI-based security application built with Python that enables users to generate highly secure passwords, evaluate password strength against key criteria, and safely store/retrieve encrypted login credentials locally.

## Overview

Managing secure, distinct passwords across multiple online accounts is a significant challenge. The **Automated Password Manager & Generator** solves this issue by offering a lightweight, offline, command-line interface (CLI) terminal. Users can create randomized, complex passwords customized to specific criteria, evaluate existing passwords for security vulnerabilities, and persist credential records in an obfuscated local vault protected by master authentication.

## Features

- **Master Password Authentication**: Secures application entry to prevent unauthorized local access.
- **Customizable Password Generation**: Generates strong passwords tailored by length and inclusion of uppercase letters, numbers, and special characters.
- **Password Strength Evaluator**: Analyzes passwords and categorizes them into **Weak**, **Medium**, or **Strong** tiers based on length and character variance.
- **Obfuscated Credential Storage**: Masks sensitive passwords using character-shift algorithms before persisting them to disk.
- **Vault Viewer**: Reads, unmasks, and neatly formats saved website credentials on demand.

## Technologies & Tools Used

- **Programming Language**: Python 3.x
- **Standard Libraries**:
  - `random`: Pseudo-random selection for secure key character assembly.
  - `string`: Character set sets (`ascii_lowercase`, `ascii_uppercase`, `digits`, `punctuation`).

## Steps to Install & Run

### Prerequisites
- Python 3.x installed on your computer.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pratham-Parmarr/Automated_Password_Manager-Generator
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Automated_Password_Manager-Generator
   ```

### Execution
Run the main script to start the interactive security terminal:
```bash
python main.py
```
> **Default Master Password**: `boom boom`

## Instructions for Testing

1. **Test Master Authentication**:
   - Run `python main.py`.
   - Enter an incorrect master password to verify access denial.
   - Enter `boom boom` to verify access granted.

2. **Test Password Generation (Option 1)**:
   - Select option `1`.
   - Set length (e.g., `16`) and toggle options (`y/n`). Verify that the output string matches the requested constraints.

3. **Test Password Strength Evaluator (Option 2)**:
   - Select option `2`.
   - Test short passwords (e.g., `pass`) -> Expect `Weak`.
   - Test medium passwords (e.g., `Pass1234`) -> Expect `Medium`.
   - Test complex passwords (e.g., `P@ssw0rd_2026!`) -> Expect `Strong`.

4. **Test Vault Management (Options 3 & 4)**:
   - Select option `3` to save a credential (`site.com`, `user1`, `Secret123`).
   - Check `vault.txt` directly to confirm the password is saved in a masked state.
   - Select option `4` in the CLI menu to confirm credentials are properly unmasked when displayed.

### Main Security Terminal Menu
```text
=== SECURITY TERMINAL ===
Enter Master Password to unlock: boom boom
Access Granted!

--- MENU ---
1. Generate Password
2. Check Password Strength
3. Save Credential to Vault
4. View Saved Credentials
5. Exit
```

---
