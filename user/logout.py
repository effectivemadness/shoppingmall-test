import requests
import random
import time
import json


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


if __name__ == '__main__':
    # user_set()
    while True:
        user_logout_test()