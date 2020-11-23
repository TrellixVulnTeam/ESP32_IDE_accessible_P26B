import pyb
from pyb import Pin
import time
class DHT11:
    def __init__(self,pin_name):
        time.sleep(1)
        self.N1 = Pin(pin_name, Pin.OUT_PP)
        self.PinName=pin_name
        pyb.delay(10)
    def read_data(self):
        self.__init__(self.PinName)
        data=[]
        j=0
        N1=self.N1
        N1.low()
        time.sleep(0.03)
        N1.high()
        N1 = Pin(self.PinName, Pin.IN)
        while N1.value()==1:
            continue
        while N1.value()==0:
            continue
        while N1.value()==1:
            continue
        while j<40:
            k=0
            while N1.value()==0:
                continue
            while N1.value()==1:
                k+=1
                if k>100:break
            if k<3:
                data.append(0)
            else:
                data.append(1)
            j=j+1
        
        j=0
        humidity_bit=data[0:8]
        humidity_point_bit=data[8:16]
        temperature_bit=data[16:24]
        temperature_point_bit=data[24:32]
        check_bit=data[32:40]
        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
        for i in range(8):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)
        tmp=humidity+humidity_point+temperature+temperature_point
        return [temperature,humidity]
