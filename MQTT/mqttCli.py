#-*-coding:utf-8-*-
import paho.mqtt.client as mqtt
import  logging,json
import time,datetime

print(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
# logging.basicConfig(level=logging.INFO,
#                     filename='log.txt',
#                     filemode='a+',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = './log/logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 当连接上服务器后回调此函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # 放在on_connect函数里意味着
    # 重新连接时订阅主题将会被更新
    client.subscribe("command/#")
    # client.subscribe("sample-values/#")

# 从服务器接受到消息后回调此函数
def on_message(client, userdata, msg):
    res = "Topic:"+msg.topic+" Message:"+str(msg.payload)
    logger.info(res)

print(time.asctime())

client = mqtt.Client()
#参数有 Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client.on_connect = on_connect #设置连接上服务器回调函数
client.on_message = on_message  #设置接收到服务器消息回调函数
client.connect("192.168.1.113", 1883, 60)  #连接服务器,端口为1883,维持心跳为60秒
# client.loop_start()
# print()

while True:
    # rack_ID = input("请输入监控单元ID：")
    rack_ID = "04156D"
    # u_ID = input("请输入采集单元ID：")
    u_ID = "u-1"
    # c_ID = input("请输入控制通道ID：")
    c_ID = "led"
    # value = input("请输入值：")
    value = "0-1-0"
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    cov = True
    state = 0
    topic = "command/"+rack_ID+"/"+u_ID+"/"+c_ID
    msg = {
	        "monitoringUnit": rack_ID,
	        "sampleUnit": u_ID,
	        "channel": c_ID,
            "parameters": {
                "r":-1,
                "g":-1,
                "b":-1
            },
        "phase": "executing",
        "timeout":1000,
        "priority":0,
        "operator":"admin",
	    "startTime": timestamp, #"2018-01-01T12:00:00Z",
    }
    print(json.dumps(msg))
    print(topic)
    client.publish(topic, json.dumps(msg))
    break
client.loop_forever()