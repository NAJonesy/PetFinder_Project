import json
from Pet import *


def outputJSON():
    pass

def createFavoritesFile():
    pass

def createSheltersNearMeFile():
    pass

def singlePetToJSON(pet):
    outline = {"PetFinder":{
                "Pet":{\
                       "ID":pet.id,\
                       "Name":pet.name,\
                       "":x,\
                       "":x,\
                       "":x,\
                       "":x,\
                       "":x,\
                       
                    }}}
    petInfo = {"ID":pet.id,"Name":pet.name}
    
    stringInfo = "{\"PetFinder\":{\"Pet\":{{0}}}}".format(petInfo)
    
    print(stringInfo)
    
    output = json.dump({"PetFinder":{"Pet":{{0}}}})
    return output

def petListJSON(petList):
    pass

