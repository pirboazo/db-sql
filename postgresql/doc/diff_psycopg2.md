
## Les différences

Nous allons regarder rapidement les différences entre les drivers **sqlite3** et **psycopg2**.

1. l'import du driver

\# import du driver de connection sqlite3   
import sqlite3   
versus   
import psycopg2

2. la gestion de la connection.

\# Etablissement de la connection

DBConnection = sqlite3.connect('chinook.db')   
versus   
DBCon = psycopg2.connect(database="chinook", user="chinook", password="chinook", host="192.168.1.135", port="5432")

Dans un cas on fait référence au fichier de base sqlite3 dans l'autre on indique tous les paramètres de la chaine de connection.

3. Ouverture du curseur.

C'est la même chose avec les deux drivers

verif = DBCon.cursor()

4. L'execution et fetch résultat.

  * sqlite3
>version = verif.execute("select sqlite_version()").fetchone()

  * psycopg2
  La syntaxe sqlite3 n'est pas acceptée.

  > verif.execute("select version()")  
  > version = verif.fetchone()
