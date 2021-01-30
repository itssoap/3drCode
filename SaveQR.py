import cv2
from pyzbar import pyzbar
import numpy as np
from PIL import Image
from time import sleep

def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    
    while ret:
        sleep(.5)
        ret, frame = camera.read()
        barcode_info=None
        pts=np.zeros((4,1,2))
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
             x, y , w, h = barcode.rect
        #1
            
             barcode_info = barcode.data.decode('utf-8')
             pts = np.array([barcode.polygon], np.int32)
             pts = pts.reshape(-1,1,2)
        #cropped = frame[pts]
        #cv2.imwrite('cropped.jpg', cropped)
             cv2.polylines(frame, [pts], True, (0, 255, 0), 1)
        x1=pts[0][0][0]
        y1=pts[0][0][1]
        x2=pts[1][0][0]
        y2=pts[1][0][1]
        x3=pts[2][0][0]
        y3=pts[2][0][1]
        x4=pts[3][0][0]
        y4=pts[3][0][1]
        
        top_left_x = min([x1,x2,x3,x4])
        top_left_y = min([y1,y2,y3,y4])
        bot_right_x = max([x1,x2,x3,x4])
        bot_right_y = max([y1,y2,y3,y4])
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27 or barcode_info!=None:
             cv2.imwrite('Capture.png', frame[top_left_y:bot_right_y+1, top_left_x:bot_right_x+1])
             print(pts)
             break
        
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()