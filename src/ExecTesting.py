from APIcalls import *
from Pet import *
import json
import requests
from DBcalls import DataBase

#Chewy the test pet :)

#chewy = Pet(Chewbacca.Json)

conn = DataBase()
#conn = dbConnect.createConnection('./pets.db')

with conn.conn:
    cur = conn.conn.cursor()
    cur.execute("Select * from Pets")
    rows = cur.fetchall()
    print(rows)
    
conn.cleanAllTables()
api = API()
#randomPet = api.getRandomPet()
#breeds=api.getBreeds("dog")
#print(breeds)
#pet = api.getRandomPet()
# petID = pet.id
# conn.addPet(pet)
# conn.getPetByID(petID)
# conn.dropAllTables()
    #cur.execute(".tables")s
#     cur.execute("ALTER TABLE Pets")
