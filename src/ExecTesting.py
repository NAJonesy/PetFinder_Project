from APIcalls import *
from Pet import *
import json
import requests
from DBcalls import DataBase
from Outputs import *
from pathlib import Path


#Chewy the test pet :)

def makeChewy():
    script_location = Path(__file__).absolute().parent
    chewyFile = script_location / 'Chewbacca.json'
    chewyShelterFile = script_location / 'ChewyShelter.json'
    with open(chewyFile) as json_file:
        petData = json.load(json_file)
    with open(chewyShelterFile) as json_file:
        shelterData = json.load(json_file)
    chewyShelter = Shelter(json=shelterData['petfinder']['shelter'])
    petData = petData['petfinder']['pet']
    chewy = Pet(petData, shelter=chewyShelter)
    return chewy

chewy = makeChewy()

singlePetToJSON(chewy)