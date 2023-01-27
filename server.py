from flask import Flask, request
import json
from mock_data import catalog
from config import db
from flask_cors import CORS

app = Flask("server")
CORS(app)

@app.get("/")
def home():
    return "hello from flask"

#Create an endpoint that redirects to the about page and 
#it contains your name
@app.get("/about")
def about():
    return "Jose Luis Sanchez"

################################################################
####################### CATALAG API  ###########################
################################################################

@app.get("/api/version")
def version():
 return "test"


@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"]) # fix _id issue
        results.append(prod)
    
    return json.dumps(results)

# save products
@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    product["_id"] = str(product["_id"]) # clean the ObjectId('asd') from the obj

    return json.dumps(product)


@app.get("/api/catalog/<category>")
def get_by_category(category):
    cursor =db.products.find({"category": category})
    results = []
    for prod in cursor:
            prod["_id"] = str(prod["_id"])
            results.append(prod)

    return json.dumps(results)

@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    cursor =db.products.find({"title": {"$regex": title, "$options": "i"} })
    results = []
    for prod in cursor:
            prod["_id"] = str(prod["_id"])
            results.append(prod)

    return json.dumps(results)


@app.get("/api/product/cheaper/<price>")
def search_by_price(price):
    cursor = db.products.find({})
    result = []
    for prod in catalog:
        if prod["price"] < float(price):
            prod["_id"] = str(prod["_id"])
            result.apend(prod)

    return json.dumps(result)

@app.get("/api/product/count")
def count_products():
    count = db.products.count_documents({})
    return json.dumps(count)


@app.get("/api/product/cheapest")
def get_cheapest():
    cursor = db.products.find({})
    answer = cursor[0]
    for prod in cursor:
        if prod["price"] < answer["price"]:
            answer = prod

    answer["_id"] = str(prod["_id"])
    return json.dumps(answer)


@app.get('/test/numbers') 
def get_numbers():

    result = []  
    for n in range(1, 21):
        if n != 13 and n != 17:
            result.append(n)
        
    return json.dumps(result)

app.run(debug=True)
