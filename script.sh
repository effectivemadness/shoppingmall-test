#!/bin/sh
nohup python3 user/login.py &
nohup python3 user/logout.py &
nohup python3 user/signin_leave.py &
nohup python3 product/get_desc_test.py &
nohup python3 product/get_list_test.py &
nohup python3 product/register_delete_test.py &
nohup python3 order/create_cont_test.py &
nohup python3 order/get_desc_test.py &
nohup python3 order/get_list_test.py &