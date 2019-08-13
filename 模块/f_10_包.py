import f_package

f_package.f_send_message.send("hello,是我,fjf")
txt = f_package.f_receive_message.receive()
print(txt)