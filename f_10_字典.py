fjf = {"name": "樊家富",
       "age": 18,
       "gender": True,
       "height": 185,
       "weight": 70}
# 取值
print(fjf["name"])
# 修改增加
fjf["hobby"] = "basketball"
fjf["name"] = "cxk"

# 删除
fjf.pop("name")
# 求取键值对的长度
print(len(fjf))
# 更新字典
temp = {"country": "china",
        "age": 20}
fjf.update(temp)
# 情况字典
fjf.clear()
print(fjf)
