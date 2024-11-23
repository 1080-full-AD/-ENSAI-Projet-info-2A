
# ENSAI-Info-Project-2A

Source code for the computer science project in the **Compléments d'informatique** course at ENSAI [Link](https://ludo2ne.github.io/ENSAI-2A-Projet-info/).

Authors: Attig Chahine, Gibert Adrien, Kambou Hery Ruth, Madec Jeanne, Saleck Mohamed

## Objectives

This application interacts with mangas from an open-source API.

- Search for a manga by its title or mangaka
- Share opinions about these mangas
- Share manga collections

## Installation

Install the required packages using the following bash commands:

```bash
pip install -r requirements.txt     # Install all the packages listed in the file
pip list                            # Get the list of installed packages
```

- **inquirerPy**: Library for creating interactive text-based menus with questions and options for users.
- **pytest**: Powerful Python testing framework.
- **python-dotenv**: Library for loading environment variables from .env files.
- **requests**: Designed to make HTTP requests more accessible to humans.

## Unit Tests

```bash
python -m pytest -v
```

## Running the Application

```bash
python src/__main__.py
```
