import pySynaptics

#check all function in pySynaptics

ret=pySynaptics.i2c_write(0x2c, [0x20,0x00])

if ret == 1:
    print("i2c_write not supported")
    exit()


ret_data=pySynaptics.i2c_read(0x2c, 30)
if ret_data == None:
    print("i2c_read not supported")
else:
    print("i2c_read: ", ret_data)