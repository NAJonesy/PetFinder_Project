from APIcalls import *
from Pet import *
import json
import requests
from DBcalls import DataBase

conn = DataBase()
#conn = dbConnect.createConnection('./pets.db')

api = API()
pet = api.getRandomPet()
petID = pet.id
conn.addPet(pet)
conn.getPetByID(petID)
conn.dropAllTables()
    #cur.execute(".tables")
#     cur.execute("ALTER TABLE Pets")
