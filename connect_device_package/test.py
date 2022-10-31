from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


mqttclient = AWSIoTMQTTClient("Aiot")

mqttclient.configureEndpoint("a26gvpee2b66bd-ats.iot.us-west-2.amazonaws.com",8883)

mqttclient.configureCredentials(CAFilePath="root-CA.crt",KeyPath="./aiot.private.key",CertificatePath="./aiot.cert.pem")


mqttclient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
mqttclient.configureDrainingFrequency(2) # Draining: 2 Hz
mqttclient.configureConnectDisconnectTimeout(10) # 10 sec
mqttclient.configureMQTTOperationTimeout(5) # 5 sec


def callback(self,param,data):

    print(data.payload)

mqttclient.connect()

count = 0
    
while True:
    # mqttclient.subscribe("aiot/test",0,callback)
    
    s = str(count)
    
    mqttclient.publish("aiot/test",payload=s,QoS=1)
    
    count+=1