# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import random
import time
import json


def order_set():
    for i in range(1000):
        try:
            data = {}
            data['order_id'] = i
            data['user_id'] = f"user_{random.randrange(0,1500):04}"
            data['prod_id'] = random.randrange(0,500)
            data['payment_id'] = random.randrange(0,1000)
            data['order_note'] = f"order_{i:04}"
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
        sleep_time = random.random()/100
        print(f"sleeping {sleep_time}")
        time.sleep(sleep_time)

prod_list = []

def prod_register_test():
    while True:
        prod_id = random.randrange(500, 1000)
        if prod_id not in prod_list:
            break
    try:
        data = {}
        data['prod_id'] = prod_id
        data['prod_name'] = f"prod_{prod_id:04}"
        data['prod_price'] = random.randrange(1000, 99000)
        print(data['prod_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-producti-67d279dcae-1560587798.ap-northeast-2.elb.amazonaws.com/product/register",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        prod_list.append(prod_id)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)


def prod_delete_test():
    while True:
        prod_id = random.randrange(500, 1000)
        if prod_id not in prod_list:
            break
    try:
        data = {}
        data['prod_id'] = prod_id
        print(data['prod_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-producti-67d279dcae-1560587798.ap-northeast-2.elb.amazonaws.com/product/delete",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        prod_list.append(prod_id)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)


def prod_get_list_test():
    try:
        response = requests.get(
            url="http://k8s-shopping-producti-67d279dcae-1560587798.ap-northeast-2.elb.amazonaws.com/product/list"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)

def prod_get_desc_test():
    prod_id = random.randrange(0, 500)
    try:
        params = {}
        params['prod_id'] = prod_id
        response = requests.get(
            url="http://k8s-shopping-producti-67d279dcae-1560587798.ap-northeast-2.elb.amazonaws.com/product/list",
            params=params
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)


def user_logout_test():
    uid = random.randrange(0, 1500)
    try:
        data = {}
        data['user_id'] = f"user_{uid:04}"
        data['user_pw'] = f"user_{uid:04}"
        print(data['user_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/user/logout",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # user_set()
    while True:
        order_set()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
