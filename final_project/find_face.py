import cv2
import numpy as np
from keras.models import load_model



model = load_model("face.h5")
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

t = ["Sue","Simon","Who are you?"]



while True:   
         
        success,img = cap.read()    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        

        
        faces = face_detector.detectMultiScale(gray,1.5,5)
                
        for (x, y, w, h) in faces:
                    
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0))

        try:
                gray = gray[y:y+h,x:x+w]

                gray = cv2.resize(gray,(50,50))
        
        except:
                
                 gray = cv2.resize(gray,(50,50))
                 
        result = model.predict(gray.reshape(-1,50,50,1))[0]
    
        idx = result.argmax()

        confidence = result.max()*100

        if confidence >=70:
        
                print(t[idx])
        

        else:
        
                print(t[2])

   
        

     
        cv2.imshow("result",img)        
        cv2.waitKey(1)        
         
        