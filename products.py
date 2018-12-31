import os #operating system

#读取档案
def read_file(filename):
	products = [] # 建立空清单
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 让使用者输入
def user_input(products):
	while True:
		name = input('请输入商品名称： ')
		if name == 'q':
			break
		price = input('请输入商品价格： ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# 印出所有购买记录
def print_product(products):
	for p in products:
		print(p[0], '的价格是', p[1])

# 写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #with 的功能是自动close
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#检查档案是否在里面
		print('yeah! 找到档案惹！')
		products = read_file(filename)
	else:
		print('找不到档案惹.....')
	products = user_input(products)
	print_product(products)
	write_file('products.csv', products)

main()

# 这个写程序的过程叫做refactor
 