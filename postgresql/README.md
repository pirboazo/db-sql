# DB-sql **PostgreSQL**



Quelques explications sur les différences entre **sqlite** et **PostgreSQL**.

## Au programme

1. L'organisation globale.
  1. fichier versus service
  2. SQL presque le même.
  2. la gestion d'utilisateur, la sécurité

2. Que faire pour mettre en route un serveur **PostgreSQL**
  1. installer le service ( cluster )
  2. créer une base dans le cluster.
  2. configurer la cluster ( postgresql.conf,  ... )
  2. créer un utilisateur dans le cluster.
    1. > create user chinook password 'chinook' createdb CREATErole superuser;
    1. > create database chinook;


  2. Autoriser cet utilisateur à ce connecter à la base.
    1.  pg_hba.conf

2. l'accés au Données
  1. en mode cli :
  > pgsql -U chinook chinook
  1. en python. drivers psycopg2
    1. Installation :
  > https://www.psycopg.org/docs/install.html
  >
  > pip | pipenv install psycopg2-binary
    2.
