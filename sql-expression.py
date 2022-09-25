from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our local host "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)
# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title",String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Create variable for "Track" table
track_table = Table(
    "Track", meta
)

# making the connection
with db.connect() as connection:
