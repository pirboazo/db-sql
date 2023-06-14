#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3
import hashlib

def md5digest(t):
    return hashlib.md5(bytes(t,'utf-8')).hexdigest()


# Etablissement de la connection
DBCon= sqlite3.connect('chinook.db')

if DBCon :
    print("Connection established ..........")

DBCon.create_function("md5",1,md5digest)

ltable = DBCon.cursor()
liste = ltable.execute("select name,md5(name) from sqlite_master where name  NOT LIKE 'sqlite_%' and type= ?",['table']).fetchall()

ltable.close()


for table in liste:
    print("nom =", table[0] , "hash =", md5digest(table[0]), "md5=", table[1])


DBCon.close()

exit()
