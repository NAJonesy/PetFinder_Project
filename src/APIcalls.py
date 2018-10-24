import requests
import json
from Pet import Pet, Shelter
from logger import logger

    ## TO DO: Documentation, make polymorphic ##

class API():
#+++++++++++++++++++++++++ Breeds ++++++++++++++++++++++++++++#
    def getBreeds(self, animal):
        json = API.getJson(self,'breed.list',{'animal':animal})
        breedList = json["breeds"]["breed"]
        results = []
        for entry in breedList:
            results.append(entry["$t"])
        return results


#++++++++++++++++++++++++++++ PET +++++++++++++++++++++++++++#
    def getPet(self, id):
        json = API.getJson(self,'pet.get',{'id':id})
        pet = ''
        if 'pet' in json:
            pet = Pet(json=json['pet'])
        else:
            logger.detail.warning("No 'pet' in returned json.\n{0}".format(json))
        return pet

    
    def getRandomPet(self,variables={}):
        json = API.getJson(self,'pet.getRandom',variables)
        id = json["petIds"]["id"]["$t"]
        pet = API.getPet(self,id)
        return pet


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
    def getFindShelter(self,variables={}):
        shelterList = []
        json = API.getJson(self,'shelter.find',variables)
        jsonShelters = json['shelters']
        for shelter in jsonShelters['shelter']:
            temp = Shelter(shelter)
            shelterList.append(temp)
        return shelterList


    def getShelter(self,id):
        json = API.getJson(self,'shelter.get',{'id':id})
        shelter = Shelter(json['shelter'])
        return shelter


    def setPetShelter(self,pet,shelter):
        pet.setShelter(pet,shelter)

#+++++++++++++++++++ Base +++++++++++++++++++++#

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

    def setShelterVariables(self,location='',name='',count='',offset=''):
        varDict ={
            'count': count,
            'location': location,
            'name': name,
            'offset': offset
        }
        return API.checkDictionary(self,varDict)

    def checkDictionary(self,dict):
        badKeys = list()
        for key, value in dict.items():
            if value == '':
                badKeys.append(key)
        for key in badKeys:
            del dict[key]
        return dict

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
        

