file_read = open("README")
file_write = open("README[复件]", "w")
while True:
    txt = file_read.readline()
    if not txt:
        break
    file_write.write(txt)

file_read.close()
file_write.close()
