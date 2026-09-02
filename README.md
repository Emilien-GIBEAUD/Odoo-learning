# Odoo-learning

Projet personnel d'apprentissage et d'expérimentation autour de **python** et **Odoo 19**.

L'objectif est de découvrir python ainsi que le fonctionnement d'Odoo, son architecture, le développement de modules personnalisés et son intégration avec PostgreSQL.

L'architecture de développement est basée sur [https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026) avec les adaptations suivantes :

* Adaptation à **Odoo 19**.
* Ajout d'un conteneur **pgAdmin** pour faciliter l'administration et la visualisation de la base de données PostgreSQL.

## 🛠️ Technologies

* **Odoo 19.0**
* **Python 3.12**
* **PostgreSQL**
* **Docker / Docker Compose**
* **VS Code**
* **WSL2 / Ubuntu**
* **Git**

## 📁 Structure du projet

```text
Odoo-learning/
├── .vscode/               # Configuration VS Code
├── custom-addons/         # Modules Odoo personnalisés
├── data/                  # Données générées par Odoo                  ⚠️[NON COMMITÉ]
├── odoo/                  # Code source d'Odoo                         ⚠️[NON COMMITÉ]
├── venv/                  # Environnement virtuel Python               ⚠️[NON COMMITÉ]
├── .env                   # Variables d'environnement                  ⚠️[NON COMMITÉ]
├── .gitignore
├── compose.yaml           # Services Docker (PostgreSQL, pgAdmin)
├── odoo.dev.conf          # Configuration Odoo pour le développement   ⚠️[NON COMMITÉ]
├── README.md
└── run.sh                 # Script de lancement d'Odoo
```

## 🚀 Installation

à venir

## ▶️ Lancer Odoo

à venir

## 🐳 Services Docker

à venir

## 📦 Modules personnalisés

Les développements spécifiques au projet seront placés dans :

```text
custom-addons/
```

Chaque module Odoo sera créé comme un sous-répertoire de ce dossier.
