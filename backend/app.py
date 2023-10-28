from flask import Flask,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS,cross_origin

#Inititalization
app=Flask(__name__)
cors=CORS(app)

#Configure App
app.config["MONGO_URI"]="mongodb://localhost:27017/recipe"
app.config["CORS_HEADER"]="Content-Type"
mongo=PyMongo(app)

#Route
@app.route("/")
def index():
    recipe=list(mongo.db.recipes.find())
    for a in recipe:
        a['_id']=str(a['_id'])
    data={"data":recipe}
    return jsonify(data)

# condition required while connecting flask to server
if __name__ == "__main__":
    app.run(debug=True)