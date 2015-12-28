# -*- coding: utf-8 -*-
"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码
（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random
import string


def generator(num, length = 10):
	f = open('activation-code.txt','w')
	char = string.letters + string.digits
	for i in range(num):
		s = [random.choice(char) for i in range(length)]
		f.write (''.join(s) + '\n')
	f.close

if __name__ == '__main__':
	generator(200)
