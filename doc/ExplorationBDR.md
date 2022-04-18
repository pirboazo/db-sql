
# Exploration d’une Base Relationnelle en SQL avec python.

## Comment utiliser python pour décrire une base SQLITE?

# Introduction
Comme nous avons utilisé sqlitebrowser pour parcourir notre base exemple de manière interactive, nous allons écrire un programme nous donnant des informations sur cette base.
## Au programme
### Apprendre
1. à se connecter à une base.
2. la logique de fonctionnement des interrogations
   1. Création d’un curseur
   2. Exécution d’une requête
   3. parcours des lignes retournées

### Retrouver
3. Le nombre de tables de la base
4. La liste des tables avec
   1. Le nombre d'enregistrements.
   2. Le nombre d'attributs des tables.

### Mémoriser ces informations dans la base
5. Description de la table statdb ( nom, nbrec, nbattribut )
6. Création d’une table.
   1. Insérer des enregistrements dans la table statdb.
   2. Mettre à jour des informations nbrec, nbattribut.

## Extraire
7. Export des données de la base.
   1. un fichier par table aux format csv
   2. un fichier de recréation des tables.


Création d’un rapport html avec les informations de la base.

## Pré-requis
Avoir installé
* un environnement python 3 ( Interpréteur, module sqlite3 )
* une base exemple ( chinook.db )

## Réflexion
Sur l’accès aux données d’un fichier
* Que feriez-vous pour accéder aux données d’un fichier en python?
* Comment liriez-vous les enregistrements?


Imaginez un processus pour une base de données.
## Mise en oeuvre
1.1 Se connecter Interactivement

1.2 Se connecter à une base de données en python c’est
  1. importer le driver de connexion.
  2. se connecter à la base.


A l’aide de deuxdes liens que je vous ai transmis faire une connexion interactive à la base SQLite chinook.db que vous avez téléchargé sur votre machine( en python)


Puis garder dans un fichier connection.py les instructions de connexion.


**Questions** :

> Que se passe-t-il si on se trompe de nom de fichier ?
>
> Que devez vous faire pour vous connecter à la base postgresql se trouvant sur la machine à l‘adresse 192.168.10.156 ?
Avez vous besoin d'informations supplémentaires?

## Scripter
Écrire le script réalisant la même opération en y ajoutant la fermeture de la base.  


### la logique d’interrogation
A l'aide des deux mêmes liens décrire cette logique de lecture.


> Créer un script lisant dans la table employees les (nom, prénom et date de naissance )
Ecrire les résultat sur le standard output ou dans un fichier


Faire une version avec fetchall() ou  avec fetchone().


### Retrouver des informations de structure de la base

Pour cela nous allons nous aider d’une table donnant des informations sur le contenu de la base.
Ces informations sont propres à chaque moteur de base de données. ,  il s’agit
* Pour sqlite de la table sqlite_master.
* Pour oracle de la table/vue user_tables / ALL_TABLES.
* pour mysql de la table : information_schema.tables
* pour postgresql de la table information_schema.tables

#### Le nombre de tables de la base ,
Donc retrouver le nombre de table se fera par un comptage du nombre de ligne en une requête sur la table sqlite_master


1 - Ecrire la requête en vous aidant de sqlitebrowser
2 - l’intégrer dans un script.

#### La liste des tables.

1. Avec le nombre d'enregistrements.
Quelle requête ?

1. le nombre d'attributs des tables attention c’est spécifique à la base, pas dans la norme SQL.


####  Mémoriser ces informations dans la base
1. Description
Voici la description de la table statdb ( nom, nbrec, nbattribut )


STATDB  3 attribut

    >    NOMTABLE 30 caracteres Nom de la table Unique non null
    >    NBLIGNE integer Nombre d’enregistrement de la table non null
    >    NBATTR integer Nombre d’attribut de la table non null

2. Création d’une table.   
Créer cette table inter-activement ou par programme.

1. Insérer des enregistrements dans la table statdb.
        soit en ne mettant que le nom de la table
        soit en remplissant toutes des colonnes

1. Mettre à jour lles informations nb record, nb attribut.   
en utilisant la commande update


#### Export des données de la base.
En utilisant le module csv
* exporter chaque table dans un fichier csv

* parallèlement créer un fichier contenant ordres sql de création des tables

#### Création d’un rapport.

En Markdown ou en html et contenant :   
* Le nom et  la taille de la base.

* Le nombre de tables.

* La liste des tables avec le nombre d’enregistrement et un lien sur la structure de celle-ci
