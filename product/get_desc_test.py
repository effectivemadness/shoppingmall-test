import requests
import random
import time
import json


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


if __name__ == '__main__':
    # user_set()
    while True:
        prod_get_desc_test()
        time.sleep(random.randrange(0, 2))