# 🛡️ File Integrity Monitor

A Python-based cybersecurity tool that monitors file integrity by calculating and comparing SHA-256 hash values. The application detects any unauthorized modifications made to monitored files and helps ensure data integrity.

> 🎯 Developed as **Task 1** for the Cyber Security Internship.

---

## 📸 Project Preview

<img width="900" alt="Project Screenshot" src="images/project.png">

> **Note:** Create an `images` folder inside your project and save your project screenshot as **project.png**.

---

# 🚀 Features

- ✅ Calculate SHA-256 hash of any file
- ✅ Store hash values in JSON format
- ✅ Compare previous and current hash values
- ✅ Detect file modifications
- ✅ Verify file integrity
- ✅ Simple Command Line Interface (CLI)
- ✅ Lightweight and easy to use

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| hashlib | SHA-256 Hash Generation |
| json | Store Hash Values |
| os | File Handling |

---

# 📁 Project Structure

```text
Task_1/
│
├── file_integrity_monitor.py
├── sample.txt
├── hashes.json
├── README.md
│
└── images/
    └── project.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Singhdeepak442005/Internship_CDZ.git
```

Move into Task 1

```bash
cd Internship_CDZ/Task_1
```

---

## Requirements

Check Python Version

```bash
python3 --version
```

No external libraries are required because this project only uses Python's built-in modules.

---

# ▶ Run Application

```bash
python3 file_integrity_monitor.py
```

When prompted, enter the file name:

```text
sample.txt
```

---

# 🧪 Test Case 1

### First Run

Input

```text
sample.txt
```

Output

```text
📁 New file detected.
Hash stored successfully.
```

---

# 🧪 Test Case 2

Modify the file.

Example:

```text
Hello World

This file has been modified.
```

Run again

```bash
python3 file_integrity_monitor.py
```

Input

```text
sample.txt
```

Output

```text
⚠ WARNING!
File has been modified!

Old Hash :
xxxxxxxxxxxxxxxxxxxxxxxxxxxx

New Hash :
yyyyyyyyyyyyyyyyyyyyyyyyyyyy
```

---

# 🧪 Test Case 3

Run the application again **without modifying** the file.

Input

```text
sample.txt
```

Output

```text
✅ File Integrity Verified.

No changes detected.
```

---

# 🔍 How It Works

The application follows these steps:

1. User enters the file path.
2. Python reads the file in binary mode.
3. SHA-256 hash is generated.
4. Previous hash is loaded from `hashes.json`.
5. Current and previous hashes are compared.
6. If hashes match, the file is verified.
7. If hashes differ, the application reports that the file has been modified.
8. The latest hash is stored for future comparisons.

---

# ⚡ Workflow

```text
User
   │
   ▼
Select File
   │
   ▼
Read File
   │
   ▼
Generate SHA-256 Hash
   │
   ▼
Compare with Stored Hash
   │
   ├───────────────┐
   │               │
   ▼               ▼
Same Hash      Different Hash
   │               │
   ▼               ▼
Integrity      Warning
Verified       File Modified
```

---

# 📚 Learning Outcome

Through this project, I learned:

- SHA-256 Hashing
- File Integrity Verification
- Python File Handling
- JSON Data Storage
- Cybersecurity Fundamentals
- Command Line Application Development

---

# 🔮 Future Improvements

- 📁 Monitor multiple files simultaneously
- 📂 Folder integrity monitoring
- 🔔 Real-time file change alerts
- 🗂 Automatic scheduled scanning
- 📧 Email notification support
- 🖥 GUI Version using Tkinter

---

# 👨‍💻 Author

## Deepak Singh

Cyber Security Researcher

🎓 MCA Student

🇮🇳 India

### GitHub

https://github.com/Singhdeepak442005

### LinkedIn

https://www.linkedin.com/in/ddeepak-singh/

---

# ⭐ Internship

Cyber Security Internship

## Task 1

**File Integrity Monitor**

---

### ⭐ If you like this project, don't forget to star the repository.