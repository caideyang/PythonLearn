#encoding:utf-8

import logging

"""
日志一共分成5个等级，从低到高分别是：DEBUG INFO WARNING ERROR CRITICAL。

DEBUG：详细的信息,通常只出现在诊断问题上
INFO：确认一切按预期运行
WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
ERROR：更严重的问题,软件没能执行一些功能
CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行

这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。

有两种方式记录跟踪，一种输出控制台，另一种是记录到文件中，如日志文件

"""

#定义日志级别和输出格式
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#将日志输出到log.txt文件
logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='a+',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')

