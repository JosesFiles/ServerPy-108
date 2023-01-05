from flask import Flask
import json
from mock_data import catalog


app = Flask("server")

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
    version = {
        "V":"V.1.0.1",
        "name":"Candy_firewall",
        "yourzip": "your",
    }
    return json.dumps(version)


@app.get("/api/catalog")
def get_catalog():

    return json.dumps(catalog)

@app.get("/api/catalog/<category>")
def get_by_category(category):
    result = []
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            result.append(prod)

    return json.dumps(result)

@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    result = []
    for prod in catalog:
        if title.lower() in prod["title"].lower():
            result.append(prod)

    return json.dumps(result)

@app.get("/api/product/cheaper/<price>")
def search_by_price(price):
    result = []
    for prod in catalog:
        if prod["price"] < float(price):
            result.apend(prod)

    return json.dumps(result)

@app.get("/api/product/count")
def count_products():
    count = len(catalog)
    return json.dumps(count)


@app.get("/api/product/cheapest")
def get_cheapest():
    answer = catalog[0]
    for prod in catalog:
        if prod["price"] < answer["price"]:
            answer = prod

    return json.dumps(answer)


@app.get('/test/numbers') 
def get_numbers():

    result = []  
    for n in range(1, 21):
        if n != 13 and n != 17:
            result.append(n)
        
    return json.dumps(result)

app.run(debug=True)
