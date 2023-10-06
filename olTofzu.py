input_str = input("请输入一个字符串：")
if "ol" in input_str:
    modified_str = input_str.replace("ol", "fzu")
    reversed_str = modified_str[::-1]
    print("替换后的字符串并倒序输出：", reversed_str)
else:
    print("字符串中不含有\"ol\"子串。")
