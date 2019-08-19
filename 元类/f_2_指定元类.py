def upper_attr(class_name, class_parents, class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    #调用type来创建一个类
    return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(Foo.BAR)
print(f.BAR)


def upper_attr(class_name, parent_class, class_attr):
    new_class_attr = dict()
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_class_attr[name.upper()] = value
    return type(class_name, parent_class, new_class_attr)


class Test(object, metaclass=upper_attr):
    bar = "hello"


print(hasattr(Test, "bar"))
print(hasattr(Test, "BAR"))
# print(Test.bar)
print(Test.BAR)
t = Test()
print(t.BAR)
