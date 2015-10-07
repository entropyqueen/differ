#!/usr/bin/python3.4

import sys
import contextlib

line_spacing = True

colors = {
	'white':	'\033[0m',
	'black': 	'\033[30m',
	'red':		'\033[31m',
	'green':	'\033[32m',
	'yellow':	'\033[33m',
	'blue':		'\033[34m',
	'purple':	'\033[35m',
	'cyan':		'\033[36m'
}

c_fail = '\033[31m'
c_default = '\033[0m'

def display_line(line1, lines, args):
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
				print(colors[args.diff_color] + line1[i], end='')
			else:
				print(colors[args.eq_color] + line1[i], end='')
		except IndexError:
			print(c_fail + line1[i], end='')
	print(c_default)

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(prog='differ',
				description='A simple diff script to quickly show the differences between multiple files.')
	parser.add_argument('--file-number', '-f', dest='lnbr', action='store_true',
				 help='show file number before each lines')
	parser.add_argument('--eq-color', dest='eq_color', type=str, default='green', metavar='COLOR',
				help='choose color for matching chars')
	parser.add_argument('--diff-color', dest='diff_color', type=str, default='cyan', metavar='COLOR',
				help='choose color for different chars')
	parser.add_argument('--color-list', dest='disp_clist', help='print color list and exits', action='store_true')
	parser.add_argument('FILE', nargs='+', help='files to compare')
	parser.set_defaults(lnbr=False)
	args = parser.parse_args()

	if args.disp_clist == True:
		print('Available colors are:')
		for k, v in colors.items():
			print('\t' + v + k)
		exit()

	with contextlib.ExitStack() as stack:
		files = [stack.enter_context(open(fname)) for fname in args.FILE]
		for l in files[0]:	
			lines = [x.readline() for x in files[1:]]
			lines.append(l)
			for j in range(len(lines)):
				if args.lnbr == True:
					print('{}> '.format(j), end='')
				tmp=[y for y in lines]
				tmp.remove(lines[j])
				display_line(lines[j], tmp, args)
			if line_spacing == True:
				print('')
