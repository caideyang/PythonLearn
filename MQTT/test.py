import time,json


tag = True
while tag:
    # rack_ID = input("请输入监控单元ID：")
    rack_ID = "041558"
    # u_ID = input("请输入采集单元ID：")
    u_ID = "u-11"
    # c_ID = input("请输入控制通道ID：")
    c_ID = "led"
    # value = input("请输入值：")
    value = "0-1-0"
    timestamp = int(time.time())
    cov = True
    state = 0
    topic = "command/"+rack_ID+"/"+u_ID+"/"+c_ID
    msg = {
	        "monitoringUnitId": rack_ID,
	        "sampleUnitId": u_ID,
	        "channelId": c_ID,
	        "value": value,
	        "timestamp": timestamp, #"2018-01-01T12:00:00Z",
	        "cov": True,
	        "state": 0
    }
    print(json.dumps(msg))
    print(topic)
    print("2018-05-28 17:45:01,123 - mqttCli.py[line:20] - INFO: Topic:%s,Message:b\'%s\'" %(topic,json.dumps(msg)))
    tag = False