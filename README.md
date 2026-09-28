# 🐧 backup-config-ale-switch

Script Python qui se connecte en **SSH via Netmiko** aux switchs **Alcatel-Lucent Enterprise OS6450** (tous modèles, quel que soit le nombre de ports) pour **sauvegarder automatiquement leur configuration** sur un NAS.

---

## ✨ Fonctionnalités

- 🔐 Connexion SSH aux switchs ALE OS6450 grâce à **Netmiko**
- 📄 Récupération de la configuration avec la commande `show configuration snapshot`
- 📁 Un dossier de sauvegarde par switch pour garder tout bien rangé
- 💾 Stockage des sauvegardes sur un **NAS via SMB**
- 🧹 Politique de rétention : seules les **5 sauvegardes les plus récentes** par switch sont conservées, les plus anciennes sont supprimées automatiquement
- 📝 Journalisation (logs) et gestion des erreurs : si un switch ne répond pas, le script continue avec les suivants

---

## 🧰 Prérequis

- Linux (testé sur **Ubuntu**)
- **Python 3.8+**
- Accès SSH activé sur les switchs
- Un partage SMB accessible (NAS)

---

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/devopsthomas/backup-config-ale-switch.git
cd backup-config-ale-switch

# Installer les dépendances
pip install netmiko
```

---

## 🔧 Configuration

1. **Monter le partage SMB du NAS** sur la machine Linux :

```bash
sudo apt install cifs-utils
sudo mkdir -p /mnt/backups
sudo mount -t cifs //IP_DU_NAS/backups /mnt/backups -o username=UTILISATEUR
```

2. **Renseigner la liste des switchs** dans le script (nom, adresse IP, identifiants) :

```python
switches = [
    {"name": "SW-CORE", "host": "192.168.X.X"},
    {"name": "SW-01",   "host": "192.168.X.X"},
]
```

> ⚠️ Ne publie jamais tes vrais identifiants ni tes vraies adresses IP sur GitHub. Utilise des variables d'environnement ou un fichier de configuration ajouté au `.gitignore`.

---

## 🚀 Utilisation

```bash
python3 backup_switches.py
```

Exemple d'arborescence obtenue :

```
/mnt/backups/
├── SW-CORE/
│   ├── SW-CORE_2026-09-28_02-00.txt
│   └── ...
└── SW-01/
    ├── SW-01_2026-09-28_02-00.txt
    └── ...
```

---

## ⏰ Automatisation (cron)

Pour lancer la sauvegarde tous les jours à 2 h du matin :

```bash
crontab -e
```

```
0 2 * * * /usr/bin/python3 /chemin/vers/backup_switches.py
```

---

## 🗺️ Améliorations prévues

- [ ] Fichier de configuration séparé (YAML ou `.env`)
- [ ] Notification par e-mail en cas d'échec
- [ ] Comparaison des configurations (détection des changements)

---

## 👤 Auteur

**Thomas Letard** — [@devopsthomas](https://github.com/devopsthomas)
Apprenti TSSR · Linux, réseau & automatisation 🐧
