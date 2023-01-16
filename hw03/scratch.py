import time
import smbus
import gpiod

EncPath1 = '/sys/bus/counter/devices/counter1/count0'
f = open(EncPath1+'/ceiling', 'w')
f.write('500')
f.close()
f = open(EncPath1+'/count', 'w')
f.write('250')
f.close()
f = open(EncPath1+'/enable', 'w')
f.write('1')
f.close()
f = open(EncPath1+'/count','r')

old = int(f.read())
while True:
    f.seek(0)
    new = int(f.read())
    up = (old < new)
    down = not up
    print('up', up)
    print('down',down)
    old = new
    time.sleep(0.5)