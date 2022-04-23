
# Exploration d’une Base Relationnelle en SQL avec python.
## Solutions
### réflexions
Que feriez-vous pour accéder aux données d’un fichier en python?
j’ouvrirai le fichier avec une commande :
> fh = open('myFile.txt')


Comment liriez-vous les enregistrements?
* en une seule fois
> texte = fh.read()

* Ligne par ligne :
> \# Ouvrir le fichier en lecture seule
>
> file = open('file.txt', "r")
>
> for line in file:
>
> >   print(line)
>
> file.close()


Imaginez un processus pour une base de données.
Ouverture de la base
lecture d’une table.


en une seule fois ou ligne par ligne.
1.1 Se connecter
commandes interactives


> import sqlite3
> DBCon = sqlite3.connect('chinook.db')
>
> print("Connection established ..........")


### le script
connection.py
#!/home/pboizot/src/DB-sql/bin/python   
\# import du driver de connection sqlite3
import sqlite3
\# Etablissement de la connection
DBConnection = sqlite3.connect('chinook.db')
if DBConnection :
    print("Connection established ..........")
\# remarque le module sqlite3 créera une base sî il ne trouve pas le fichier # DEBUG:
\# comment vérifier que nous avons ouvert le bon fichier


DBConnection.close()
exit()




1.2 la logique d’interrogation
Comme pour un fichier l'accès aux données va se faire au travers d’une séquence d’ouverture de la base.


Mais à la différence du cas fichier on passera par les étapes intermédiaires.
1. Ouverture d’un curseur
2. Exécution d’une requête.
3. Parcours des données du curseur.
   1. en une fois :                 fetchall()
   2. ligne par ligne :         fetchone()


2. Retrouver des informations de structure de la base
La liste des tables
requete :
> select name from sqlite_master where type= ?",['table']
impression :
> for table in liste:
            print(table[0])


Le nombre de tables de la base
La requête SQL  est
ltable = DBCon.cursor()
ltable.execute("select count(*) from sqlite_master where type= ?",['table'])
nbtable = ltable.fetchone()
print(nbtable)




### Nombre d’attribut de la base :
attr=attrCursor.execute(f"pragma table_info('{table[0]}')").fetchall()


### Mémoriser ces informations dans la base
Description :Code SQL
CREATE TABLE `STATDB` (
        `NOMTABLE`        INTEGER NOT NULL UNIQUE,
        `NBLIGNE`        INTEGER NOT NULL,
        `NBATTR`        INTEGER
);

## Intégration dans python.


cur = con.cursor()
cur.execute('create table statdb (nomtable text not NULL unique, nbligne integer not null, nbattr integer )')
cur.close()
