import cv2
import time
from flask import Flask
import requests as req

# app = Flask(__name__)
# frequency in seconds


url = 'http://localhost:90/capture'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# @app.route("/Edge/<string:frequency>/<string:grayscale>")
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
        if int(grayscale):
            cv2.imwrite(img_name, gray)

        print("{} written!".format(img_name))
        img_counter += 1

        req.post(url,image)

        _, img_encoded = cv2.imencode('.jpg', image)
        # send http request with image and receive response
        response = req.post(url, data=img_encoded.tostring(), headers=headers)
        print(json.loads(response.text))
        time.sleep(int(frequency))


capture_image(5,1)
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)
