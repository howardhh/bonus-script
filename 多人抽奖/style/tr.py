file1=open('staff.txt','r')
file2=open('newstaff.txt','w')
array = file1.readlines()
print array
for i in range(len(array)):
	#newline = 'xinm[' + str(i) + ']=\"' + array[i].rstrip() + '\"\n'
	newline = 'phone[' + str(i) + ']=\"' + '************' + '\"\n'
	file2.write(newline)
file1.close()
file2.close()
