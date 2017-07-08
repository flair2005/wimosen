import time
import local_common as lc
import params as pa
import visualize as viz

#viz.initvis()

while pa.run:
    time.sleep(pa.delay) #100ms 0.01
    ret =  lc.fetch().rssi
