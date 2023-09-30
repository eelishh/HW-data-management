import mysql.connector
from pymongo.mongo_client import MongoClient
import urllib
from tqdm import tqdm

for month in tqdm(["january", "february", "march", "april", "may", "june"]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cyclist"
    )

    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * from " + month + ";"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()

    uri = "mongodb://localhost:27017"
    myclient = MongoClient(uri)
    mydb = myclient["DM"]
    mycol = mydb[month] 

    if len(myresult) > 0:
        x = mycol.insert_many(myresult)
        print(len(x.inserted_ids))