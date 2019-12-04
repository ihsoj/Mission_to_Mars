from flask import Flask, render_template, redirect,jsonify 
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri = "mongodb://localhost:27017/app_mars")

# Define database and collection
#db = client.mars_db
#collection = db.items


@app.route("/")
def index():

    data1 = mongo.db.data.find_one()
    return render_template("index.html", data=data1)

@app.route("/scrape")
def scrape():
    #Call scrape function from scrape_mars.py
    #data = scrape_mars.scrape()
    data = mongo.db.data
    data_mars = scrape_mars.scrape()
    data.update({},data_mars,upsert = True)
    
   #Load scrape data in Mongo DB collection called items
   # mongo.db.collection.insert_one(data)

   #Redirect to index
    return redirect("/")


if __name__ == "__main__":
  app.run(port = 5001)
