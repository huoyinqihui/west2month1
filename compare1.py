x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("由大到小排序：", z, y, x)
