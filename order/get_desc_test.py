import requests
import random
import time
import json


def order_get_desc_test():
    order_id = random.randrange(0, 1000)
    try:
        params = {}
        params['order_id'] = order_id
        response = requests.get(
            url="http://k8s-shopping-ordering-89f985b67a-1398614510.ap-northeast-2.elb.amazonaws.com/order/desc",
            params=params
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    sleep_time = random.random() / 100
    print(f"sleeping {sleep_time}")
    time.sleep(sleep_time)


if __name__ == '__main__':
    # user_set()
    while True:
        order_get_desc_test()