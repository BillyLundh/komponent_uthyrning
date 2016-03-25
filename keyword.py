#!/usr/bin/python
# -*- coding: utf-8 -*

''' Search specified file and enter keyword'''



y = raw_input("Enter file path: ");

z = raw_input("Enter keyword: ");

count = 0;


# /HAL/tasks.txt

x = open(y)

for line in x:
	if line.startswith(z):
		#print "\n"
		print line
		count = count + 1

print 'Nbr of lines: ', count
print '\n'


