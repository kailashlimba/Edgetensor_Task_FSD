
from flask import Flask
app = Flask(__name__)
import requests as req

url = 'http://localhost:80/Edge/3/1'

@app.route("/capture/")
def capture():
    while True:
        req.get(url)
        time.sleep(2)

    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90)
    