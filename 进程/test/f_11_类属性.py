class Tool:
    __count = 0

    def __init__(self, name):
        self.name = name
        Tool.__count += 1

    @classmethod
    def show_tool_count(cls):
        print("当前工具类创建的对象数:%d" % cls.__count)


tool1 = Tool("锤子")
tool2 = Tool("榔头")
tool3 = Tool("榔头")
# tool1.count = 99
# print(Tool.count)
# print(tool1.count)
# print(tool2.count)
Tool.show_tool_count()
