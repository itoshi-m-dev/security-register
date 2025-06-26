# 🛡️ Employee Credentials Generator

A simple and secure Python script to generate usernames and passwords for company employees, storing the results in two organized CSV files.

---

## 🚀 Features

- Generates usernames from full names (e.g., `john.doe`)
- Creates strong, random passwords with letters, digits, and symbols
- Logs:
  - `usuarios.csv`: full info (name, username, password)
  - `funcionarios.csv`: names only

---

## 🧪 Example

**Input:**
```
Enter employee's name: João Silva
```

**Generated output:**
```
Username: joao.silva
Password: 8&Tu@X1Lm#vP
```

---

## 📁 Files created

- `usuarios.csv` – contains name, username, and password
- `funcionarios.csv` – contains only the name for records

---

## 🛠️ Technologies

- Python 3.10+
- `csv`, `random`, `string`, `pathlib`

---

## ⚙️ How to run

```bash
python gerar_credenciais.py
```

Then follow the prompts in your terminal.

---

## 🧼 Git structure

Includes a `.gitignore` to avoid pushing unnecessary files like:

- `__pycache__/`
- `.env`, `.venv/`
- `.csv` data
- editor configs like `.vscode/`

---

## 👨‍💻 Author

Made by Emanuel  — just a dev having fun with Python automation and secure credential generation.
