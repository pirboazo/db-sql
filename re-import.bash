#!/run/current-system/sw/bin/bash

sqlite3 chinook-test.db <createtable.sql

sqlite3 chinook-test.db <re-import.sql

cat res.md

