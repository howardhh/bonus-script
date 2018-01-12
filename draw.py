# -*- coding:utf-8 -*-
# @author: howardhh
# @date: 2018/1/12

import msvcrt
import sys
import time
import os
import random
import threading

def roll():
	with open('stafflist') as file:
		_staff_list = file.readlines()
		_staff_count = len(_staff_list) - 1
		while True:
			_rand = random.randint(0,_staff_count)
			print "按回车停止"
			print _staff_list[_rand]
			time.sleep(0.05)
			os.system("/usr/bin/clear")

def interrupt():
	if ord(msvcrt.getch()) in [13,32]:
		try:
			t1.setDaemon(False)
		except:
			print "恭喜"


threads = []
t1 = threading.Thread(target=roll)
threads.append(t1)
t2 = threading.Thread(target=interrupt)
threads.append(t2)

if __name__ == '__main__':
	t1.setDaemon(True)
	t1.start()
	t2.start()
