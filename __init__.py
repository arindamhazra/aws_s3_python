from flask import Flask, render_template,request,redirect
from datetime import datetime
import json
from werkzeug.security import *


app = Flask(__name__)
app.config.from_object("base_config")

from connect import *

@app.route("/")
@app.route("/home")
def home():
    bucket_list = s3.list_buckets()
    # ['Buckets']
    # buckets = [bucket for bucket in bucket_list['Buckets']]
    # owner = bucket_list['Owner']
    buckets = []
    for bucket in bucket_list['Buckets']:
        #print (bucket)
        bucket_info = {
            'Name': bucket['Name'],
            'CreationDate': str(bucket['CreationDate'])
#oDate = datetime.datetime.strptime(sDate, '%Y-%m-%d %H:%M:%S.%f'
        }
        buckets.append(bucket_info)
    print (json.dumps(buckets))
    #return render_template("index.html",bucket_list = buckets,owner = owner)
    return render_template("index.html",bucket_list = buckets)

@app.route("/showSignIn")
def showSignIn():
    return render_template("signIn.html")

@app.route("/showSignUp")
def showSignUp():
    return render_template("signUp.html")

@app.route("/showAbout")
def showAbout():
    return render_template("about.html")

@app.route("/showContactUS")
def showContactUs():
    return render_template("contactUs.html")


if __name__ == "__main__":
    app.run(debug=True)
