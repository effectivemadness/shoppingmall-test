import requests
import random
import time
import json

user_list = []

def user_signin_test():
    while True:
        uid = random.randrange(1500, 2000)
        if uid not in user_list:
            break
    try:
        data = {}
        data['user_id'] = f"user_{uid:04}"
        data['user_name'] = f"user_{uid:04}_name"
        data['user_pw'] = f"user_{uid:04}"
        print(data['user_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/user/signup",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        user_list.append(uid)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def user_leave_test():
    while True:
        uid = random.randrange(1500, 2000)
        if uid in user_list:
            break
    try:
        data = {}
        data['user_id'] = f"user_{uid:04}"
        data['user_pw'] = f"user_{uid:04}"
        print(data['user_id'])
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(
            url="http://k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/user/leave",
            data=json.dumps(data),
            headers=headers
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        user_list.remove(uid)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == '__main__':
    # user_set()
    while True:
        user_signin_test()
        time.sleep(random.random())
        user_leave_test()
        time.sleep(random.random())
