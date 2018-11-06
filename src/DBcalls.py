import sqlite3
from sqlite3 import Error
from DBstrings import *
from logger import logger
from APIcalls import API
from Pet import *
import os.path
#from Carbon.Aliases import false


class DataBase:
    DBstrings = DBstrings()
    def __init__(self,path="Pets.db"):
        self.conn = self.createConnection(path=path)
        DataBase.buildDatabase(self)

#++++++++++++++++ PETS +++++++++++++++++++++#
    def addPet(self,pet):
        contactid = DataBase.addContact(self,pet.contact)
        exists = self.alreadyExists("Pets", "ID", pet.id)

        if exists:
            pass
        else:
            if(pet.shelter == ""):
                shelterid = "No Shelter ID yet."
            else:
                shelterid = pet.shelterid

            with self.conn:
                cur = self.conn.cursor()
                command = "INSERT INTO Pets VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \
                        \"{6}\", \"{7}\", \"{8}\", \"{9}\", \"{10}\", \"{11}\");".format(pet.id, pet.name, pet.age, \
                        pet.animal, pet.description, pet.mix, pet.sex, pet.size,\
                        pet.breeds, pet.photoLinks, contactid, shelterid)
                #logger.detail.info(command)
                cur.execute(command)
                self.conn.commit()
                logger.detail.info("{0} has been added to database".format(pet.name))

    def getPetByID(self,id):
        result = self.getEntryByID("Pets",id)
        if result != []:
            result= result[0]
            details = list()
            for each in result:
                details.append(each)
            pet = Pet()
            pet.id = details[0]
            pet.name = details[1]
            pet.age = details[2]
            pet.animal = details[3]
            pet.description = details[4]
            pet.mix = details[5]
            pet.size = details[6]
            pet.breeds = details[7]
            pet.media = details[8]
            pet.contactId = details[9]
            pet.shelterId = details[10]
        else:
            api = API()
            pet = api.getPet(id)
            self.addPet(pet)
            
        return pet

#++++++++++++++++ CONTACTS ++++++++++++++++++++#
    def addContact(self,contact):
        exists = self.alreadyExists("Contacts", "Email", contact.email)
        if exists:
            pass
        else:
            with self.conn:
                cur= self.conn.cursor()
                command = "INSERT INTO Contacts (Phone, Email, Address, City, State, Zip) VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\");"\
                        .format(contact.phone, contact.email, contact.address, contact.city, contact.state, contact.zip)   
                cur.execute(command)
                logger.detail.info("Contact added to database.")
                cur.execute("SELECT last_insert_rowid();")
                contactid=cur.fetchall()
                contactid = contactid[0][0]
                self.conn.commit()
                return contactid

    def getContactByID(self,id):
        result = self.getEntryByID("Contacts",id)
        contact = Contact()
        if(result != []):
            result= result[0]
            details =[each for each in result]
            contact.dbID = details[0]
            contact.phone = details[1]
            contact.email = details[2]
            contact.address = details[3]
            contact.city = details[4]
            contact.state = details[5]
            contact.zip = details[6]
        else:
            pass
        return contact

#+++++++++++++++ SHELTERS +++++++++++++++++++++++#
    def addShelter(self,shelter):
        exists = self.alreadyExists("Shelters", "Email", shelter.email)
        if exists:
            pass
        else:    
            with self.conn:
                cur= self.conn.cursor()
                command = "INSERT INTO Shelters VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\",\"{9}\",\"{10}\");"\
                    .format(shelter.id, shelter.name, shelter.phone, shelter.email, shelter.address, shelter.city,\
                            shelter.state, shelter.zip, shelter.country, shelter.latitude, shelter.longitude)
                cur.execute(command)
                self.conn.commit()
                logger.detail.info("Shelter added to database.")


    def getShelterByID(self,id):
        result = self.getEntryByID("Shelters",id)
        shelter = Shelter()
        if result != []:
            result = result[0]
            details = [each for each in result]
            shelter.id = details[0]
            shelter.name = details[1]
            shelter.phone = details[2]
            shelter.email = details[3]
            shelter.address = details[4]
            shelter.city = details[5]
            shelter.state = details[6]
            shelter.zip = details[7]
            shelter.country = details[8]
            shelter.latitude = details[9]
            shelter.longitude = details[10]
        else:
            api = API()
            shelter = api.getShelter(id)
            self.addShelter(shelter)
        return shelter


