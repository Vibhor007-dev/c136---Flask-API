from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)
@app.route("/")

def index():
    return jsonify({
       "data":data,
        "message":"sucess"
}),200

@app.route("/planet")

def planet():
    name=request.args.get("name")
    planetData=next(item for item in data if item["name"]==name)

    return jsonify({
        "data":planetData,
        "message":"success"
    }),200

if __name__=="main":
    app.run()                
