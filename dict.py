# 创建一个空字典
student_dict = {}

# 添加学号和姓名元素
student_dict[101] = "小A"
student_dict[102] = "小B"
student_dict[103] = "小C"
student_dict[104] = "小D"
student_dict[105] = "小E"

# 删除学号尾号为偶数的元素
keys_to_remove = []
for key in student_dict:
    if key % 2 == 0:  # 判断学号尾号是否为偶数
        keys_to_remove.append(key)

for key in keys_to_remove:
    del student_dict[key]

# 输出最终的字典
print("最终的字典：", student_dict)
