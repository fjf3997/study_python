name_list = [
    {"name": "张三"},
    {"name": "李四"}
]
find_name = "王五"
for name_dict in name_list:
    print(name_dict)
    if name_dict["name"] == find_name:
        print("找到了%s" % find_name)
        break
else:
    print("没有找到%s" % find_name)
print("循环结束")
