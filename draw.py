# -*- coding:utf-8 -*-
# @author: howardhh
# @date: 2018/1/12

import msvcrt
import sys
import time
import os
import random
import threading

print 'begin..........'
def roll():
	with open('d:/howard-github/bonus-script/staff.txt') as file:
		_staff_list = file.readlines()
		_staff_count = len(_staff_list) - 1
		while True:			
			_rand = random.randint(0,_staff_count)
			#print _rand
			print _staff_list[_rand].decode('utf-8').encode('gb2312')
			os.system("cls")
			time.sleep(0.01)

def realroll():
	with open('d:/howard-github/bonus-script/staff.txt') as file:
		_staff_list = file.readlines()
		_staff_count = len(_staff_list) - 1
		_rand = random.randint(0,_staff_count)
		#print _rand
		return _staff_list[_rand].decode('utf-8').encode('gb2312')
						

def interrupt():
	if ord(msvcrt.getch()) in [13,32]:
		try:
			t1.setDaemon(False)
		except:
			print realroll()


threads = []
t1 = threading.Thread(target=roll)
threads.append(t1)
t2 = threading.Thread(target=interrupt)
threads.append(t2)


t1.setDaemon(True)
t1.start()
t2.start()
