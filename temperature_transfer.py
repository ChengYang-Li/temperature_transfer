# temperature transfer

transfer_type = int(input('請選擇你要轉換的形式(攝氏轉華氏請打1 華氏轉攝氏請打2):'))

if transfer_type == 1:
	c = float(input('請輸入攝氏溫度:'))
	f = 9 * c / 5 + 32
	print('華氏溫度為:', f)

if transfer_type == 2:
	f = float(input('請輸入華氏溫度:'))
	c = (f - 32) * 5 / 9
	print('攝氏溫度為:', c)


