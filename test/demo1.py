#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import redis
import time
import random

sys.path.append('/etc/redis-py')

r = redis.Redis(host="127.0.0.1", port=6379, db=0)


# produce timestamp in millisecond
def  generate_timestamp():
	millis = int(round(time.time() * 1000))
	return millis

# produce server number: 1-2
def generate_servernum():
	sernum = random.randint(1,2)
	return sernum

# produce hash number: 100-199
def generate_hashnum():
	hashnum = random.randint(100,199)
	return hashnum

# produce random data, three options:50MB/5MB/0MB
def generate_randomdata():
	# initial string: 149 bytes, empty string: 49 bytes.
	str_init = 'asdfaasauusfsqwsdfaffafgsdfgdfsgaaassdffgsfa1234dfgsadqertd13sdfdsadfdfdfasdcvz;xdsdfaasdfaqwrqwrasd'
	
	# 生成50MB的字符串
	# 50000000 / 100 = 500000
	str_50M = ''
	'''
	for i in range(500000):
		str_50M += str_init
	'''
	str_50M = str_init * 500000

	# 生成5MB的字符串
	# 5000000 / 100 = 50000
	str_5M = ''
	for i in range(50000):
		str_5M += str_init

	# 生成0MB的字符串
	str_0M = ''

	# test string
	str_test = 'test value'

	# random choose one of them
	candidate = (str_50M, str_5M, str_0M)
	randdata = random.choice(candidate)
	# return randdata
	# return str_test
	# return str_0M
	# return str_5M
	return str_50M

# produce key-value msg
def generate_msg():
	msg_time = generate_timestamp()
	msg_sernum = generate_servernum()
	msg_hashnum = generate_hashnum()
	msg_randdata = generate_randomdata()

	msg = {}
	msg_key = str(msg_time) + str(msg_sernum) + str(msg_hashnum)
	msg_value = msg_randdata
	msg[msg_key] = msg_value

	# store key-value msg in the redis
	start_time = time.time()
	cnt = 0
	print ("Start to put data into Redis at:", start_time)
	now_time = time.time()
	while now_time < (start_time + 1):
		r.set(msg_key, msg_value)
		cnt += 1
		now_time = time.time()
	print(cnt)
	print(start_time)
	print(now_time)

def main():
	generate_msg()

if __name__ == '__main__':
	main()
	
