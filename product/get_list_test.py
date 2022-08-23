import requests
import random
import time
import json


def prod_get_list_test():
    try:
        response = requests.get(
            url="http://k8s-shopping-producti-67d279dcae-1560587798.ap-northeast-2.elb.amazonaws.com/product/list"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == '__main__':
    # user_set()
    while True:
        prod_get_list_test()
        time.sleep(random.random())