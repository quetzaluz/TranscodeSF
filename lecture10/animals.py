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
 
##Pretty prints a join of the animal and species tables in data.sqlite
def print_join():
    as_join = select([animals.c.id, animals.c.name, species.c.id, species.c.name, species.c.sound]).where(animals.c.species == species.c.id)
    divider = "+-----+----------------+-----+----------------+----------------+"
    print divider
    print "|a.id |     a.name     |s.id |     s.name     |     s.sound    |"
    print divider
    for row in as_join.execute():
        print "|%-5d|%-16s|%-5d|%-16s|%-16s|" % (row[0], row[1][0:15], row[2], row[3][0:15], row[4][0:15])
    print divider

class RecordError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
   
##The following function accepts animal ID numbers   
def breed(animal_1_id, animal_2_id):
    as_join = select([animals.c.id, animals.c.name, species.c.id, species.c.name, species.c.sound]).where(animals.c.species == species.c.id)
    #The following dictionaries store ID, name, species, and sound values.
    a1 = {'a_id': animal_1_id, 'a_name': None, 's_id': None, "s_name": None, 'sound': None}
    a2 = {'a_id': animal_2_id, 'a_name': None, 's_id': None, "s_name": None, 'sound': None}
    both_a = [a1, a2]
    new_a_name = None
    new_s_name = None
    new_s_id = None
    new_sound = None
    for a in both_a:
        get_vals = as_join.execute()
        for row in get_vals:
            if row[0] == a['a_id']:
                a['a_id'] = row[0]
                a['a_name'] = row[1]
                a['s_id'] = row[2]
                a['s_name'] = row[3]
                a['sound'] = row[4]
        for i in a:
            if a[i] == None:
                raise RecordError('Animal ID not found:' + str(a['a_id']))
    #Checking to see if animal1 and animal2 refer to the same value.
    if a1['a_id'] == a2['a_id']:
        new_a_name = "%s's clone" % a1['a_name']
        new_s_id = a1['s_id']
    elif a1['s_id'] == a2['s_id']:
        new_a_name = a1['a_name']+'-'+a2['a_name']
        new_s_id = a1['s_id']
    elif a1['s_id'] != a2['s_id']:
        s_list = sorted([a1['s_name'], a2['s_name']])#To try and add consistency to first generation hybrids so you won't have cow-dog-dog-cows for instance.
        new_a_name = a1['a_name']+'-'+a2['a_name']
        new_s_name = "%s-%s" % (s_list[0], s_list[1])
        pick_sound = random.random()
        if pick_sound >= 0.5:
            new_sound = a1['sound']
        elif pick_sound < 0.5:
            new_sound = a2['sound']
        new_species = species.insert().values(name=new_s_name, sound=new_sound)
        new_species.execute()
        sel1 = select([species.c.id]).where(species.c.name == new_s_name).execute()
        for row in sel1:
            new_s_id = row[0]
    else:
        print "Error error error."
    baby = animals.insert().values(name=new_a_name, species=new_s_id)
    baby.execute()

print_join()

