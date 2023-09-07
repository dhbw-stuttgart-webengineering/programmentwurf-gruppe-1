# DHBW Notenvergleich

Ein Projekt um via Dualis Login Noten auszulesen und sich mit anderen Studenten vergleichen zu können.

## Wichtige Links

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/IEPW_6q_)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11744256&assignment_repo_type=AssignmentRepo)

## Virtualenv Tutorial

Zur einfachen Arbeit mit Python empfehle ich euch virtual env zu nutzen:

### Installation

Installieren der Python Anwendung `virtualenv`.

    pip install virtualenv

Erstellen der virtuellen Umgebung im Ordner `venv`.

    virtualenv venv

Aktivierung der virtuellen Umgebung.

    ./venv/Scripts/activate

VSCode wird die virtuelle Umgebung erkennen und fragen ob ihr diese für den Workspace nutzen wollt. Antwortet dort mit ja.

Um die erfolgreiche Installation zu überprüfen könnt ihr folgendes eingeben:

    which python3

Nun könnt ihr ganz normal weiter arbeiten. Um nötige Bibliotheken zu installieren könnt ihr noch mit `pip` die aufgelistetet Bibliotheken aus der `requirements.txt` installieren

    pip install -r requirements.txt

## Empfohlene Extensions

Python:

- [autoDocsstring](vscode:extension/njpwerner.autodocstring)
- [autopep8](vscode:extension/ms-python.autopep8)
- [django](vscode:extension/batisteo.vscode-django)
- [Flake8](vscode:extension/ms-python.flake8)
- [isort](vscode:extension/ms-python.isort)
- [Pylance](vscode:extension/ms-python.vscode-pylance)
- [Python](vscode:extension/ms-python.python)
- [Python Extended](vscode:extension/tushortz.python-extended-snippets)
- [Python Indent](vscode:extension/KevinRose.vsc-python-indent)

Grafiken erstellen

- [Draw.io Integration](vscode:extension/hediet.vscode-drawio)

GitHub Integrationen

- [GitHub Copilot](vscode:extension/GitHub.copilot)
- [GitLens](vscode:extension/eamodio.gitlens)

HTML und CSS

- [HTML Boilerplate](vscode:extension/sidthesloth.html5-boilerplate)
- [HTML CSS Support](vscode:extension/ecmel.vscode-html-css)
- [W3C Web Validator](vscode:extension/CelianRiboulet.webvalidator)

Einfaches erstellen von README-Files in Markdown

- [Markdown](vscode:extension/yzhang.markdown-all-in-one)
