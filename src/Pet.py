from common import getJsonAttribute, getMailingAddress
from logger import logger

#TO DO: HANDLE no pet in JSON error
class Pet:
    def __init__(self,json = "",shelter = ""):
        if(json != ""):
            self.animal = getJsonAttribute(json,"animal")
            self.age = getJsonAttribute(json,"age")
            self.contact = Contact(json["contact"])
            self.description = getJsonAttribute(json,"description")   
            self.id = getJsonAttribute(json,"id")
            self.mix = getJsonAttribute(json,"mix") 
            self.sex = getJsonAttribute(json,"sex")
            self.shelterid = getJsonAttribute(json,"shelterId")
            self.size = getJsonAttribute(json,"size")
        # ++++ NAME FILTERING +++ #
            self.name = getJsonAttribute(json,"name")
            self.name = self.name.replace(" - courtesy listing","")
            self.name = self.name.replace(" - Courtesy Listing","")
        # ++++ BREEDS +++++ #
            self.breeds=[]
            breedsJson = json["breeds"]["breed"]
            if(type(breedsJson) is dict):
               self.breeds.append(breedsJson["$t"])
            elif(type(breedsJson) is list):
                for breed in breedsJson:
                    self.breeds.append(breed["$t"])
        # ++++++++ MEDIA(photos) +++++++++++++++++++#
            self.photoLinks = []
            
            if json["media"] != {}:
                mediaJson = json["media"]["photos"]
                if mediaJson != {}:
                    if(type(mediaJson) is dict):
                        pass
                    if(type(mediaJson) is list):
                        for photo in mediaJson:
                            self.photoLinks.append(photo["$t"])
                else:
                    self.photoLinks.append("No photos available.")
            else:
                self.photoLinks.append("No photos available.")
 
        else:
            logger.detail.warning("Empty pet created. No JSON.")
        # +++++++++++ SHELTER ++++++++++++++ #  
        self.shelter = "" 
        if(shelter != ""):
            self.shelter = shelter


    # shelter separated to limit API calls #
    def setShelter(self,shelter):
        self.shelter = shelter
        return self


class Shelter:
    def __init__(self,json=""):  
        if(json != ""): 
            self.address = getJsonAttribute(json,"address1")
            self.city = getJsonAttribute(json,"city")
            self.country = getJsonAttribute(json,"country")
            self.email = getJsonAttribute(json, "email")
            self.id = getJsonAttribute(json,"id")
            self.latitude = getJsonAttribute(json,"latitude")
            self.longitude = getJsonAttribute(json,"longitude")
            self.name = getJsonAttribute(json,"name")
            self.phone = getJsonAttribute(json,"phone")
            self.state = getJsonAttribute(json,"state")
            self.zip = getJsonAttribute(json,"zip")
        else:
            logger.detail.warning("Empty shelter created. No JSON.")        
        
class Contact:
    def __init__(self,json=""):
        if(json!=""):
            self.phone = getJsonAttribute(json,"phone")
            self.state = getJsonAttribute(json,"state")
            self.email = getJsonAttribute(json,"email")
            self.city = getJsonAttribute(json,"city")
            self.zip = getJsonAttribute(json,"zip")
            self.address = getJsonAttribute(json,"address1")
        else:
            logger.detail.warning("Empty contact created. No JSON.")

    def printAddress(self):
        return getMailingAddress(self.address,self.city,self.state,self.zip)
   
