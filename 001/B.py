# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
b = a / 1000
if b < 0.1:
	print('00')
elif (b >= 0.1) and (b <= 5):
	if (b >= 0.1) and (b < 1):
		print('0' + str(int(b*10)))
	else:
		print(str(int(b * 10)))
elif (b>= 6) and (b <= 30):
	print(str(int(b + 50)))
elif (b >= 35) and (b <= 70):
	print(str(int( (b - 30) / 5 + 80 )))
else:
	print('89')