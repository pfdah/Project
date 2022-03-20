import uuid
import os
import cv2

def captureVids(stName):
    print('hit',stName)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        #set frame
        ret, frame = cap.read()
        cv2.imshow('Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            #write the file
            os.makedirs(os.path.join('train_img','{}'.format(stName)))
            for i in range(100):
                imgName = os.path.join('train_img','{}'.format(stName), '{}.jpg'.format(uuid.uuid1()))
                cv2.imwrite(imgName, frame)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()