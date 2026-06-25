import pandas as pd
import sqlite3 as db

#Reading the file
df = pd.read_csv('20_Roundabouts_Worldwide.csv')

#Creating/Starting the connection to the database
connectionEstablish = db.connect("mydatabase.db")

#Creating the table based on the info given in the csv file
df.to_sql(
    name = 'Roundabouts', #name of the table
    con=connectionEstablish, #Name of the connection
    if_exists='replace',  #replace, append, or fail
    index=False
)

#Closing database connection
connectionEstablish.close()
