import cv2 as cv
img = cv.imread("E:\OPENCV\opencv test\opencv test\img.jpg")
cv.namedWindow("picture")
cv.imshow("picture",img)
cv.waitKey(0)
cv2.destroyAllWindows() 