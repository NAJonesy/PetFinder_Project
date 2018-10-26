from logger import logger
#from pathlib import Path
import json

def getJsonAttribute(json, attribute):
        if attribute in dict(json):
            try:
                if(json[attribute] != {}):
                    return json[attribute]['$t']
                elif(attribute == 'description'):
                    return "No description available."
                elif(attribute == 'address1'):
                        return "No street address on file."
                else:
                    logger.detail.info("Missing attribute: {0}\n{1}".format(attribute, json))
                    return "No value given."    
            except KeyError as e:
                logger.detail.critical("JSON KEY ERROR!\nEntered key: {0}\n{1}".format(e,json))
            except Exception as x:
                logger.detail.critical("JSON KEY ERROR! See common.py\nError Code: {}".format(x))
        else:
            logger.detail.warning("Attribute '{0}' not found in JSON.\n{1}".format(attribute,json))

def getMailingAddress(address,city,state,zip):
        if(address != "No value given."):
            address = address + "\n"
        if(city != "No value given."):
            city = city +", "
        if(state != "No value given."):
            state = state + " "
        if(zip != "No value given."):
            zip = zip

        if(address == "" and city =="" and state =="" and zip == ""):
            return "No mailing address available."
        else:
            return address + city + state  + zip
