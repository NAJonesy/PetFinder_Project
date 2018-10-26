from APIcalls import API
from Pet import Pet, Shelter
from DBcalls import DataBase
from pathlib import Path
import json
import os.path


#Chewy is built from local json files (collected from PetFinder) and does not call the PetFinder API 
def makeChewy():
    script_location = Path(__file__).absolute().parent
    chewyFile = script_location / 'Chewbacca.json'
    chewyShelterFile = script_location / 'ChewyShelter.json'
    with open(chewyFile) as json_file:
        petData = json.load(json_file)
    with open(chewyShelterFile) as json_file:
        shelterData = json.load(json_file)
    chewy = Pet(petData['petfinder']['pet'], shelter=Shelter(json=shelterData))
    return chewy

# +++++++++++++++++++++++++++++ Testing Variables +++++++++++++++++++++++++++++++++ #
chewy = makeChewy()
testConnection = API()
testDB = DataBase(path='petTesting.db')
testPet = Pet()
testShelter = Shelter()

# ++++++++++++++++++++++++++++ API TESTS +++++++++++++++++++++++++++++++++++++++++++ #
def getBreedsTest():
    response = testConnection.getBreeds("dog")
    assert "Collie" in response, "APIcalls 'getBreeds' error."

def APItests():
    petTests()
    getBreedsTest()
    shelterTests()

# ++++++++++++++++++++++++++++ PET TESTS +++++++++++++++++++++++++++++++++++++++++++ #
def getPetTest():
    testid = 42967158
    testPet = testConnection.getPet(testid)
    assert int(testPet.id) == testid, "APIcalls 'getPet' error."

def getRandomTest():
    randomAnimal = testConnection.getRandomPet()
    assert randomAnimal.name != "", "APIcalls 'getRandom' error."

def setPetVariablesTest():
    results = testConnection.setPetVariables(age='12',animal='dog',location='80005')
    assert 'animal' in results, "APIcalls 'setPetVariables' or 'checkDictionary' error. Missing 'animal' key."
    assert 'age' in results, "APIcalls 'setPetVariables' or 'checkDictionary' error. Missing 'age' key."
    assert 'location' in results, "APIcalls 'setPetVariables' or 'checkDictionary' error. Missing 'location' key."
    assert 'offset' not in results, "APIcalls 'checkDictionary' error. Not removing empty variables."

def petContactTest():
    testContact = chewy.contact
    assert testContact.email == "adoptions@pawpatroldayton.com", "Contact attribute EMAIL is not loading properly. Value loaded: {}".format(testContact.email)
    assert testContact.zip == "45429", "Contact attribute ZIP is not loading properly. Value loaded: {}".format(testContact.zip)


def petTests():
    getRandomTest()
    getPetTest()
    setPetVariablesTest()
    petContactTest()


# ++++++++++++++++++++++++++++ SHELTER TESTS +++++++++++++++++++++++++++++++++++++++#
def getFindShelterTest():
    variables={'location': '80005'}
    ShelterList = testConnection.getFindShelter(variables)
    assert type(ShelterList[0]) is Shelter, "APIcalls 'getFindShelter' error."

def getShelterTest():
    shelterid = 'CO115'
    testShelter = testConnection.getShelter(shelterid)
    assert type(testShelter) is Shelter, "APIcalls 'getShelter' error."

def setShelterVariablesTest():
    results = testConnection.setShelterVariables(location='80005', name='Leroy Jenkins')
    assert 'name' in results, "APIcalls 'setShelterVariables' or 'checkDictionary' error. Missing 'name' key."
    assert 'location' in results, "APIcalls 'setShelterVariables' or 'checkDictionary' error. Missing 'location' key."
    assert 'offset' not in results, "APIcalls 'checkDictionary' error. Not removing empty variables."

def setPetShelterTest():
    testPet = makeChewy()
    testShelter = testPet.shelter
    assert testShelter.id == "OH1158", "Shelter attribute ID is not loading properly. Value given: {}".format(testShelter.id)
    assert testShelter.name == "Paw Patrol", "Shelter attribute NAME is not loading properly. Value given: {}".format(testShelter.id)


def shelterTests():
    getFindShelterTest()
    getShelterTest()
    setShelterVariablesTest()
    setPetShelterTest()

# ++++++++++++++++++++++++++++++ DATABASE +++++++++++++++++++++++++++++++++++++++++#
testingConnection = testDB.conn 
testingCursor = testingConnection.cursor()
def createDataBaseTest():
    tables = []
    exists = os.path.isfile('petTesting.db') 
    assert exists, "The database is not being created."
    with testingConnection:
        testingCursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        results = testingCursor.fetchall()
        for table in results:
            tables.append(table[0])
    assert "Pets" in tables,"Pets table is not being created."
    assert "Shelters" in tables,"Shelters table is not being created."
    assert "Users" in tables, "Users table is not being created."
    assert "Contacts" in tables, "Contacts table is not being created."




def addPetToDataBaseTest():
    testDB.addPet(chewy)
    pass
def addShelterToDataBaseTest():
    testDB.addShelter(chewy.shelter)
    pass
def addUserToDataBaseTest():
    pass

def loginTest():
    pass

def getEntryFromTableTests():
    pass

def tableCleaningTest():
    pass

def tableDroppingTest():
    pass

def DataBaseTests():
    createDataBaseTest()
    addPetToDataBaseTest()
    addShelterToDataBaseTest()
    addUserToDataBaseTest()
    loginTest()
    getEntryFromTableTests()
    tableCleaningTest()
    tableDroppingTest()

# ++++++++++++++++++++++++++++++ MAIN +++++++++++++++++++++++++++++++++++++++++++++#

def main():    
    #APItests()
    DataBaseTests()

if __name__ == "__main__":
    main()
