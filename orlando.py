import pandas as pd, os, numpy, time, datetime as dt, json
from pymongo import MongoClient

path = "/home/francois/Bureau/orlando_dataset/"
list_of_dataframes = []
client = MongoClient('mongodb://localhost:27017/')
db = client['AttractionsDisney']
collection = db["AttractionsOrlando"]

theme_parks_attractions = {
    "Splash Mountain" : "MagicKingdom_01",
    "Toy Story Mania" : "DisneysHollywoodStudios_01",
    "Rock N Rollercoaster" : "DisneysHollywoodStudios_02",
    "Kilimanjaro Safaris" : "DisneysAnimalKingdom_01",
    "Spaceship Earth" : "Epcot_01",
    "Pirates Of Caribbean" : "MagicKingdom_02",
    "Dinosaur" : "DisneysAnimalKingdom_02",
    "Expedition Everest" : "DisneysAnimalKingdom_03",
    "Soarin" : "Epcot_02"
}


for file in os.listdir(path):
    if os.path.splitext(file)[1] == ".csv" and not file == "metadata.csv":
        df_csv = pd.read_csv(path + file)
        df_csv = df_csv.drop(columns='SACTMIN')
        name = os.path.splitext(file)[0].replace("_", " ").title()
        lastUpdate = df_csv["datetime"]
        df_attraction = pd.DataFrame({"name" : name, "id" : theme_parks_attractions[name], "waitTime" : df_csv["SPOSTMIN"], "lastUpdate" : lastUpdate})
        df_attraction = df_attraction.dropna()
        df_attraction["active"] = df_attraction.apply(lambda row: False if row['waitTime'] == -999.0 else True, axis=1)
        df_attraction["status"] = df_attraction.apply(lambda row: "Operating" if row['active'] else "Closed", axis=1)
        df_attraction["lastUpdate"] = (pd.to_datetime(df_attraction["lastUpdate"]) - dt.datetime(1970,1,1)).dt.total_seconds()
        list_of_dataframes.append(df_attraction)


df = pd.DataFrame().append(list_of_dataframes)
df = df.sort_values(by=['lastUpdate'])
records = df.to_dict(orient='records')
collection.insert_many(records)