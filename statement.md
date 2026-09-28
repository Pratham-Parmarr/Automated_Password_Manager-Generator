# Project Statement: Security Terminal & Credential Vault

## Problem Statement

With the modern explosion of online services, it is common for a user to have tens of accounts across different platforms. This often leads to bad security practices, including using weak passwords or writing down credentials in plain text. Commercial password managers are often bloated or require a connection to a proprietary server. The end user needs a lightweight, transparent, and modular local CLI utility to assess password safety, generate high-entropy strings, and store secrets offline.

---

## Scope of the Project

This project's scope is to design a multi-module Python CLI utility capable of handling basic credential-related tasks. Some of the features that should be implemented are:

- Authentication layer: a simple barrier that prevents unathorized users from printing the vault's contents.

- Password utilities: a module that can generate random strings and assess password strength.

- Local storage and obfuscation: a module that uses standard Python libraries to store the sensitive data in files in an obfuscated way.

The scope of this project does not include advanced data encryption features (AES-256), database layer utilities, or GUI elements.

---

## Target Users

- Developers and power-users: people that are comfortable with command line interfaces and want to avoid bloat.

- Students and learners: people that wish to expand their knowledge of Python by learning about string manipulation, file writing/reading, and light data encryption.

- Privacy-focused individuals: people that are concerned about online security and want to avoid potential surveillance from third parties.

---

## High-Level Features

1. Master password: a simple authentication mechanism that prevents unauthorized access to the vault.

2. Random password generator: a utility that can create strong, customizable, and random strings.

3. Password assessment: a feature that scores generated or user-submitted passwords.

4. Character masking: a helper utility that replaces characters in a string with user-defined ones.

5. File utilities: functions to append entries to a file and read a file's contents.
