#hardware platform:FireBeetle-ESP8266

time.sleep(0.1)
print(i2c.readfrom_mem(0x50,0,7,addrsize=16))   #Read 7 bytes from the slave specified by 0x50 starting from the memory address specified by 0. 