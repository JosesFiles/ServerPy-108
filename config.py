import pymongo
import certifi

connection_str = "mongodb+srv://FSDI:jose1981@cluster0.0ligvcm.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where() )
db = client.get_database("OnlineStore")