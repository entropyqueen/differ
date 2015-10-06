#!/usr/bin/python3.4

import sys
import contextlib

line_spacing = True

c_eq = '\033[32m'
c_diff = '\033[36m'
c_default = '\033[0m'
c_fail = '\033[31m'

def display_line(line1, lines):
	line1 = line1.strip()
	for i in range(len(line1)):
		try:
			diff = False
			for line in lines:
				line = line.strip()
				if i == len(line) + 1:
					print(c_fail + line1[i], end='')
					continue
				if line[i] != line1[i]:
					diff = True
			if diff == True:
				print(c_diff + line1[i], end='')
			else:
				print(c_eq + line1[i], end='')
		except IndexError:
			print(c_fail + line1[i], end='')
	print(c_default)

if __name__ == "__main__":

	if len(sys.argv) < 3:
		print('Usage: %s file1 file2 ... fileX' %(sys.argv[0]))
		exit()

	with contextlib.ExitStack() as stack:
		files = [stack.enter_context(open(fname)) for fname in sys.argv[1:]]
		for l in files[0]:	
			lines = [x.readline() for x in files[1:]]
			lines.append(l)
			for line in lines:
				tmp=[y for y in lines]
				tmp.remove(line)
				display_line(line, tmp)
			if line_spacing == True:
				print('')
