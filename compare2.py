x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))

numbers = [x, y, z]
numbers.sort(reverse=True)

print("由大到小排序：", numbers)
