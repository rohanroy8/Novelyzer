# 📖 Novelyzer

> **A fast, lightweight CLI text analyzer for novels, books, and long-form documents.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Repo Status](https://img.shields.io/badge/Status-Active-brightgreen.svg?style=for-the-badge)](#)

---

## 🌟 Overview

**Novelyzer** is a Python command-line utility designed to quickly analyze text documents and manuscripts. It provides instant statistics including total word counts and prominent keyword frequency distributions with zero external dependencies.

---

## ✨ Features

- ⚡ **Zero Dependencies**: Built entirely with Python's standard library.
- 📊 **Word Count**: Fast and accurate word count computation across any text file.
- 🔍 **Top Keyword Frequency**: Automatically filters trivial words (< 6 characters) to highlight dominant themes and vocabulary.
- 🖥️ **Clean Terminal Output**: Clear, structured terminal report with divider sections.

---

## 🖥️ Sample Output

```text
============ BOOKBOT ============
Analyzing book found at sample.txt...
----------- Word Count ----------
Found 42 words in the file
--------- Top 10 Word Frequency -------
novelyzer : 2
analyzing : 2
analytical : 1
specifically : 1
novels, : 1
books, : 1
manuscripts. : 1
analysis : 1
effortless : 1
provides : 1
============= END ===============
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/FIREICE03/Novelyzer.git
cd Novelyzer
```

### 2. Run analysis
Pass any text file as an argument:

```bash
python main.py <path-to-file>
```

#### Example:
```bash
python main.py sample.txt
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m "Add some AmazingFeature"`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📜 License

Created and maintained by **Rohan Roy**.

This project is open-source and available under the [MIT License](LICENSE).