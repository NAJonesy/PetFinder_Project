from APIcalls import API
from Pet import Pet, Shelter
from DBcalls import DataBase
from pathlib import Path
from logger import logger
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
    chewyShelter = Shelter(json=shelterData['petfinder']['shelter'])
    petData = petData['petfinder']['pet']
    chewy = Pet(petData, shelter=chewyShelter)
    return chewy

# +++++++++++++++++++++++++++++ Testing Variables +++++++++++++++++++++++++++++++++ #
chewy = makeChewy()
testConnection = API()
testDB = DataBase(path='PetTesting.db')
testPet = Pet()
testShelter = Shelter()

# ++++++++++++++++++++++++++++ API TESTS +++++++++++++++++++++++++++++++++++++++++++ #
def getBreedsTest():
    logger.detail.debug("getBreedsTest has started")
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
    with testDB.conn:
        cur= testDB.conn.cursor()
        cur.execute("Select * from Pets where Name = \"Chewbacca\"")
        results = cur.fetchall()
    if(results != []):
        pet = results[0]
        assert str(pet[0]) == str(chewy.id), "testPet ID data does not match Chewy. Database: {}".format(pet[0])
        assert pet[1] == "Chewbacca", "testPet name does not match Chewy. Database: {}".format(pet[1])
    else:
        logger.detail.warning("No results coming from Pets table in database.")
   
def addShelterToDataBaseTest():
    testDB.addShelter(chewy.shelter)
    with testDB.conn:
        cur= testDB.conn.cursor()
        cur.execute("Select * from Shelters where City = \"Kettering\"")
        results = cur.fetchall()
    if(results != []):
        shelter = results[0]
        assert str(shelter[0]) == str(chewy.shelter.id), "testShelter ID data does not match ChewyShelter. Database: {}".format(shelter[0])
        assert shelter[1] == "Paw Patrol", "testShelter name data does not match ChewyShelter."
    else:
        logger.detail.warning("No results coming from Shelters table in database.")

def addUserToDataBaseTest():
    testDB.addUser("test","test","test@test.com", "test admin")
    with testDB.conn:
        cur= testDB.conn.cursor()
        cur.execute("Select * from Users where Username = \"test\"")
        results = cur.fetchall()
    if(results != []):
        user = results[0]
        assert user[1] == "test", "User username data does not match test credentials."
        assert user[2] == "test", "User password data does not match test credentials."
        assert user[3] == "test@test.com", "User email data does not match test credentials."
    else:
        logger.detail.warning("No results coming from Users table in database.")

def loginTest():
    result = testDB.login("test","test")
    assert result == True, "Login does not work properly."

def getEntryFromTableTests():
    pass

def addFavoriteTest():
    testDB.addFavorite("test",chewy)
    with testDB.conn:
        cur = testDB.conn.cursor()
        cur.execute("SELECT * FROM Users WHERE Username = \"test\"")
        results = cur.fetchall()
    favorites = list(str(results[0][5]).split(","))
    assert chewy.id in favorites, "Pet ID not being added to favorites."

def deleteEntryTest():
    testDB.deleteEntry("Pets", "ID", chewy.id)
    with testDB.conn:
        cur = testDB.conn.cursor()
        cur.execute("SELECT * FROM Pets WHERE ID = {}".format(chewy.id))
        results = cur.fetchall()
    assert results == [], "Delete Entry is not working correctly."

def tableCleaningTest():
    testDB.cleanAllTables()
    with testDB.conn:
        cur = testDB.conn.cursor()
        cur.execute("Select * from Pets")
        petRows = cur.fetchall()
        cur.execute("select * from Shelters")
        shelterRows = cur.fetchall()
        
    assert petRows == [], "Pets table rows are not being deleted."
    assert shelterRows == [], "Shelters table rows are not being deleted."

def tableDroppingTest():
    testDB.dropAllTables()
    pass

def DataBaseTests():
    createDataBaseTest()
    addPetToDataBaseTest()
    addShelterToDataBaseTest()
    addUserToDataBaseTest()
    loginTest()
    getEntryFromTableTests()
    addFavoriteTest()
    deleteEntryTest()
    tableCleaningTest()
    tableDroppingTest()

# ++++++++++++++++++++++++++++++ MAIN +++++++++++++++++++++++++++++++++++++++++++++#

def main():    
    APItests()
    DataBaseTests()

if __name__ == "__main__":
    main()
