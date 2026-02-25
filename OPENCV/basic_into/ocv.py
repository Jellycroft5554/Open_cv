#Reading and displaying an image using OpenCV
import cv2
img = cv2.imread("Pika.png", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Pikachu Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
