# Odoo-learning

Projet personnel d'apprentissage et d'expérimentation autour de **python** et **Odoo 19**.

L'objectif est de découvrir python ainsi que le fonctionnement d'Odoo, son architecture, le développement de modules personnalisés et son intégration avec PostgreSQL.

L'architecture de développement est basée sur [https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026) avec les adaptations suivantes :

* Adaptation à **Odoo 19**.
* Ajout d'un conteneur **pgAdmin** pour faciliter l'administration et la visualisation de la base de données PostgreSQL.

<br>

Pour démarrer un projet tout frais voir la section **[🚀 Démarrer un projet tout frais 🚀](#fresh-clone)**.
<br>
<br>

## 🛠️ Technologies

* **Odoo 19.0**
* **Python 3.12**
* **PostgreSQL**
* **Docker / Docker Compose**
* **VS Code** avec l'extension odoo (version 1.5.0 et > requise)
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

## 🐘 Base de données

**PostgreSQL** fonctionne dans un conteneur Docker.

Un conteneur **pgAdmin** est également présent pour faciliter l'administration et la visualisation de la base de données.

La base de données utilisée pour le développement est `dev_db` et les paramètres de connexion sont définis dans `odoo.dev.conf`.

🚀 Pour lancer les conteneurs **PostgreSQL** et **pgAdmin** 🚀 :

```
docker compose up -d
```
<br>

## ▶️ Lancer Odoo <a id="run-odoo"></a>

Depuis le répertoire du projet, activer l'environnement virtuel :
><span style="color:#00FF00">**user@Machine**</span> : <span style="color:#0000FF">**~/votre/répertoire/courant**</span> \$ source venv/bin/activate<br>(venv) <span style="color:#00FF00">**user@Machine**</span> : <span style="color:#0000FF">**~/votre/répertoire/courant**</span> \$<br>
<br>

<br>

Depuis le répertoire du projet, **avec l'environnement virtuel activé** :

```
./run.sh
```
<br>

Odoo est alors accessible à l'adresse :

```
http://odoo.localhost:8069
```
<br>

**Identifiants de développement :**

```
Login    : admin
Password : admin
```

>⚠️ Ces identifiants sont uniquement destinés à l'environnement local de développement. ⚠️

<br>

_L'environnement virtuel peut être désactivé avec `deactivate` :_

>(venv) <span style="color:#00FF00">**user@Machine**</span> : <span style="color:#0000FF">**~/votre/répertoire/courant**</span> \$ deactivate<br><span style="color:#00FF00">**user@Machine**</span> : <span style="color:#0000FF">**~/votre/répertoire/courant**</span> \$ <br>
<br>

<br>

## 🐳 Services Docker

Lancer les conteneurs :

```
docker compose up -d
```
<br>

Arrêter les conteneurs :

```
docker compose down
```
<br>

Se connecter au conteneur PostgreSQL (en bash) :

```
docker exec -it postgres bash
```
<br>

---
🚀 <strong>Arrêter les conteneurs et supprimer également les volumes </strong> 🚀  
Permet de repartir d'un environnement PostgreSQL vierge :</strong> 

```
docker compose down -v
```

⚠️ Cette dernière commande supprime notamment les données PostgreSQL et pgAdmin.
<br>
<br>

## 📦 Modules personnalisés

Les développements spécifiques au projet seront placés dans :

```
custom-addons/
```

Chaque module Odoo sera créé comme un sous-répertoire de ce dossier. 
<br>
<br>

## 🚀 Démarrer un projet tout frais 🚀 <a id="fresh-clone"></a>

_`A venir, la branche 'fresh-clone' n'est pas encore opérationnelle...`_

Pour démarrer un nouveau projet à partir d'un état propre du projet, la branche `fresh-clone` peut être utilisée, suivre la pocédure suivante :

#### 🔧 Installer les dépendances WSL2 :

```
sudo apt update && sudo apt install -y python3.12 python3.12-venv python3-pip \
    build-essential libxslt1-dev libzip-dev libldap2-dev libsasl2-dev \
    libpq-dev libjpeg-dev wkhtmltopdf nodejs npm git
```

```
sudo npm install -g rtlcss
```

#### 🔧 Cloner la branche `fresh-clone` :

```
git clone --depth 1 --branch fresh-clone https://github.com/Emilien-GIBEAUD/Odoo-learning.git
```

#### 🔧 Cloner les sources Odoo :

```
cd ~/votre/dossier/projets/
```

```
mkdir votre_projet && cd votre_projet
```

```
git clone --depth 1 --branch 19.0 https://github.com/odoo/odoo
```

#### 🔧 Créer l'environnement virtuel :

```
xxx
```

```
xxx
```

```
xxx
```

_Adaptation [ECOSIRE](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026)...<br>
`En cours , ...`_


Vous pouvez maintenant lancer odoo et commencer vos développements, voir la section **[▶️ Lancer Odoo](#run-odoo)**.
<br>
<br>
