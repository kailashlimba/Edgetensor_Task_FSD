import cv2
import time
# frequency in seconds

def capture_image(frequency,grayscale):
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
        image = cv2.imread(img_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Original image',image)
        # cv2.imshow('Gray image', gray)
        if grayscale:
            cv2.imwrite(img_name, gray)

        print("{} written!".format(img_name))
        img_counter += 1
        time.sleep(5)

capture_image(5,1)