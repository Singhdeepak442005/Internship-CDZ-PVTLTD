# 🛡️ Fake Social Media Profile Detector

A Python-based web application that analyzes basic social media profile information and predicts whether a profile is genuine or potentially fake using predefined cybersecurity rules.

> 🎯 Developed as **Task 2** for the Cyber Security Internship.

---

## 📸 Project Preview

<img width="900" alt="Project Screenshot" src="images/project.png">

> **Note:** Create an `images` folder and save your project screenshot as **project.png** for the preview to appear on GitHub.

---

# 🚀 Features

- ✅ Analyze social media profile details
- ✅ Followers vs Following ratio analysis
- ✅ Post count verification
- ✅ Profile picture validation
- ✅ Bio length analysis
- ✅ Instant Fake / Genuine detection
- ✅ Displays detection reasons
- ✅ Simple & Responsive User Interface

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend |
| Flask | Web Framework |
| HTML5 | Frontend |
| CSS3 | Styling |

---

# 📁 Project Structure

```text
Task_2/
│
├── fake_social_media_profile_detector.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/Singhdeepak442005/Internship_CDZ.git
```

Move into project

```bash
cd Internship_CDZ/Task_2
```

---

## Install Dependencies

Check Python

```bash
python3 --version
```

Install Flask

```bash
pip install flask
```

For Kali Linux / Parrot OS

```bash
python3 -m pip install flask --break-system-packages
```

---

# ▶ Run Application

```bash
python3 fake_social_media_profile_detector.py
```

Output

```text
* Serving Flask app 'fake_social_media_profile_detector'
* Running on http://127.0.0.1:5000
```

Open Browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Test Case 1

| Field | Value |
|-------|------|
| Followers | 50 |
| Following | 50 |
| Posts | 5 |
| Profile Picture | Yes |
| Bio | hi |

### Output

```text
✅ Profile Looks Genuine

Reason

• Bio is too short
```

---

# 🧪 Test Case 2

| Field | Value |
|-------|------|
| Followers | 50 |
| Following | 30 |
| Posts | 2 |
| Profile Picture | No |
| Bio | hi |

### Output

```text
⚠ Fake Profile Suspected

Reasons

• Very few posts
• No profile picture
• Bio is too short
```

---

# 🔍 Detection Logic

The application checks the following rules:

- Followers less than **20**
- Following more than **5× Followers**
- Posts less than **3**
- No Profile Picture
- Bio length less than **10 characters**

Profiles matching multiple suspicious conditions are classified as **Fake Profiles**.

---

# ⚡ Workflow

```text
User
   │
   ▼
Fill Profile Details
   │
   ▼
Flask Server
   │
   ▼
Python Detection Logic
   │
   ▼
Analyze Profile
   │
   ▼
Display Result
```

---

# 🔮 Future Improvements

- 🤖 Machine Learning Detection
- 🌐 Live Instagram Analysis
- 🌐 Facebook Profile Support
- 🌐 X (Twitter) Support
- 📊 Confidence Score
- 🗄 Database Integration

---

# 📚 Learning Outcome

Through this project, I learned:

- Flask Web Framework
- HTML Form Handling
- Python Backend Development
- Cybersecurity Rule-Based Detection
- Frontend & Backend Integration

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

## Task 2

**Fake Social Media Profile Detector**

---

### ⭐ If you like this project, don't forget to star the repository.