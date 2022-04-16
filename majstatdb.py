#!/home/oboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
liste = ltable.execute("select name from sqlite_master where type= ?",['table']).fetchall()

ltable.close()

# ouvrir un curseur pour compter
MajtabCursor = DBCon.cursor()
nblinCursor=DBCon.cursor()
attrCursor=DBCon.cursor()

# print("Nom \t\t\t lignes \t attributs" )

for table in liste:
    # construire la chaine pour le select
    requetline="select count(*) from " + table[0]
    nbline=nblinCursor.execute(requetline).fetchone()
    # requetattr=('f"pragma table_info(' +table[0] +')"')
    #print(requetattr)
    attr=attrCursor.execute(f"pragma table_info('{table[0]}')").fetchall()
    #attr=attrCursor.execute(requetattr).fetchall()
    data = [nbline[0],len(attr),table[0]]
    MajtabCursor.execute("update statdb set nbligne = ? ,nbattr=? where nomtable = ? ", data)
    DBCon.commit()

nblinCursor.close()
attrCursor.close()
MajtabCursor.close()

DBCon.close()

exit()
