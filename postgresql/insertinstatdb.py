#!/home/oboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import psycopg2

DBCon = None

# Etablissement de la connection
try:
    DBCon = psycopg2.connect(database="chinook", user="chinook", password="chinook", host="192.168.10.84", port="5432")
    print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
# retrouver la liste des tables
    ltable = DBCon.cursor()
    ltable.execute("select table_name from information_schema.tables where table_schema='public'")
    liste = ltable.fetchall()

    # delete des ligne de statdb.
    ltable.execute("delete from statdb")
    DBCon.commit()

    ltable.close()

# ouvrir un curseur pour compter
    MajtabCursor = DBCon.cursor()
    nblinCursor=DBCon.cursor()
    attrCursor=DBCon.cursor()

# print("Nom \t\t\t lignes \t attributs" )

    for table in liste:
        # construire la chaine pour le select
        requetline="select count(*) from " + table[0]
        nblinCursor.execute(requetline)
        nbline=nblinCursor.fetchone()
    # requetattr=('f"pragma table_info(' +table[0] +')"')
    #    print("1")
        attrCursor.execute("select count(*) from information_schema.columns where table_name=%s",(table[0],))
        attr=attrCursor.fetchall()
    #    print("2")
    #attr=attrCursor.execute(requetattr).fetchall()
        data = [table[0],nbline[0],attr[0]]
        MajtabCursor.execute("insert into statdb (nomtable,nbligne,nbattr) values (%s, %s, %s)", data)
    #    print("3")
        DBCon.commit()

    nblinCursor.close()
    attrCursor.close()
    MajtabCursor.close()

    if DBCon is not None:
        DBCon.close()
        print('Database connection closed.')

except (Exception, psycopg2.DatabaseError) as error:
        print("error de connection")
        print(error)

exit()
