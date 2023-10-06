x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))

maximum = max(x, y, z)
minimum = min(x, y, z)
middle = (x + y + z) - maximum - minimum

print("由大到小排序：", maximum, middle, minimum)
