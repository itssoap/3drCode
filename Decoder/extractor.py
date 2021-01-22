import cv2

def color_remove():
    img_array1 = cv2.imread("temp.jpg")
    img_array2 = cv2.imread("temp.jpg")
    img_array3 = cv2.imread("temp.jpg")
    # note that [:,:,0] is blue, [:,:,1] is green, [:,:,2] is red
    img_array1[:, :, 1] = 0
    img_array1[:, :, 2] = 0
    mask = cv2.inRange(img_array1, (0, 0, 0), (200, 200, 200))
    thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    inverted = 255 - thresholded
    cv2.imwrite("1.jpg", inverted)
    # cv2.imwrite("redblue.jpg", img_array)
    img_array2[:, :, 2] = 0
    img_array2[:, :, 0] = 0
    mask = cv2.inRange(img_array2, (0, 0, 0), (200, 200, 200))
    thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    inverted = 255 - thresholded
    cv2.imwrite("2.jpg", inverted)

    img_array3[:, :, 0] = 0
    img_array3[:, :, 1] = 0
    mask = cv2.inRange(img_array3, (0, 0, 0), (200, 200, 200))
    thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    inverted = 255 - thresholded
    cv2.imwrite("3.jpg", inverted)
