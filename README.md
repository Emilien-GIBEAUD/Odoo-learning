# Odoo-learning

Projet personnel d'apprentissage et d'expérimentation autour de **python** et **Odoo 19**.

L'objectif est de découvrir python ainsi que le fonctionnement d'Odoo, son architecture, le développement de modules personnalisés et son intégration avec PostgreSQL.

L'architecture de développement est basée sur [https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026) avec les adaptations suivantes :

* Adaptation à **Odoo 19**.
* Ajout d'un conteneur **pgAdmin** pour faciliter l'administration et la visualisation de la base de données PostgreSQL.
<br>
<br>

## 🛠️ Technologies

* **Odoo 19.0**
* **Python 3.12**
* **PostgreSQL**
* **Docker / Docker Compose**
* **VS Code** avec l'extension odoo (1.5.0 et >)
* **WSL2 / Ubuntu**
* **Git**
<br>
<br>

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
├── odools.toml            # Configuration de l'extension VS Code odoo
├── README.md
└── run.sh                 # Script de lancement d'Odoo
```
<br>

## 🚀 Installation

à venir
<br>
<br>

## ▶️ Lancer Odoo

à venir
<br>
<br>

## 🐳 Services Docker

Lancer les conteneurs :

```bash
docker compose up -d
```
<br>

Arrêter les conteneurs :

```bash
docker compose down
```
<br>

Se connecter au conteneur PostgreSQL (en bash) :

```bash
docker exec -it postgres bash
```
<br>

---
🚀 <strong>Arrêter les conteneurs et supprimer également les volumes </strong> 🚀  
Permet de repartir d'un environnement PostgreSQL vierge :</strong> 

```bash
docker compose down -v
```

⚠️ Cette dernière commande supprime notamment les données PostgreSQL et pgAdmin.
<br>
<br>

## 📦 Modules personnalisés

Les développements spécifiques au projet seront placés dans :

```text
custom-addons/
```

Chaque module Odoo sera créé comme un sous-répertoire de ce dossier.
