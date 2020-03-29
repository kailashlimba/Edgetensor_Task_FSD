
from flask import Flask, request, Response
import numpy as np
import jsonpickle
app = Flask(__name__)
import requests as req

url = 'http://localhost:80/Edge/3/1'

@app.route("/capture/")
def capture():
    while True:
        req.get(url)
        time.sleep(2)

@app.route("/store",methods=['POST'])
def store():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img_counter = 0
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, img)
    # do some fancy processing here....

    # build a response dict to send back to client
    # response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
    #             }

    # # encode response using jsonpickle
    # response_pickled = jsonpickle.encode(response)

    # return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90)
    