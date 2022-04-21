#
#  exemple de select pour générer l'ensemble des ordre d'import csv
#
select ".import --csv --skip 1 "||"'csv/"||name||"_data.csv'"||" "||name from sqlite_master where type="table";
