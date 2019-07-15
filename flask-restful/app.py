from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


items = [{
            "name": "banana",
            "price": 25.99
        },
        {
            "name": "apple",
            "price": 125.99
        },
        {
            "name": "orange",
            "price": 1.99
        }]

#Each class with extend Resource class
class Item(Resource):
    def get(self,name): #GET request's response will be rendered from this method
        item = next(filter(lambda x: x['name']==name,items),None)
        return {'name':item},200 if item else 404 # set http status as 200 is item available else 404
    def post(self,name): #POST request's response will be rendered from this method
        data = request.get_json(force=True)
        item = next(filter(lambda x: x['name']==data['name'],items),None)
        if item:
            return {'message':'An item with name {} already exists'.format(data['name'])},400 #error is item already exists
        item = {'name':data['name'],'price':data['price']}
        items.append(item)
        return item,201
    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name']!=name,items)) # for remove we will iterate and retain all items that has name != name sent in request
        '''
        new_items=[]
        for item in items:
            if item['name'] != name:
                new_items.append(item)
        items = new_items
        '''
        return {'message':'{} deleted from the list'.format(name)},200
		
class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>') #Mapping request and class
api.add_resource(ItemList,'/items')

app.run(port=5000,debug=True)