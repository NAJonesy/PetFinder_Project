from APIcalls import API
from Pet import Pet, Shelter
from DBcalls import DataBase

testConnection = API()
testDB = DataBase('petTesting.db')
testPet = Pet()
testShelter = Shelter()

# ++++++++++++++++++++++++++++ API TESTS +++++++++++++++++++++++++++++++++++++++++++#
def getBreedsTest():
    response = testConnection.getBreeds("dog")
    assert "Collie" in response, "APIcalls 'getBreeds' error."

def APItests():
    petTests()
    getBreedsTest()
    shelterTests()

# ++++++++++++++++++++++++++++ PET TESTS +++++++++++++++++++++++++++++++++++++++++++#
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
    pass

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
    pass

def shelterTests():
    getFindShelterTest()
    getShelterTest()
    setShelterVariablesTest()
    setPetShelterTest()

# ++++++++++++++++++++++++++++++ DATABASE +++++++++++++++++++++++++++++++++++++++++#
def createDataBaseTest():
    pass

def addPetToDataBaseTest():
    pass

def addShelterToDataBaseTest():
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
    APItests()
    DataBaseTests()

if __name__ == "__main__":
    main()
