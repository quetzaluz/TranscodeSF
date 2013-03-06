from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy import create_engine
from sqlalchemy import select
import random

db = MetaData()
db.bind=create_engine('sqlite:///data.sqlite')

animals = Table("animals", db,
 Column("id", Integer, primary_key=True),
 Column("name", String),
 Column("species", None, ForeignKey("species.id")))

species = Table("species", db,
 Column("id", Integer, primary_key=True),
 Column("name", String),
 Column("sound", String))

db.create_all()
