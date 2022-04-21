
# SQLITE en ligne de commande.

Nous avons vu une possibilité d'interroger une ~base~/fichier sqlite avec [sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser/wiki) c'est sympa facile d'utilisation mais pas dificile à utiliser en script.

 Il existe un utilitaire utilisable en ligne de commande.

 * sqlite3

Avec sqlite3 il est possible d'utiliser le langage SQL et des commandes propres à SQLite on les nomme les "dot-commands".

vous en connaitrez la liste par la commande .help

>sqlite> .help
.archive ...             Manage SQL archives
.auth ON|OFF             Show authorizer callbacks
.backup ?DB? FILE        Backup DB (default "main") to FILE
.bail on|off             Stop after hitting an error.  Default OFF
.binary on|off           Turn binary output on or off.  Default OFF
.cd DIRECTORY            Change the working directory to DIRECTORY
.changes on|off          Show number of rows changed by SQL
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.databases               List names and files of attached databases
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options

pour connaitre les arguments de chaque commandes taper .help "la commande"

> .help import
> .import FILE TABLE       Import data from FILE into TABLE
   Options:
     --ascii               Use \037 and \036 as column and row separators
     --csv                 Use , and \n as column and row separators
     --skip N              Skip the first N rows of input
     -v                    "Verbose" - increase auxiliary output
   Notes:
     *  If TABLE does not exist, it is created.  The first row of input
        determines the column names.
     *  If neither --csv or --ascii are used, the input mode is derived
        from the ".mode" output mode
     *  If FILE begins with "|" then it is a command that generates the
        input text.

ou

> .help shell
.shell CMD ARGS...       Run CMD ARGS... in a system shell




il est possible d'écrire des scripts SQL et de les exécuter non interactivement.


## Exemple
Recréatation de chinook.db sous un autre nom

Traitement des tables
> sqlite3 chinook-test.db < creatable.sql

Import des données.
