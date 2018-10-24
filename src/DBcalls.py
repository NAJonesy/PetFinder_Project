import sqlite3
from sqlite3 import Error
from DBstrings import *
from logger import *
from APIcalls import API


#TO DO: Add favorites, DBtests, 
class DataBase:
    DBstrings = DBstrings()
    def __init__(self,path="Pets.db"):
        self.conn = self.createConnection(path=path)
        DataBase.buildDatabase(self)

#++++++++++++++++ PETS +++++++++++++++++++++#
    def addPet(self,pet):
        contactid = DataBase.addContact(self,pet.contact)
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
            logger.detail.info(command)
            cur.execute(command)
            logger.detail.info("{0} has been added to database".format(pet.name))

    def getPetByID(self,id):
        return self.getEntryByID("Pets",id)   

#++++++++++++++++ CONTACTS ++++++++++++++++++++#
    def addContact(self,contact):
        with self.conn:
            cur= self.conn.cursor()
            command = "INSERT INTO Contacts (Phone, Email, Address, City, State, Zip) VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\");"\
                        .format(contact.phone, contact.email, contact.address, contact.city, contact.state, contact.zip)                                   
            cur.execute(command)
            logger.detail.info("Contact added to database.")
            cur.execute("SELECT last_insert_rowid();")
            contactid=cur.fetchall()
            contactid = contactid[0][0]
            return contactid

    def getContactByID(self,id):
        return self.getEntryByID("Contacts",id)

#+++++++++++++++ SHELTERS +++++++++++++++++++++++#
    def addShelter(self,shelter):
        with self.conn:
            cur= self.conn.cursor()
            command = "INSERT INTO Shelters VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\",\"{9}\",\"{10}\");"\
                .format(shelter.id, shelter.name, shelter.phone, shelter.email, shelter.address, shelter.city,\
                shelter.state, shelter.zip, shelter.country, shelter.latitude, shelter.longitude)
            cur.execute(command)
            logger.detail.info("Shelter added to database.")


    def getShelterByID(self,id):
        return self.getEntryByID("Shelters",id)

#++++++++++++++++ USERS ++++++++++++++++++++++++++#
    def addUser(self,username,password,email,name):
        with self.conn:
            cur = self.conn.cursor()
            command = "INSERT INTO Users (Username, Password, Email, Name, Favorites) \
                VALUES (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"\");".format(username, password, email, name)
            cur.execute(command)
            logger.detail.info("{} added to database.".format(name))


#++++++++++++++++ BASE +++++++++++++++++++++++++++#
    def createConnection(self,path="Pets.db"):
        try:
            conn = sqlite3.connect(path)
            return conn
        except Error as e:
            print(e)
        return none

    def buildDatabase(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(DBstrings.petTable)
            cur.execute(DBstrings.shelterTable)
            cur.execute(DBstrings.contactTable)
            cur.execute(DBstrings.usersTable)
            logger.detail.info("DATABASE has been created and loaded with base tables.")

    def getEntryByID(self,table,id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM {0} WHERE ID = {1};".format(table,id))
            return cur.fetchall()


#+++++++++++++++ CLEANING ++++++++++++++++++++++#
    def dropAllTables(self):
        with self.conn:
            cur=self.conn.cursor()
            cur.execute(dropTableQuery("Contacts"))
            cur.execute(dropTableQuery("Pets"))
            cur.execute(dropTableQuery("Shelters"))
            cur.execute(dropTableQuery("Users"))
            logger.detail.warn("ALL TABLES DROPPED FROM Pets.db!")

    def cleanAllTables(self):
        with self.conn:
            cur=self.conn.cursor()
            cur.execute("DELETE FROM Contacts;")
            cur.execute("DELETE FROM Pets;")
            cur.execute("DELETE FROM Shelters;")
            cur.execute("DELETE FROM Users;")
            logger.detail.warn("ALL ROWS DELETED FROM ALL Pets.db TABLES!")

    def deleteEntry(self, table, col, value):
        with self.conn:
            cur=self.conn.cursor()
            command = "DELETE FROM {0} WHERE {1} = {2}".format(table,col,value)
            cur.execute(command)
            logger.detail.info("Row with {0} = {1} DELETED from {2} table.".format(col,value,table))



