#!/usr/bin/python3.4

import sys

c_eq = '\033[32m'
c_diff = '\033[36m'
c_default = '\033[0m'
c_fail = '\033[31m'

def display_line(line1, line2):
	for i in range(len(line1)):
		try:
			if i == len(line1) - 1 and i != len(line2) - 1:
				print(c_fail + '.' * (len(line2) - len(line1)))
				continue
			if line1[i] == line2[i]:
				print(c_eq + line1[i], end='')
			else:
				print(c_diff + line1[i], end='')
		except IndexError:
			pass

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print('Usage: %s file1 file2' %(sys.argv[0]))

	with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
		for x in f1:
			y = f2.readline()
			display_line(x, y)
			display_line(y, x)

