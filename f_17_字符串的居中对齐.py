poem = [
    "\t\n登鹳雀楼",
    "王之涣\r",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]
for sentence in poem:
    print("|%s|" % (sentence.strip().center(10),))
print(type((poem[0].center(10),)))
sentence = "\t\n\r樊家富\t\t"
print(sentence)
sentence.strip()
print(sentence)
print(sentence.strip())
