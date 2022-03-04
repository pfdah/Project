import uuid
import os
import cv2

def captureVids(stName):
    print('hit',stName)
    
    cap = cv2.VideoCapture('./vid.mp4')
    while cap.isOpened():
        #set frame
        ret, frame = cap.read()
        name = stName
        cv2.imshow('Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            #write the file
            os.makedirs(os.path.join('train_img','{}'.format(name)))
            for i in range(50):
                imgName = os.path.join('train_img','{}'.format(name), '{}.jpg'.format(uuid.uuid1()))
                cv2.imwrite(imgName, frame)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()