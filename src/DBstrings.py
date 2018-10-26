class DBstrings:

    petTable = "CREATE TABLE IF NOT EXISTS Pets(\
            ID integer PRIMARY KEY,\
            Name text NOT NULL,\
            Age text NOT NULL,\
            Animal text NOT NULL,\
            Description text NOT NULL,\
            Mix text NOT NULL,\
            Sex text NOT NULL,\
            Size text NOT NULL,\
            Breeds text NOT NULL,\
            Media text,\
            ContactID integer NOT NULL,\
            ShelterID text NOT NULL);"

    contactTable = "CREATE TABLE IF NOT EXISTS Contacts(\
            ID integer PRIMARY KEY AUTOINCREMENT,\
            Phone text NOT NULL,\
            Email text NOT NULL,\
            Address text NOT NULL,\
            City text NOT NULL,\
            State text NOT NULL,\
            Zip text NOT NULL);"

    shelterTable = "CREATE TABLE IF NOT EXISTS Shelters(\
            ID text PRIMARY KEY,\
            Name text NOT NULL,\
            Phone text NOT NULL,\
            Email text NOT NULL,\
            Address text NOT NULL,\
            City text NOT NULL,\
            State text NOT NULL,\
            Zip text NOT NULL,\
            Country text NOT NULL,\
            Latitude text,\
            Longitude text);"

    usersTable = "CREATE TABLE IF NOT EXISTS Users(\
            ID text PRIMARY KEY,\
            Userame text NOT NULL,\
            Password text NOT NULL,\
            Email text NOT NULL,\
            Name text NOT NULL,\
            Favorites text NOT NULL);"





