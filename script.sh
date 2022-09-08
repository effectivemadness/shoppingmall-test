#!/bin/sh
python3 user/login.py &
python3 user/logout.py &
python3 user/signin_leave.py &
python3 product/get_desc_test.py &
python3 product/get_list_test.py &
python3 product/register_delete_test.py &
python3 order/create_cont_test.py &
python3 order/get_desc_test.py &
python3 order/get_list_test.py &
