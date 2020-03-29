from flask import Flask, request, Response
import jsonpickle
import numpy as np
app = Flask(__name__)
import requests as req

url = 'http://localhost:80/Edge/3/1'

@app.route("/capture/", methods=['POST'])
def capture():
    
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_name = "opencv_frame_{}.png".format(0)
    # do some fancy processing here....
    cv2.imwrite(img_name, img)

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90)
