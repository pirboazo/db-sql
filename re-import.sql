
.output import-csv-all.sql
.read "pre-import-csv.sql"         
.read "import-csv-all.sql"
.output res.md
.mode markdown
select * from statdb ;
