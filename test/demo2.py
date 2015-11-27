#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import time

start_time = time.time()
cnt = 0
print ("Start to put data into Redis at:", start_time)
now_time = time.time()
while now_time < (start_time + 1):
	# print('test time')
	cnt += 1
	now_time = time.time()
print(cnt)
print(start_time)
print(now_time)