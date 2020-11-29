#Code adapated from https://github.com/andrewbeattycourseware/dataRepresenation2020
from stockDAO import stockDao
from flask import Flask, url_for, request, redirect, abort,jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')




@app.route('/')
def index():
   return  "is this thing on?"

@app.route('/stock')
def getAll():
   return jsonify(stockDao.getAll())
#curl http://127.0.0.1:5000/stock

@app.route('/stock/<int:id>') 
def findById(id): 
    return jsonify(stockDao.findById(id))
#curl http://127.0.0.1:5000/stock/109


#curl -X POST -d "{\"description\":\"Apple Juice Box\", \"price\":1250, \"provenance\":\"The Apple Farm, Cahir\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/stock
@app.route('/stock', methods=['POST'])
def create(): 

    if not request.json: #abort the request if it is not in the correct json format
        abort(400)
    #if it is a good request do this, append the book with a new id and so on
    item = {
        "description": request.json["description"],
        "price": request.json["price"],
        "provenance": request.json["provenance"]
    }

    return jsonify(stockDao.create(item))
   



#curl -X PUT -d "{\"description\":\"new lad\", \"price\":567, \"provenance\":\"Cashel\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/stock/115
@app.route('/stock/<int:id>', methods=['PUT'])
def update(id):
    foundItem=stockDao.findById(id)
    print(foundItem)
    if foundItem == {}:#if ya find nothing with that id,  code 404 shows up on the server, {} on the screen.
        return jsonify({}), 404
    currentItem = foundItem
    if 'description' in request.json:
        currentItem['description'] = request.json['description']
    if 'price' in request.json:
        currentItem['price'] = request.json['price']
    if 'provenance' in request.json:
        currentItem['provenance'] = request.json['provenance']
    stockDao.update(currentItem)
    return jsonify(currentItem)


#λ curl -X DELETE http://127.0.0.1:5000/stock/115
#{
#  "done": true
#}

@app.route('/stock/<int:id>', methods=['DELETE'])
def delete(id):
    stockDao.delete(id)
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)