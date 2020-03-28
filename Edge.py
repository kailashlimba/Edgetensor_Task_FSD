import cv2
import time
# frequency in seconds

def capture_image(frequency):
    img_counter = 0
    while True:
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        cam.release()
        cv2.destroyAllWindows()
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        time.sleep(5)

capture_image(5)