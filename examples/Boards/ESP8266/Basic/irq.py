#hardware platform: FireBeetle-ESP8266import machinefrom machine import Pinimport timevalue=1counter=0def func(v):  global value,counter  time.sleep_ms(50)  if(button.value() == 0):    return  while(button.value() == 1):                       #If press the button, it will wait until released    time.sleep_ms(100)  time.sleep_ms(100)  counter+=1  led.value(value)  value = 0 if value else 1                         #If LED is turn on,it will be shutdown next,otherwise it will turn on next.  print("IRQ ",counter)  try:  led = Pin(13, Pin.OUT)                              #create LED object from pin13,Set Pin13 to output  led.value(0)  button = Pin(15, Pin.IN)                            #create Button object from pin15,Set Pin15 to input  button.irq(trigger=Pin.IRQ_RISING, handler=func)    #init irq,set interrupt on rising edge,and callback function is func  while True:    passexcept:  machine.disable_irq()