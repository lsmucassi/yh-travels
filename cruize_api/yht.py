from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Destinations'
app.config['MONGO_URI'] = 'mongodb+srv://william-phokompe:WilliamPhokompe@travellingcluster-heab2.mongodb.net/Destinations?retryWrites=true&w=majority'
mongo = PyMongo(app)
    
@app.route('/continents', methods=['GET'])
def get_all_continents():
    continent = mongo.db.Continents
    continents = []

    for cont in continent.find():
        continents.append({
            'id': cont['id'], 
            'name': cont['name'],
            'tours' : cont['tours'],
            'places': cont['places']
        })

    return jsonify({'result': continents})

# @app.route('/continents/create', methods=['POST'])
# def add_continent():
#     continent = mongo.db.Continents
#     id = str(uuid.uuid4())
#     name = request.json['name']
#     tours = request.json['tours']
#     places = request.json['places']
#     continent_id = continent.insert({
#         'id': id,
#         'name': name,
#         'tours': tours,
#         'places': places
#     })
#     new_continent = continent.find_one({'_id': continent_id})

#     return jsonify({
#         'result': {
#             'id': new_continent['id'],
#             'name': new_continent['name'],
#             'tours': new_continent['tours'],
#             'places': new_continent['places']
#         }
#     })

@app.route('/continents/countries', methods=['GET'])
def get_countries():
    return jsonify({'result': {}})

@app.route('/continents/countries/cities', methods=['GET'])
def get_countries(): 

    return jsonify({'result': {}})

if __name__ == '__main__':
    app.run(debug=True)