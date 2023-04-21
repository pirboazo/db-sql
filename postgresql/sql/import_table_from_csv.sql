
-- commande d'intégration de fichier CSV dans Postgresql.

\copy artists from 'csv/artists_data.csv' DELIMITER ',' CSV HEADER;
\copy albums from 'csv/albums_data.csv' DELIMITER ',' CSV HEADER;
\copy genres from 'csv/genres_data.csv' DELIMITER ',' CSV HEADER;
\copy media_types from 'csv/media_types_data.csv' DELIMITER ',' CSV HEADER;
\copy tracks from 'csv/tracks_data.csv' DELIMITER ',' CSV HEADER;
\copy playlists from 'csv/playlists_data.csv' DELIMITER ',' CSV HEADER;
\copy playlist_track from 'csv/playlist_track_data.csv' DELIMITER ',' CSV HEADER;
\copy employees from 'csv/employees_data.csv' DELIMITER ',' CSV HEADER;
\copy customers from 'csv/customers_data.csv' DELIMITER ',' CSV HEADER;
\copy invoices from 'csv/invoices_data.csv' DELIMITER ',' CSV HEADER;
\copy invoice_items from 'csv/invoice_items_data.csv' DELIMITER ',' CSV HEADER;

\q
