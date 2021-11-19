from flask import request
from flask_api import status

from app import app
from app.storage import get_data, store_data
from app.utils import get_item_index_or_404, item_to_json, get_user_input_json


@app.route('/items/', methods=['GET', 'POST'])
def all_item_requests_handler():
    data = get_data()
    if request.method == 'GET':
        return [item_to_json(item) for item in data]
    else:
        user_data = get_user_input_json(request.get_data())
        item_request = {
            "id": max([msg['id'] for msg in data], default=0) + 1,
            "title": user_data['title'],
            "amount": user_data['amount'],
            "price": user_data['price'],
        }
        data.append(item_request)
        store_data(data)
        return item_to_json(item_request), status.HTTP_201_CREATED


@app.route('/items/calculate/', methods=['GET'])
def get_all_amount_item_handler():
    data = get_data()
    summa = 0
    for item in data:
        if item['amount'] > 0:
            summa += item['amount'] * item['price']
    return {'massege': f'sum of amounts of all items is: {summa}'}


@app.route('/items/<int:item_id>/', methods=['GET', 'PUT', 'DELETE'])
def single_item_request_handler(item_id):
    data = get_data()
    item_index = get_item_index_or_404(data, item_id)
    item_request = data[item_index]
    if request.method == 'GET':  # GET
        return item_to_json(item_request)
    elif request.method == 'PUT':  # UPDATE
        user_data = get_user_input_json(request.get_data())
        item_request['title'] = user_data["title"]
        item_request['amount'] = user_data['amount']
        item_request['price'] = user_data['price']
        store_data(data)
        return item_to_json(item_request)
    else:  # DELETE
        del data[item_index]
        store_data(data)
        return None, status.HTTP_204_NO_CONTENT
