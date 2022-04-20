
# SQLITE en ligne de commande.

Nous avons vu une possibilité d'interroger une ~base~/fichier sqlite avec [sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser/wiki) c'est sympa facile d'utilisation mais pas dificile à utiliser en script.

 Il existe un utilitaire utilisable en ligne de commande.

 * sqlite3

il est possible d'écrire des scripts SQL et de les exécuter non interactivement.


## Exemple
Recréatation de chinook.db sous un autre nom

> sqlite3 chinook-test.db < creatable.sql
