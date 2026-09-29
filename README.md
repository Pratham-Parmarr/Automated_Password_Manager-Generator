# Automated Password Manager & Generator (`Automated_Password_Manager-Generator`)

An automated CLI-based security application implemented in Python for generating strong passwords, evaluating their strength against standard criteria, and securing stored login credentials.
## Introduction

Managing secure, unique passwords is a huge pain for many people. The Automated Password Manager & Generator solves this problem by providing an easy-to-use CLI-based terminal for generating strong random passwords, assessing the strength of existing passwords, and storing secure passwords in an encrypted vault.
## Overview
The app offers users a variety of tools for dealing with the problem of keeping track of distinct and secure passwords for all of their different online accounts.
Some of the key features offered by the app are: a Master Password to secure the application, password generation, password strength evaluation, and encrypted storage facility.
To guarantee the security of the application, the user has to enter a Master Password every time they use the application. The generated passwords are also strong enough to withstand brute-force or dictionary attacks.

## Technologies and Tools

- Implementation language: Python 3.x
- Libraries: `random`, `string`
## How to Use
### Requirements

- Python 3+

### Installation
Install the requirements by cloning the repo:
```bash
git clone https://github.com/Pratham-Parmarr/Automated_Password_Manager-Generator
```
Then navigate to the cloned repo and run:
```bash
cd Automated_Password_Manager-Generator
```

For instructions on running the code, see below.

### Run
To run the code, simply do:
```bash
python main.py
```

Default master password: `boom boom`
### Testing
#### Testing the Master Password
- Run `python main.py`.
- In the terminal that appears, enter any password and ensure that the wrong password message shows.
- Then try the default master password `boom boom` and ensure that the menu appears.
#### Testing the Password Generator

- From the master password prompt, select the 1 option to generate a password.
- Set a length (e.g., 16), and set desired options to `y` or `n`. Ensure that the generated password meets the requirements we set.
#### Testing the Password Strength
- From the master password prompt, select the 2 option to check the strength of a test password.
- Try a few passwords with different strengths, for example, 'pass' should return weak, 'Pass1234' medium, and 'P@ssw0rd_2026!' strong.
#### Testing the Saving and Reading of Vault
- To test the saving facility: From the master password prompt, select 3 to save a credential. Set a site name, username and password. This should save to the `vault.txt` file.
- Check the `vault.txt` file to ensure that the password is masked correctly.
- From the master password prompt, select 4 to view the saved credentials. This will unmask the passwords and display them clearly.
### The Security Terminal
The following is the menu that users see when they are prompted to enter the master password.
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
