#encoding:utf-8

import sys,time

for i in range(20):
    percent = i / 20 * 100
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)