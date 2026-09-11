# Odoo-learning

Projet personnel d'apprentissage et d'expérimentation autour de **python** et **Odoo 19**.

L'objectif est de découvrir python ainsi que le fonctionnement d'Odoo, son architecture, le développement de modules personnalisés et son intégration avec PostgreSQL.

L'architecture de développement est basée sur [https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026) avec les adaptations suivantes :

* Adaptation à **Odoo 19**.
* Ajout d'un conteneur **pgAdmin** pour faciliter l'administration et la visualisation de la base de données PostgreSQL.

<br>

Pour démarrer un projet tout frais voir la section suivante :**<br>[🚀 Démarrer un projet tout frais 🚀](#fresh-clone)**.
<br>
<br>

## 🛠️ Technologies

* **Odoo 19.0**
* **Python 3.12**
* **PostgreSQL**
* **Docker / Docker Compose**
* **VS Code**
    * Extension Odoo de Odoo (version 1.5.0 et > requise)
    * Extension Python de Microsoft
* **WSL2 / Ubuntu**
* **Git**
<br>
<br>

## 📁 Structure du projet

```text
Odoo-learning/
├── .vscode/               # Configurations VS Code
├───── launch.json         # Configurations de débogage et tests
├───── settings.json       # Configuration Python VS Code
├── custom-addons/         # Modules Odoo personnalisés
├── data/                  # Données générées par Odoo                  ⚠️[NON COMMITÉ]
├── odoo/                  # Code source d'Odoo                         ⚠️[NON COMMITÉ]
├── venv/                  # Environnement virtuel Python               ⚠️[NON COMMITÉ]
├── .env                   # Variables d'environnement                  ⚠️[NON COMMITÉ]
├── .env.exemple           # Variables d'environnement (exemple)
├── .gitignore
├── compose.yaml           # Services Docker (PostgreSQL, pgAdmin)
├── odoo.dev.conf          # Configuration Odoo pour le développement   ⚠️[NON COMMITÉ]
├── odoo.dev.conf.exemple  # Configuration Odoo pour le développement (exemple)
├── odools.toml            # Configuration de Odoo Language Server
├── README.md
├── run.sh                 # Script de lancement d'Odoo
└── sitecustomize.py       # Filtre les avertissements @t-esc dépréciés de certains
                             modules (odoo.addons.base.models.ir_qweb uniquement)
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
```
source venv/bin/activate
```
💡_(venv) doit apparaître, exemple :_ 
>user@Machine:\~/votre/répertoire/projet$ source venv/bin/activate<br>(venv) user@Machine:\~/votre/répertoire/projet$<br>
<br>

<br>

Pour lancer Odoo :

```
./run.sh
```
>⚠️ L'**environnement virtuel** doit être **activé** et le **conteneur PostgreSQL** doit être **lancé**. ⚠️

<br>

Odoo est alors accessible à l'adresse :

```
http://localhost:8069
```

<br>

**Identifiants de développement :**

```
Login    : admin
Password : admin
```

>⚠️ Ces identifiants sont uniquement destinés à l'environnement local de développement. ⚠️

<br>

Pour arrêter Odoo `CTRL + C` dans le terminal.

<br>

💡_L'environnement virtuel peut être désactivé avec :_
```
deactivate.
```
_Exemple :_
>(venv) user@Machine:\~/votre/répertoire/projet$ deactivate<br>user@Machine:\~/votre/répertoire/projet$<br>
<br>

<br>

### 🐛 Erreurs courantes : 
Au lancement de `./run.sh`, si le terminal renvoie :

>...<br>
2026-09-07 07:51:59,674 18344 INFO ? odoo.service.server: AutoReload watcher running with watchdog<br>
Address already in use<br>
Port 8069 is in use by another program. Either identify and stop that program, or start the server with a different port.<br>
(venv) user@Machine:~/votre/répertoire/projet$

Ceci se produit lorsque vous fermez VS Code sans avoir arrêté Odoo avec `CTRL + C` dans le terminal par exemple.<br>
Odoo restera fonctionnel mais vous n'aurez plus la main sur les logs d'Odoo dans le terminal.

Pour remédier à cela, indentifier le processus Odoo avec `sudo lsof -i :8069`, le tuer avec `kill` puis relancer Odoo avec `./run.sh` :
_Exemple :_
>(venv) user@Machine:\~/votre/répertoire/projet$ lsof -i :8069<br>
COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME<br>
python  8139    user   15u  IPv4 287191      0t0  TCP *:8069 (LISTEN)<br>
python  8139    user   24u  IPv4 293327      0t0  TCP localhost:8069->localhost:56040 (ESTABLISHED)<br>
<br>
(venv) user@Machine:~/votre/répertoire/projet$ kill 8139<br>
<br>
(venv) user@Machine:~/votre/répertoire/projet$ ./run.sh<br>
2026-09-07 08:09:41,491 28201 INFO ? odoo: Odoo version 19.0<br>
...<br>
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

Pour créer un module :

```
./venv/bin/python odoo/odoo-bin scaffold NomDuModule custom-addons/
```

<br>
<br>

## 🚀 Démarrer un projet tout frais 🚀 <a id="fresh-clone"></a>

_`A venir, la branche 'fresh-clone' n'est pas encore opérationnelle...`_

_`test fresh-clone en cours...`_

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
<br>

#### 🔧 Cloner la branche `fresh-clone` :

```
git clone --depth 1 --branch fresh-clone https://github.com/Emilien-GIBEAUD/Odoo-learning.git
```
<br>

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
<br>

#### 🔧 Créer l'environnement virtuel :

```
cd ~/votre/dossier/projets/
```

```
python3.12 -m venv venv
```

```
source venv/bin/activate
```

```
pip install --upgrade pip wheel
```

```
pip install -r odoo/requirements.txt
```

```
pip install ipdb watchdog python-dotenv
```
<br>

#### 🔧 Configurer votre projet :

Saisissez vos données et secrets dans les fichiers `.env` et `odoo.dev.conf` (en vous aidant des fichiers `.env.exemple` et `odoo.dev.conf.exemple`).

<br>

#### 🔧 Installer les extensions VS Code :

Installez les extensions `Odoo` de Odoo et `Python` de Microsoft.

<br>

_Adaptation [ECOSIRE](https://ecosire.com/blog/how-to-set-up-odoo-development-environment-2026) ...<br>
`En cours , ...`_


Vous pouvez maintenant lancer odoo et commencer vos développements, voir la section suivante :**<br>[▶️ Lancer Odoo](#run-odoo)**.
<br>
<br>
