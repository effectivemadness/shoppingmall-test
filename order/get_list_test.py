import requests
import random
import time
import json


def order_get_list_test():
    try:
        response = requests.get(
            url="http://k8s-shopping-ordering-89f985b67a-1398614510.ap-northeast-2.elb.amazonaws.com/order/list"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == '__main__':
    # user_set()
    while True:
        order_get_list_test()
        time.sleep(random.random())