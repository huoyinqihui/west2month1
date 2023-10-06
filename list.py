input_list = input("请输入一个列表，包含字符串和整数，用逗号分隔：").split(',')
integer_list = [int(item) for item in input_list if item.isdigit()]
print("升序排序后的整数列表：",sorted(integer_list))
