# Exploration de la création d'une base de données

Lors de l'analyse d'un projet informatique on procède à une analyse des données nécessaire au fonctionnement du projet

de cette phase d'analyse on va produire un schéma conceptuel de la structure, puis une schéma logique. c'est ce schéma logique qui est transformé en un modele physique de table stockée dans une structure physique. une [introduction](https://sqlmodel.tiangolo.com/databases/) sur le sujet.

Dans le cas de SQLite la structure physique est un fichier, dont les utilisateurs de base que nous sommes ne connaissent pas la structure, les développeurs de SQLite ont publié la desctiption de cette [structure](https://www.sqlite.org/fileformat2.html)


voici un descritptif de la base **chinook**.  Cette base comporte 11 tables.

![base chnook](sqlite-sample-database-color.jpg)

Pour nous familiariser avec la syntaxe des ordres de définition de base ( DDL ) lire l'[article](https://learnsql.fr/blog/que-sont-ddl-dml-dql-et-dcl-en-sql/)

je vous propose de recréer cette base avec des noms d'attribut en Français.

exemple :
>
> CREATE TABLE "artists"   
> (   
>     [ArtistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,   
>    [Name] NVARCHAR(120)   
> )

devient  

 CREATE TABLE artistes
  (
    [IdentifiantArtiste] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [nom] NVARCHAR(120)
  )

  
