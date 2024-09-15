import cv2
import os

# Load the image in grayscale
img = cv2.imread("pika.png", 0)
cv2.imshow("Pikachu in Grayscale", img)
cv2.waitKey(0)

# Save the image
saved_directory = "C:/Downloads/Jetlearn/temp"
os.chdir(saved_directory)
cv2.imwrite("pikaBlackWhite.png", img)
print(f"Successfully saved pikaBlackWhite.png")

# Load the image again in color mode
img = cv2.imread("pika.png", 1)
cv2.imshow("Original", img)
cv2.waitKey(0)

# Split the image into its BGR channels
B, G, R = cv2.split(img)
cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(0)
cv2.imshow("Green Saturation Image", G)
cv2.waitKey(0)
cv2.imshow("Red Saturation Image", R)
cv2.waitKey(0)

cv2.destroyAllWindows()