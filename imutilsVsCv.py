from imutils.video import VideoStream
import imutils
import cv2
import time
#coding ini utk menunjukkan perbedaan video stream antar imutils dan opencv

#mendeklarasikan variabel fps live
prev_frame_time = 0
new_frame_time = 0

#perlu diperhatikan, keduanya berbeda dalam memanggil video live capture
#cap = cv2.VideoCapture(0)
cap2 = VideoStream(src=0).start()


while True:
    
    #jika memakai opencv, harus memakai successor di dpn
    #jika memakai imutils, tidak usah, langsung variabel
    #success, img = cap.read()
    imgGray = cap2.read()
    
    imgGray = cv2.resize(imgGray, (640, 480))
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    new_frame_time = time.time()
    #menghitung fps
    fps = int(1/(new_frame_time-prev_frame_time))
    fpsShow = ("FPS live: {0} fps".format(fps))
    prev_frame_time = new_frame_time

    cv2.putText(imgGray, fpsShow, (7,50), font, 2, (255,0,0), 3)

    #cv2.imshow("Opencv", imgGray)
    cv2.imshow("Imutils", imgGray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
