##########
########## Creating database and entering data
##########

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Create table named Simpson_Info
conn.execute("CREATE TABLE SIMPSON_INFO(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, GENDER TEXT,AGE INT, OCCUPATION TEXT); ")

# Add Bart Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO(NAME, GENDER, AGE, OCCUPATION) VALUES ('Bart Simpson','Male',10,'Student'); ")

# Add Home Simpson
conn.execute("INSERT INTO SIMPSON_INFO(NAME, GENDER, AGE, OCCUPATION) VALUES ('Homer Simpson','Male',40,'Nuclear Plant'); ")

# Add Lisa Simpson
conn.execute("INSERT INTO SIMPSON_INFO(NAME, GENDER, AGE, OCCUPATION) VALUES ('Lisa Simpson','Female',8,'Student'); ")

# Save changes
conn.commit()

# Print number of changes to database
changes=conn.total_changes
print"Number of changes:", changes

##########
########## Get data from database and Delete Data
##########

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Get data from database
cursor = conn.execute("SELECT ID, NAME, GENDER, AGE, OCCUPATION from SIMPSON_INFO")
cursor = conn.execute("SELECT * from SIMPSON_INFO")
cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")
cursor = conn.execute("SELECT * from SIMPSON_INFO where GENDER='Female'")
cursor = conn.execute("SELECT * from SIMPSON_INFO where OCCUPATION='Student'")

cursor = conn.execute("DELETE from SIMPSON_INFO where ID=2")

# Save changes
conn.commit()

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Print number of changes to database
changes=conn.total_changes
print"Number of changes:", changes

# Extract data from cursor
rows = cursor.fetchall()
print rows

##########
########## Updating Data in SQL
##########

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Updating Data
conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson'")

# Save changes
conn.commit()

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Print number of changes to database
changes=conn.total_changes
print"Number of changes:", changes

# Extract data from cursor
rows = cursor.fetchall()
print rows

##########
########## Deleting a Table in SQL
##########
import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')


conn.execute("DROP TABLE SIMPSON_INFO")

# Save changes
conn.commit()

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Print number of changes to database
changes=conn.total_changes
print"Number of changes:", changes

# Extract data from cursor
rows = cursor.fetchall()
print rows