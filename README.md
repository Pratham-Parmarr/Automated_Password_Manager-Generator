# CLI Password Generator and Vault Terminal

A Modular Command Line Application for Generating Strong Passwords, Assessing Their Strength and for Other Basic Local Storage of Credentials with Obfuscation Masking written in Python.

## Overview

CLI Password Generator and Vault Terminal - A compact CLI utility written in Python that gives you an all-in-one terminal-based solution to generate highly customizable secure passwords, check password strength according to standard rules, and store an encrypted local credential vault, vault.txt, with a master password panel.

## Features

* Master Security Terminal: Helps lock down applications behind a Master Password screen.

* Advanced Password Generator: Creates secure auto-generated passwords that can be customized with specific length and inclusion of (1) lowercase, (2) uppercase, (3) number and (4) special characters.

• • Password Strength Checker: Produces a score and classifies the password as Weak, Medium or Strong according to its length and whether variations of characters are used.

* Data Obfuscation & Masking: Applies custom character masking before credentials are written to disk.

• Credential vault saving: Users can save the site name, username, password (encrypted), decrypt passwords, and save information on the saved site name, username, and password.

## Technologies / Tools Used

* Language: Python 3.x

* Standard Libraries:

* random (for character picking in a non-deterministic fashion when generating passwords)

* string (for character set manipulations and string checks)

 Storage: Generic scripts Storage of data Outer shell "inner shell"? Notes (general) Vault+ is a simple and flexible secure database with several interesting features: mVault is a simple, hierarchical, flat file; the system uses the code page, not a character shift to encrypt the files (which are plain text files).

Procedure To Install & Run The Program Read on How To Run the Program ## Procedure To Install & Run The Program Read on How To Run the Program Read on How To Run the Program. Read on How To Run the Program.

# Prerequisites

* Python 3.x installed on your system.

## Running the Application

1. Clone or Download the Repository:

``

git clone https://github.com/Pratham-Parmarr/desktop-tutorial

cd <>

`

2. Run the Application:

Execute the main.py entry point:

`

python main.py

`

3. Log In:

* Enter the master password: admin









## Instructions for Testing

1. Test Password Generation:

* Choose option 1 in terminal menu.

* Input Length, for example 16 Enable/disable characters, for example y/n.

*Ensure that the output adheres to the chosen specifications.

2. Test Strength Evaluation:

* Select option 2.

* Try a very short password (e.g. Abc12) -> should return Weak.

 Test a very weak password (e.g. Password1!) -> should return Insecure • Test a strong password (e.g. P@ssw0rd2026!) -> should return Strong*.

3. Test Saving & Retrieving Credentials:

* Choose option 3 and provide the following information (e.g. Site: github.com, User: dev, Pass: Secret123!).

* Observe the generated "vault.txt" file to verify password masking.

* Choose option 4` within the application to verify that the password is displayed unmasked when read.
