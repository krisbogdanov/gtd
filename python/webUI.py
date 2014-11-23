from bottle import view, route, run, template
from pymongo import MongoClient
from model.Thing import Thing
@route('/')
@view('index')
def index():
    client = MongoClient('localhost', 27017)
    db = client.gtd
    collectionOfThings = db.Things
    document = collectionOfThings.find_one()
    thing = Thing(document['Thing']['descr'])
    return template('index', document = thing.descr)

run(host='localhost', port=8080)