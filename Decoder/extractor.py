import cv2
from pyzbar import pyzbar
from Decoder.data import enhance_data

def color_remove(file):
    file=str(file)+'.png'
    img_array1 = cv2.imread(file)
    img_array2 = cv2.imread(file)
    img_array3 = cv2.imread(file)
    # note that [:,:,0] is blue, [:,:,1] is green, [:,:,2] is red
    img_array1[:, :, 1] = 0
    img_array1[:, :, 2] = 0
    #mask = cv2.inRange(img_array1, (0, 0, 0), (200, 200, 200))
    #thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #inverted = 255 - thresholded
    cv2.imwrite("Decoder/3.png", img_array1)
    str1=enhance_data(str(3))
    # cv2.imwrite("redblue.jpg", img_array)
    img_array2[:, :, 2] = 0
    img_array2[:, :, 0] = 0
    #mask = cv2.inRange(img_array2, (0, 0, 0), (200, 200, 200))
    #thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #inverted = 255 - thresholded
    cv2.imwrite("Decoder/2.png", img_array2)
    str2=enhance_data(str(2))
    
    img_array3[:, :, 0] = 0
    img_array3[:, :, 1] = 0
    #barcode3 = pyzbar.decode(img_array2) #Alternative way
    #print(barcode3)
    #mask = cv2.inRange(img_array3, (0, 0, 0), (200, 200, 200))
    #thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #inverted = 255 - thresholded
    cv2.imwrite("Decoder/1.png", img_array3)
    str3=enhance_data(str(1))
    try:
        str1=str1[0][0].decode()
        str2=str2[0][0].decode()
        str3=str3[0][0].decode()
    except IndexError:
        print("Not decoded, possibly try with a better image.")
        return
    
    print("Data string decoded: "+str3+str2+str1)
