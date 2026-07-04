# 🛡️ Web Vulnerability Scanner

A Python-based web vulnerability scanner that performs basic security assessments on web applications. The tool analyzes a target website for common security issues such as SQL Injection indicators, Cross-Site Scripting (XSS) indicators, HTML forms, and important HTTP security headers.

> 🎯 Developed as **Task 3** for the Cyber Security Internship.

---

## 📸 Project Preview

<img width="900" alt="Project Screenshot" src="images/project.png">

> **Note:** Create an **images** folder and save your project screenshot as **project.png**.

---

# 🚀 Features

- ✅ Scan website for possible SQL Injection indicators
- ✅ Scan HTML forms for possible XSS reflection
- ✅ Detect all HTML forms
- ✅ Analyze GET and POST forms
- ✅ Check important HTTP Security Headers
- ✅ Display scan summary
- ✅ Simple Command Line Interface (CLI)
- ✅ Lightweight and easy to use

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Requests | HTTP Requests |
| BeautifulSoup4 | HTML Parsing |
| urllib.parse | URL Handling |

---

# 📁 Project Structure

```text
Task_3/
│
├── web_vulnerability_scanner.py
├── requirements.txt
├── README.md
├── report.txt
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

Move into Task 3

```bash
cd Internship_CDZ/Task_3
```

---

## Install Dependencies

Check Python Version

```bash
python3 --version
```

Install Required Libraries

```bash
python3 -m pip install requests beautifulsoup4 --break-system-packages
```

Or

```bash
pip install -r requirements.txt
```

---

# ▶ Run Application

```bash
python3 web_vulnerability_scanner.py
```

Example

```text
==================================================
      WEB VULNERABILITY SCANNER
==================================================

Enter Target URL:
```

Enter a target URL

```text
http://testphp.vulnweb.com
```

---

# 🧪 Example Scan

Input

```text
http://testphp.vulnweb.com
```

Example Output

```text
==================================================
      WEB VULNERABILITY SCANNER
==================================================

Checking SQL Injection...

SQL Injection Not Detected

Checking XSS...

Forms Found: 2

XSS Not Detected

Checking Security Headers...

Content-Security-Policy : Missing

X-Frame-Options : Present

Strict-Transport-Security : Missing

X-Content-Type-Options : Present

Referrer-Policy : Missing

Scan Completed.
```

---

# 🔍 Scan Modules

The scanner performs the following security checks:

- SQL Injection Detection
- Cross-Site Scripting (XSS) Detection
- HTML Form Discovery
- GET & POST Form Analysis
- HTTP Security Header Analysis

---

# ⚡ Workflow

```text
User
   │
   ▼
Enter Website URL
   │
   ▼
Connect to Website
   │
   ▼
Analyze HTML Forms
   │
   ▼
Check SQL Injection Indicators
   │
   ▼
Check XSS Indicators
   │
   ▼
Analyze Security Headers
   │
   ▼
Display Scan Result
```

---

# 📚 Learning Outcome

Through this project, I learned:

- Web Application Security Basics
- HTTP Requests using Requests Library
- HTML Parsing with BeautifulSoup
- Form Analysis
- Security Header Inspection
- Basic Vulnerability Assessment
- Python Automation

---

# 🔮 Future Improvements

- 🔐 HTTPS Configuration Analysis
- 🍪 Cookie Security Check
- 📝 robots.txt Detection
- 🗺 Sitemap Detection
- 📄 PDF Scan Report
- 🌐 Multi-page Crawling
- 📊 Risk Score Generation
- 🎨 Colored Terminal Output

---

# ⚠ Disclaimer

This project is created for **educational purposes only** and should be used **only on websites that you own or have explicit permission to test**. Unauthorized security testing of third-party systems may violate laws and regulations.

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

## Task 3

**Web Vulnerability Scanner**

---

### ⭐ If you like this project, don't forget to star the repository.