#!/usr/bin/env python

import os
import sys

filename = raw_input('type filename: ')



# def ask_filename():
# 	text1 = raw_input('type filename: ', )
# 	print text1

def ask_filecontent():
	text1 = raw_input('type in line1 content: ', )
	return text1

def if_exists(filename):
	print '{} exists'.format(filename)
	text = open(filename,'r')
	for x in text:
		print x

def if_not_exist(filename):
	print '{} does not exists'.format(filename)
	new_file = open(filename,'w+')
	content = raw_input('add text: ')
	n = open(filename, 'w')
	n.write(content)
	ask = raw_input('do you want to add more? yes/no: ')
	y = asking(ask)
	# n = open(filename, 'w')
	n.write(y)

def asking(ask):
	x = 0
	t = ""
	while x < 999:
		content = raw_input('add text: ')
		t = t + '\n' + content
		print t
		asker = raw_input('do you want another line? ')
		if asker == 'yes':
			x+=1
		elif asker == 'no':
			x+=9999
	return t










def main(filename):
	if not os.path.isfile(filename):
		if_not_exist(filename)
	else:
		if_exists(filename)



main(filename)

