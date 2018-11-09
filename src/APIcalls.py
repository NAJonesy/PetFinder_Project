import requests
import json
from Pet import Pet, Shelter
from logger import logger

    ## TO DO: Documentation, make polymorphic ##

class API():
#+++++++++++++++++++++++++ Breeds ++++++++++++++++++++++++++++#
    '''
        Method: getBreeds
        Purpose: Get a list of breeds for a certain animal
        Inputs: animal (String)
        Returns: String[]
    '''
    def getBreeds(self, animal):
        json = API.getJson(self,'breed.list',{'animal':animal})
        breedList = json["breeds"]["breed"]
        results = []
        for entry in breedList:
            results.append(entry["$t"])
        return results


#++++++++++++++++++++++++++++ PET +++++++++++++++++++++++++++#
    '''
        Method: getPet
        Purpose: Get information about a pet from a given id. Then make it into a pet object.
        Inputs: id (int)
        Returns: pet (object)
    '''
    def getPet(self, id):
        json = API.getJson(self,'pet.get',{'id':id})
        pet = ''
        if 'pet' in json:
            pet = Pet(json=json['pet'])
        else:
            logger.detail.warning("No 'pet' in returned json.\n{0}".format(json))
        return pet

    '''
        Method: getRandomPet
        Purpose: Find information about a random pet. Search criteria optional.
        Inputs: Dictionary of possible search requirements
        Returns: pet (object)
    '''
    def getRandomPet(self,variables={"output":"full"}):
        variables['output'] = 'full'
        json = API.getJson(self,'pet.getRandom',variables)
        pet = ''
        if 'pet' in json:
            pet = Pet(json=json['pet'])
        else:
            logger.detail.warning("No 'pet' in returned json.\n{0}".format(json))
        return pet

    '''
        Method: getFindPet
        Purpose: Get a list of pets based on optional search criteria
        Inputs: Dictionary of optional search requirements
        Returns: list of pets <list(object)>
    '''
    def getFindPet(self,variables={}):
        petList = []
        if 'location' in variables and 'shelterid' not in variables:
            json = API.getJson(self,'pet.find',variables)
            pets = json["pets"]
            for pet in pets["pet"]:
                tempShelter = API.getShelter(self,pet['shelterId']['$t'])
                temp = Pet(json=pet,shelter = tempShelter)
                petList.append(temp)
        else:
            if 'location' not in variables:
                logger.detail.warning("No location passed to getFindPet")
            if 'shelterid' in variables:
                logger.detail.warning("Shelterid passed to getFindPet")
        return petList



#++++++++++++++++++++++++++ SHELTERS +++++++++++++++++++++++++++#
    '''
        Method: getFindShelter
        Purpose:  Get a list of shelters based on optional search criteria
        Inputs: Dictionary of optional search criteria
        Returns: list of shelters <list(object)>
    '''
    def getFindShelter(self,variables={}):
        shelterList = []
        json = API.getJson(self,'shelter.find',variables)
        jsonShelters = json['shelters']
        for shelter in jsonShelters['shelter']:
            temp = Shelter(shelter)
            shelterList.append(temp)
        return shelterList

    '''
        Method: getShelter
        Purpose: Get information about a shelter based on given shelter id
        Inputs: shelterid (int)
        Returns: shelter (object)
    '''
    def getShelter(self,id):
        json = API.getJson(self,'shelter.get',{'id':id})
        shelter = Shelter(json['shelter'])
        return shelter

    '''
        Method: setPetShelter
        Purpose: Attach a shelter object to an existing pet object. 
        Inputs: pet (object), shelter (object)
        Returns: Nothing.
    '''
    def setPetShelter(self,pet,shelter):
        pet.setShelter(pet,shelter)

#+++++++++++++++++++ Base +++++++++++++++++++++#
    '''
        Method: setPetVariables
        Purpose: Fill dictionary with optional search criteria for pets
        Inputs: Strings with variable name
        Returns: dictionary of search parameters
    '''
    def setPetVariables(self,animal='',breed='',size='', sex='',location='',shelterId='',output ='',count='',age='',offset=''):
        varDict = {
            'age': age,
            'animal': animal,
            'breed': breed,
            'count': count,
            'location': location,
            'offset': offset,
            'output': output,
            'size': size,
            'sex': sex,
            'shelterid': shelterId

        }
        return API.checkDictionary(self,varDict)
    
    '''
        Method: setShelterVariables
        Purpose: fill dictionary with optional search criteria for shelters
        Inputs: Strings with variable name
        Returns: dictionary of search parameters
    '''
    def setShelterVariables(self,location='',name='',count='',offset=''):
        varDict ={
            'count': count,
            'location': location,
            'name': name,
            'offset': offset
        }
        return API.checkDictionary(self,varDict)
    
    '''
        Method: checkDictionary
        Purpose: Parses the optional search criteria dictionaries and removes unused parameters
        Inputs: dictionary
        Returns: dictionary
    '''
    def checkDictionary(self,dict):
        badKeys = list()
        for key, value in dict.items():
            if value == '':
                badKeys.append(key)
        for key in badKeys:
            del dict[key]
        return dict
    
    '''
        Method: getJson
        Purpose: Gets a Json response from the api and adds in optional parameters
        Inputs: api (object), dictionary
        Returns: JSON
    '''
    def getJson(self,api,variables={}):
        key = "60565187dd6a139dcfbda7c1743e62d4"
        URL = 'http://api.petfinder.com/{0}?key={1}'.format(api, key)
        for value in variables:
            URL += '&{0}={1}'.format(value, variables[value])
        URL += '&format=json'
        logger.detail.info("Calling API @: {}".format(URL))
        try:
            response = requests.get(URL) 
            if(response.status_code == 200):
                js = response.json()
                return js["petfinder"]
            else:
                logger.detail.warning("Response error. Status: "+response.status_code)
        except Exception as e:
            logger.detail.warning("API call error. Code: {0}".format(e))
        

