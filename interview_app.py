# we are going to use a micro web framework called Flask
# goal is to create a web app for our simple /predict API service
import pickle 
import os 
from flask import Flask, jsonify, request 

app = Flask(__name__)

# we need to add a route (2 actually)
# a route for the homepage
# a route is a path on a server to a function that handles the request
@app.route("/", methods=["GET"])
def index():
    # need to return content and a response code
    return "<h1>Welcome to my App!!</h1>", 200

if __name__ == "__main__":
    # deployment notes
    # two main categories of deployment
    # host your own server OR use a cloud provider (AWS, Azure, Heroku, DigitalOcean,...)
    # we are going to use Heroku (BaaS, backend as a service)
    # there are quite a few ways to deploy a Flask app to Heroku
    # 1. deploy the app directly on an ubuntu "stack" (e.g. Procfile and requirements.txt)
    # 2. deploy the app as a Docker container on a container "stack" (e.g. Dockerfile)
    # 2.A. build a Docker image locally and push the image to a container registry (e.g. Heroku's registry) 
    # 2.B. define a heroku.yml and push your source code to Heroku's git and
    # Heroku is going to build the Docker image (and register it)
    # 2.C. define main.yml and push your source code to Github and a Github Action builds
    # the image and pushes the image to the registry (e.g. Heroku's registry)
    port = os.environ.get("PORT", 5000) # Heroku will set the PORT environment variable for web traffic
    app.run(debug=False, host="0.0.0.0", port=port) # set debug=False before deployment!!
