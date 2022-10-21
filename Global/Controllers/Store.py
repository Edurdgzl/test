"""
    Script that handles the received requests
    Authors: David Rodriguez Fragoso, Erick Hernandez Silva
    Created: 18/10/2022
    Last update: 18/10/2022
"""
import re
from flask import request
from Global.Classes.Store import Store

def create_store():
    try:
        params = {
            'name': request.json.get('name'),
            'state': request.json.get('state'),
            'street': request.json.get('street'),
            'number': request.json.get('number'),
            'city': request.json.get('city'),
            'password': request.json.get('password')
        }
        print(params)
        store = Store(params, False)
        return f'Store {store.name} created', 200
    except Exception as e:
        return str(e), 400

def get_store_products():
    try:
        store_id = request.args.get('store_id')
        return Store.get_store_products(store_id)
    except Exception as e:
        return str(e), 400