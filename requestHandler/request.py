from flask import Flask, render_template
import requests
import json
#this is a flask app
app = Flask("__name__")

@app.route("/")
@app.route("/getDetails")
def requestDetails():
    title = "Request Details API"
    return render_template("requestDetails.html", title = title)

@app.route("/sendRequest", methods=["POST"])
def sendRequest():
    val = requests.get("http://127.0.0.1:5000/request").content
    details = val.decode("utf-8")
    title = "Response Content"
    details = json.loads(details)
    return render_template("displayResponse.html", title=title, details=details)

if __name__=="__main__":
    app.run(port=5001, debug=True)
