names = ['fjf', 'fjf2', 'fjf3', "fjf", "fjf2"]
len_list = len(names)
print("列表的长度为%d" % len_list)
count = names.count("fjf")
print("列表中fjf出现了%d次" % count)
# 只删除出现的第一个
names.remove("fjf")
print(names)

