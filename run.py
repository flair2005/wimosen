import time
import local_common as lc
import params as pa

while pa.run:
    time.sleep(pa.delay) #100ms 0.01
    lc.fetch(pa.os_type)
