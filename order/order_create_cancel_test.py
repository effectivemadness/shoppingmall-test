import requests
import random
import time
import json

order_list = []


def order_create_test():
    while True:
        order_id = random.randrange(0, 300)
        if order_id not in order_list:
            break
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
        order_list.append(order_id)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def order_cancel_test():
    while True:
        order_id = random.randrange(0, 300)
        if order_id in order_list:
            break
    try:
        data = {'order_id': order_id}
        print(data['order_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-ordering-89f985b67a-1398614510.ap-northeast-2.elb.amazonaws.com/order/cancel",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        order_list.remove(order_id)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

if __name__ == '__main__':
    # user_set()
    while True:
        order_create_test()
        time.sleep(random.randrange(0, 2))
        order_cancel_test()
        time.sleep(random.randrange(0, 2))