import os #operating system
products = [] # 建立空清单
if os.path.isfile('product.csv'):#检查档案是否在里面
	print('yeah! 找到档案惹！')
	with open('product.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到档案惹.....')

# 让使用者输入
while True:
	name = input('请输入商品名称： ')
	if name == 'q':
		break
	price = input('请输入商品价格： ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有购买记录
for p in products:
	print(p[0], '的价格是', p[1])

# 写入档案
with open('product.csv', 'w', encoding = 'utf-8') as f: #with 的功能是自动close
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
