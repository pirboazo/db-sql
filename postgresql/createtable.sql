CREATE TABLE "artists"
(
    ArtistId SERIAL PRIMARY KEY  NOT NULL,
    Name VARCHAR(120)
)
;
CREATE TABLE "albums"
(
    AlbumId SERIAL PRIMARY KEY  NOT NULL,
    Title VARCHAR(160)  NOT NULL,
    ArtistId INTEGER  NOT NULL,
    FOREIGN KEY (ArtistId) REFERENCES "artists" (ArtistId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;
CREATE TABLE "employees"
(
    EmployeeId SERIAL PRIMARY KEY  NOT NULL,
    LastName VARCHAR(20)  NOT NULL,
    FirstName VARCHAR(20)  NOT NULL,
    Title VARCHAR(30),
    ReportsTo INTEGER,
    BirthDate timestamp,
    HireDate timestamp,
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60),
    FOREIGN KEY (ReportsTo) REFERENCES "employees" (EmployeeId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;
CREATE TABLE "customers"
(
    CustomerId SERIAL PRIMARY KEY  NOT NULL,
    FirstName VARCHAR(40)  NOT NULL,
    LastName VARCHAR(20)  NOT NULL,
    Company VARCHAR(80),
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60)  NOT NULL,
    SupportRepId INTEGER,
    FOREIGN KEY (SupportRepId) REFERENCES "employees" (EmployeeId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;

CREATE TABLE "genres"
(
    GenreId SERIAL PRIMARY KEY  NOT NULL,
    Name VARCHAR(120)
)
;
CREATE TABLE "invoices"
(
    InvoiceId SERIAL PRIMARY KEY  NOT NULL,
    CustomerId INTEGER  NOT NULL,
    InvoiceDate timestamp  NOT NULL,
    BillingAddress VARCHAR(70),
    BillingCity VARCHAR(40),
    BillingState VARCHAR(40),
    BillingCountry VARCHAR(40),
    BillingPostalCode VARCHAR(10),
    Total NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES "customers" (CustomerId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;

CREATE TABLE "media_types"
(
    MediaTypeId SERIAL PRIMARY KEY  NOT NULL,
    Name VARCHAR(120)
)
;
CREATE TABLE "playlists"
(
    PlaylistId SERIAL PRIMARY KEY  NOT NULL,
    Name VARCHAR(120)
)
;

CREATE TABLE "tracks"
(
    TrackId SERIAL PRIMARY KEY  NOT NULL,
    Name VARCHAR(200)  NOT NULL,
    AlbumId INTEGER,
    MediaTypeId INTEGER  NOT NULL,
    GenreId INTEGER,
    Composer VARCHAR(220),
    Milliseconds INTEGER  NOT NULL,
    Bytes INTEGER,
    UnitPrice NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY (AlbumId) REFERENCES "albums" (AlbumId)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (GenreId) REFERENCES "genres" (GenreId)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (MediaTypeId) REFERENCES "media_types" (MediaTypeId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;
CREATE TABLE "playlist_track"
(
    PlaylistId INTEGER  NOT NULL,
    TrackId INTEGER  NOT NULL,
    CONSTRAINT PK_PlaylistTrack PRIMARY KEY  (PlaylistId, TrackId),
    FOREIGN KEY (PlaylistId) REFERENCES "playlists" (PlaylistId)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (TrackId) REFERENCES "tracks" (TrackId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;

CREATE TABLE "invoice_items"
(
    InvoiceLineId SERIAL PRIMARY KEY  NOT NULL,
    InvoiceId INTEGER  NOT NULL,
    TrackId INTEGER  NOT NULL,
    UnitPrice NUMERIC(10,2)  NOT NULL,
    Quantity INTEGER  NOT NULL,
    FOREIGN KEY (InvoiceId) REFERENCES "invoices" (InvoiceId)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (TrackId) REFERENCES "tracks" (TrackId)
		ON DELETE NO ACTION ON UPDATE NO ACTION
)
;
CREATE TABLE statdb (nomtable text not NULL unique, nbligne integer not null, nbattr integer )
;