#++++++++++++++++ USERS ++++++++++++++++++++++++++#
    def addUser(self,username,password,email,name):
        emailExists = self.alreadyExists("Users", "Email", email)
        usernameExists = self.alreadyExists("Users", "Username", username)
        if usernameExists or emailExists:
            return False
        else:
            with self.conn:
                cur = self.conn.cursor()
                command = "INSERT INTO Users (Username, Password, Email, Name, Favorites) \
                    VALUES (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"\");".format(username, password, email, name)
                cur.execute(command)
                self.conn.commit()
                logger.detail.info("{} added to database.".format(name))
                return True

    def login(self,username,password):
        if username == "" or password == "":
            return False
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Users WHERE Username = \"{0}\" and Password= \"{1}\";".format(username,password))
            results = cur.fetchall()
            #results
        if results != []:
            print("True")
            return True
        else:
            print("False")
            return False
        
    def addFavorite(self,username,pet):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Select Favorites from Users WHERE Username = \"{}\";".format(username))
            results = cur.fetchall()
            favorites = list(results[0])
            favorites.append(pet.id)
            faveString=""
            for id in favorites:
                if id != '':
                    faveString += id +","
            print(faveString)
            cur.execute("UPDATE Users SET Favorites=\"{}\";".format(faveString))
            self.conn.commit()
            logger.detail.info("{0} added to {1}'s favorites.".format(pet.name,username))
            
    def getFavorites(self,username):
        faves = list()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Select Favorites from Users WHERE Username = \"{}\";".format(username))
            results = cur.fetchall()
            favorites = list(results[0])
            print(favorites)
            for id in favorites:
                pet = getPet(id)
                faves.append(pet)
        return faves
    
#++++++++++++++++ BASE +++++++++++++++++++++++++++#
    def createConnection(self,path="Pets.db"):
        try:
            conn = sqlite3.connect(path, timeout=10)
            return conn
        except Error as e:
            print(e)
        return None

    def buildDatabase(self):
        #check if exists first!!
        if os.path.isfile("Pets.db"):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cur.fetchall()
                tables = [table[0] for table in tables]
                if 'Pets' in tables and 'Shelters' in tables and 'Users' in tables and 'Contacts' in tables:
                    pass
                else:
                    cur.execute(DBstrings.petTable)
                    cur.execute(DBstrings.shelterTable)
                    cur.execute(DBstrings.contactTable)
                    cur.execute(DBstrings.usersTable)
                    self.conn.commit()
                    logger.detail.info("DATABASE has been created and loaded with base tables.")

        else:
            self.createConnection()
            self.buildDatabase()
            
    def getEntryByID(self,table,id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM {0} WHERE ID = {1};".format(table,id))
            return cur.fetchall()

    
#+++++++++++++++ CLEANING ++++++++++++++++++++++#
    def dropAllTables(self):
        with self.conn:
            cur=self.conn.cursor()
            cur.execute("DROP TABLE Contacts")
            cur.execute("DROP TABLE Pets")
            cur.execute("DROP TABLE Shelters")
            cur.execute("DROP TABLE Users")
            self.conn.commit()
            logger.detail.warn("ALL TABLES DROPPED FROM Pets.db!")

    def cleanAllTables(self):
        with self.conn:
            cur=self.conn.cursor()
            cur.execute("DELETE FROM Contacts;")
            cur.execute("DELETE FROM Pets;")
            cur.execute("DELETE FROM Shelters;")
            cur.execute("DELETE FROM Users;")
            self.conn.commit()
            logger.detail.warn("ALL ROWS DELETED FROM ALL Pets.db TABLES!")

    def deleteEntry(self, table, col, value):
        with self.conn:
            cur=self.conn.cursor()
            command = "DELETE FROM {0} WHERE {1} = {2}".format(table,col,value)
            cur.execute(command)
            self.conn.commit()
            logger.detail.info("Row with {0} = {1} DELETED from {2} table.".format(col,value,table))
            
    def alreadyExists(self,table,col,value):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM {0} WHERE {1} = {2}".format(table,col,"\""+value+"\""))
            results = cur.fetchall()
        if(results == []):
            return False
        else:
            return True

