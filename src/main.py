from APIcalls import API
from Pet import Pet, Shelter
from logger import logger


def main():
    myConnection = API()

    # results = myConnection.getBreeds("cat")
    # #myConnection.getRandom()

#++++++++++++++++++++
    # print(results)
    #myPet = Pet(myConnection.getRandom())
    #print(myPet.contact.getMailingAddress())
    pets = myConnection.getFindPet('80005')

    #myPet = Pet(results)
    #petList = myConnection.getFindPet("80005")
    #print(petList[0].breeds)
    #pet = petList[0].getShelter()
    #print(pet.shelter)
#+++++++++++++++++++
    #shelterJson = 
    myShelter = myConnection.getShelter('CO445')
    #print(myShelter.email)
    #print(logger.detail)
    #logger.note.debug("testing")
    #logger.detail.debug("detail testing")

if __name__ == "__main__":
    main()
