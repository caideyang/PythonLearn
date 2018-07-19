import time


res = time.time() #1527043742.3463285
res = time.asctime() #Wed May 23 10:48:46 2018
res = time.clock() #0.0

res = time.strftime("%Y-%m-%d %X") #2018-05-23 10:50:17

res = time.ctime() #Wed May 23 10:50:52 2018
res = time.ctime(1527043742) #Wed May 23 10:49:02 2018
res = time.altzone #-32400
res = time.localtime() #time.struct_time(tm_year=2018, tm_mon=5, tm_mday=23, tm_hour=10, tm_min=51, tm_sec=57, tm_wday=2, tm_yday=143, tm_isdst=0)
res = time.strftime("%Y-%m-%d %X",time.localtime()) #2018-05-23 10:53:01
res = time.gmtime(1527043742) #time.struct_time(tm_year=2018, tm_mon=5, tm_mday=23, tm_hour=2, tm_min=49, tm_sec=2, tm_wday=2, tm_yday=143, tm_isdst=0)
res = time.process_time() #0.765625
res = time.strptime('2018-05-23 10:53:01',"%Y-%m-%d %X") #time.struct_time(tm_year=2018, tm_mon=5, tm_mday=23, tm_hour=10, tm_min=53, tm_sec=1, tm_wday=2, tm_yday=143, tm_isdst=-1)
print(res)