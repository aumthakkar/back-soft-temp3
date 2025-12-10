
from flask import Flask, jsonify
import socket
import time


app = Flask(__name__)

@app.route('/api/v1/info')
# ‘/’ URL is bound with hello_world() function.
def info():
    return jsonify({
        "hostname" : socket.gethostname(),
        "time" : time.ctime(),
        "app_name" : "${{values.app_name}}",
        "env": "${{values.app_env}}",
        "deployed_on" : "kubernetes",
        "msg" : "Hello, this is Pranav here!"
    })

@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def healthz():
    return jsonify({
        "status" : "up"
    })

# main driver function
if __name__ == '__main__':

    app.run(host="0.0.0.0")