import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

mode = "canny"

print("Press:")
print("1 - Canny")
print("2 - Sobel")
print("3 - Laplacian")
print("q - Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    if mode == "canny":
        output = cv2.Canny(blurred, 50, 150)
        title = "Canny Edge Detection"

    elif mode == "sobel":
        sx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        output = cv2.addWeighted(
            cv2.convertScaleAbs(sx), 0.5,
            cv2.convertScaleAbs(sy), 0.5, 0
        )
        title = "Sobel Edge Detection"

    elif mode == "laplacian":
        output = cv2.convertScaleAbs(cv2.Laplacian(blurred, cv2.CV_64F))
        title = "Laplacian Edge Detection"

    cv2.imshow("Original", frame)
    cv2.imshow(title, output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        mode = "canny"
    elif key == ord('2'):
        mode = "sobel"
    elif key == ord('3'):
        mode = "laplacian"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
