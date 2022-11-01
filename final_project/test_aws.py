from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import numpy as np

mqttclient = AWSIoTMQTTClient("Aiot")
mqttclient.configureEndpoint("a26gvpee2b66bd-ats.iot.us-west-2.amazonaws.com",8883)
mqttclient.configureCredentials(CAFilePath="root-CA.crt",KeyPath="./aiot.private.key",CertificatePath="./aiot.cert.pem")
mqttclient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
mqttclient.configureDrainingFrequency(2) # Draining: 2 Hz
mqttclient.configureConnectDisconnectTimeout(10) # 10 sec
mqttclient.configureMQTTOperationTimeout(5) # 5 sec

img = np.array([1,2,3])

img = np.array2string(img)


lst = []

def callback(self,param,data):

    # print(data.payload)
    
    lst.append(data.payload)


mqttclient.connect()

count = 0

while True:
  
    mqttclient.publish("test/pc",payload=img+str(count),QoS=1)

    print(img)

    count+=1
    # mqttclient.subscribe("test/iot",QoS=1,callback=callback)
    
    # try:
    
    #     img2 = lst[-1].decode()
    
    #     print(img2)
      
    # except:
        
    #     continue
    
    