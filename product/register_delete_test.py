import requests
import random
import time
import json

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


def prod_delete_test():
    while True:
        prod_id = random.randrange(500, 1000)
        if prod_id in prod_list:
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
        prod_list.remove(prod_id)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

if __name__ == '__main__':
    # user_set()
    while True:
        prod_register_test()
        time.sleep(random.random()/10)
        prod_delete_test()
        time.sleep(random.random()/10)