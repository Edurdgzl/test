"""
    Class that describes a store
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
from Global.Utils.db import post, get
from json import load
from venv import create


class Store:

    def __init__(self, params, db=True):
        self.id = None
        self.name = None
        self.state = None
        self.street = None
        self.number = None
        self.city = None
        self.password = None
        self.load(params) if db else self.create(params)
        


    def create(self, params):
        from hashlib import md5
        self.name = params['name']
        self.state = params['state']
        self.street = params['street']
        self.number = params['number']
        self.city = params['city']
        self.password = md5(params['password'].encode()).hexdigest()

        try:

            self.id = post(
                '''INSERT INTO store(name, state, street, number, city, password) VALUES (%s, %s, %s, %s, %s, %s) RETURNING store_id''',
                (self.name, self.state, self.street, self.number, self.city, self.password),
                True
            )
           
        except Exception as e:  
            
            return e


    def load(self, params):
        self.id = params['id']

        try:

            self.name, self.state, self.street, self.number, self.city, self.password = get(
                '''SELECT * FROM store WHERE store_id = %s ''',
                (self.id,),
                False
            )

        except Exception as e:
            return e
    
    @classmethod
    def get_store_products(cls, id):
        result = get(
            ''' SELECT p.name, sp.quantity
                FROM store_product sp, product p
                WHERE sp.store_id = %s ''',
            (id,)
            )
        return {'products': result}