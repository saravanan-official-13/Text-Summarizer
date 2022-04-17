import requests
import os
from wsgiref import simple_server
from flask import Flask,render_template,url_for
from flask_cors import CORS, cross_origin
from flask import request as req

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET","POST"])
@cross_origin()
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
@cross_origin()
def Summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/Saravananofficial/Text_Summarizer"
        headers = {"Authorization": f"Bearer api_cDqsshiYYdsPmHybqxvnlZYIctoHFwMovw"}
        data=req.form["data"]
        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
