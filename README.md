# Flashcards

[![Polish](https://img.shields.io/badge/Język-Polski-red)](#pl)
[![English](https://img.shields.io/badge/Language-English-blue)](#en)

---
<a id="pl"></a>
## 🔴 Wersja Polska 🔴
Prosta aplikacja webowa do nauki za pomocą fiszek. 
Projekt skupia się na funkcjonalności CRUD oraz pozwala na rejestrację z autorskim systemem weryfikacji CAPTCHA.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/tailwind-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Library-green?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SHA-512](https://img.shields.io/badge/Security-SHA--512-red?style=for-the-badge)

### 🤖 Użycie AI i Tutoriali
Podczas tworzenia projektu używałem sztucznej inteligencji (Gemini).  
Asystowała mi przy tworzeniu projektu - w tym hostingu.

### ⚙️ Działanie i funkcje
1. System Kont: Rejestracja i logowanie z wykorzystaniem wbudowanego systemu Django.
2. Autorska CAPTCHA: Podczas rejestracji użytkownik musi pomyślnie przejść weryfikację CAPTCHA.
3. Zarządzanie Fiszkami: System CRUD dla talii oraz poszczególnych kart.
4. Tryb Nauki: Tryb pozwalający na przejście przez wybraną talię fiszek.

**Spróbuj sam:** <p align="center">
[Flashcards App](https://flashcardsapp.up.railway.app/)

### 🏭 Struktura Projektu
```text
📦 Katalog główny projektu
├── application/                   # Folder aplikacji
│   ├── utils/                     # Skrypt CAPTCHA i czcionki
│   ├── templates/                 # Podstrony HTML
│   ├── modles.py                  # Klasy dla SQL
│   └── views.py                   # Logika każdej podstrony
│  
├── flashcards_app/                # Konfiguracja projektu
├── theme/                         # Tailwind CSS
├── manage.py                      # Skrypt startu/zarządzania
├── requirements.txt               # Zależności projektu
├── Procfile                       # Konfiguracja dla hostingu
└── README.md                      # O projekcie
```

---
<a id="en"></a>
## 🔵 English Version 🔵
Simple web app for flashcards learning.
Project uses CRUD functionality for decks and cards; it also allows users to register an account - with custom CAPTCHA.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/tailwind-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Library-green?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SHA-512](https://img.shields.io/badge/Security-SHA--512-red?style=for-the-badge)

### 🤖 AI Usage and Tutorials
I used AI (Gemini) during the creation of this project.  
It assisted me during the creation of this project - hosting included.
I used [Dannis Ivy's]([https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=1]) tutorial to understand the core structure of Django.

### ⚙️ Functions
1. Account System: Account registration and login with basic Django auth system.
2. Custom CAPTCHA: During creation of an account, a user has to successfully solve a CAPTCHA.
3. Flashcards Management: CRUD system for decks and every single card.
4. Learning Mode: Standard learning mode, which allows a user to go through a deck of his choosing.

**Try for yourself:** <p align="center">
[Flaskcardsapp]([https://www.google.com](https://flashcardsapp.up.railway.app/))

### 🏭 Project structure
```text
📦 Project Main Directory
├── application/                   # App folder
│   ├── utils/                     # CAPTCHA script and fonts
│   ├── templates/                 # HTML code
│   ├── modles.py                  # Classes for SQL
│   └── views.py                   # Logic of the app
│  
├── flashcards_app/                # Project config
├── theme/                         # Tailwind CSS
├── manage.py                      # Main starting script
├── requirements.txt               # Project requirements
├── Procfile                       # host config
└── README.md                      # About the project
```
