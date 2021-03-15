# Import libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask app
app = Flask(__name__)

# PyMongo for Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

# Home route
@app.route("/")
def home():
    mars_home = mongo.db.collection.find_one()
    return render_template("index.html", mars = mars_home)

# Route for scrape
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_info = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")






if __name__ == "__main__":
    app.run(debug=True)