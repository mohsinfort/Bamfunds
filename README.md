# 🎭 Pytest + Playwright Test Automation  

🚀 This repository contains **end-to-end (E2E) tests** using **Playwright** with **Pytest** for fast, reliable web automation.  

---

## 📌 Features  
✅ **Playwright for browser automation** (Chromium, Firefox, WebKit)  
✅ **Pytest for structured test execution**  
✅ **Page Object Model (POM) for maintainability**  
✅ **Parallel execution support**  
✅ **HTML & Allure reports** for debugging  
✅ **Headless & headed mode support**  

---

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Playwright Browsers
```sh
playwright install
```

## 📌 Running Tests
### Run All Tests
```sh
pytest --headed
```
Runs tests in browser mode.

### Run a Specific Test File
```sh
pytest tests/e2e/test_login.py
```
## 📌 Generating Test Reports
HTML Report
```sh
pytest --html=report.html --self-contained-html
