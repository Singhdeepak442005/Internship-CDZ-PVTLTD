# AES-256 File Encryptor

## 📌 Project Description

AES-256 File Encryptor is a Python-based cybersecurity tool that securely encrypts and decrypts files using the AES-256 encryption algorithm. It protects sensitive files from unauthorized access by generating a secure encryption key and allowing only authorized users to decrypt the encrypted files.

---

## 🚀 Features

- Encrypt files using AES-256 Encryption
- Decrypt encrypted files
- Automatic Secret Key Generation
- Secure File Protection
- Easy-to-use Command-Line Interface (CLI)

---

## 🛠️ Technologies Used

- Python 3
- cryptography

---

## 📂 Project Structure

```
Task_4/
│── aes_file_encryptor.py
│── sample.txt
│── sample.txt.encrypted
│── secret.key
│── requirements.txt
│── report.txt
│── README.md
```

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/Singhdeepak442005/CDZ-Cyber-Security-Internship.git
```

### Go to Task 4

```bash
cd CDZ-Cyber-Security-Internship/Task_4
```

### Install Required Library

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Program

```bash
python3 aes_file_encryptor.py
```

---

## 📸 Example

### Encrypt a File

Input

```
Enter Choice : 1
Enter File Name : sample.txt
```

Output

```
[+] Encryption Key Generated Successfully.

[✓] File Encrypted Successfully

Encrypted File : sample.txt.encrypted
```

---

### Decrypt a File

Input

```
Enter Choice : 2
Enter Encrypted File Name : sample.txt.encrypted
```

Output

```
[✓] File Decrypted Successfully

Decrypted File : sample.txt
```

---

## 📂 Generated Files

After Encryption

```
sample.txt.encrypted
secret.key
```

---

## 🎯 Purpose

The purpose of this project is to demonstrate secure file encryption and decryption using the AES-256 encryption algorithm. It helps protect confidential files from unauthorized access while ensuring data confidentiality and integrity.

---

## 👨‍💻 Author

**Deepak Singh**

Cyber Security Internship Project

Task 4 – AES-256 File Encryptor

GitHub:
https://github.com/Singhdeepak442005