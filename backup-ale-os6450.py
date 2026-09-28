# backup_simple.py
# Version débutant : sauvegarde la configuration des switchs ALE OS6450

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# On demande les identifiants au lancement (le mot de passe ne s'affiche pas)
utilisateur = input("Utilisateur : ")
mot_de_passe = getpass("Mot de passe : ")

# La liste des adresses IP des switchs
switches = ["192.168.X.X", "192.168.X.X", "192.168.X.X"]

# La date du jour, pour nommer les fichiers (ex : 2026-09-28)
date = datetime.now().strftime("%Y-%m-%d")

# On passe sur chaque switch, un par un
for ip in switches:
    print("Connexion à", ip)

    # 1. Se connecter en SSH au switch
    connexion = ConnectHandler(
        device_type="alcatel_aos",
        host=ip,
        username=utilisateur,
        password=mot_de_passe,
    )

    # 2. Récupérer la configuration
    configuration = connexion.send_command("show configuration snapshot")

    # 3. Se déconnecter
    connexion.disconnect()

    # 4. Enregistrer la configuration dans un fichier
    nom_fichier = "backup_" + ip + "_" + date + ".txt"
    fichier = open(nom_fichier, "w")
    fichier.write(configuration)
    fichier.close()

    print("Sauvegarde OK :", nom_fichier)

print("Terminé !")
