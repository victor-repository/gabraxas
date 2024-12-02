from flask import Flask
from socket import gethostbyname
from socket import gethostname

counter = 0
ip = gethostbyname(gethostname())
app = Flask(__name__)

@app.route("/")
def hello():
    global counter
    counter += 1  
    return "Hello World!!!     No.: " + str(counter) + "     IP:" + ip + "\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
