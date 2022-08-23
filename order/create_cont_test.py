import requests
import random
import time
import json


def order_create_test_cont(order_id):
    try:
        data = {'order_id': order_id, 'user_id': f"user_{random.randrange(0, 1500):04}",
                'prod_id': random.randrange(0, 500), 'payment_id': random.randrange(0, 1000),
                'order_note': f"order_{order_id:04}"}
        print(data['order_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-ordering-89f985b67a-1398614510.ap-northeast-2.elb.amazonaws.com/order/create",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_order_count():
    try:
        response = requests.get(
            url="http://k8s-shopping-ordering-89f985b67a-1398614510.ap-northeast-2.elb.amazonaws.com/order/count"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        order_id = response.json()['count']
        return order_id
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

if __name__ == '__main__':
    # user_set()
    order_id = get_order_count()
    while True:
        order_create_test_cont(order_id)
        order_id += 1