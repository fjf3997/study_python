def demo(name,title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("title[%s]%s是%s" % (title, name, gender_text))


demo("樊家富")
demo("席颖", gender=False)
