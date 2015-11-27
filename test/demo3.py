#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import time

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
	return str_50M

# produce key-value msg
def generate_msg():
	start_time = time.time()
	for i in range(50):
		msg = generate_randomdata()
	stop_time = time.time()
	print(start_time)
	print(stop_time)
	between_time = stop_time - start_time
	print(between_time)

def main():
	generate_msg()

if __name__ == '__main__':
	main()