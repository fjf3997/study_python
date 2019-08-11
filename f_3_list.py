names = ['fjf', 'fjf2', 'fjf3']
# 取值和去索引
print(names[0])
print(names.index("fjf"))
# 修改
names[names.index("fjf")] = "樊家富"
# 添加
names.insert(1, "李四")
names.append("王五")
tem = ["吴昊", "周童", "张凯伦"]
names.extend(tem)
# 删除
names.pop()
names.pop(1)
names.remove("fjf2")
# names.clear()
print(names)
