def payment_set():
    for i in range(1000):
        try:
            data = {}
            data['payment_id'] = i
            data['payment_name'] = f"prod_{i:04}"
            data['balance'] = random.randrange(1000000, 9900000)
            data['user_id'] = f"prod_{random.randrange(0,1500):04}"
            print(data['payment_id'])
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            response = requests.post(
                url="http://payment-service.shoppingmall-lgu.svc.cluster.local:8080/payment/create",
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