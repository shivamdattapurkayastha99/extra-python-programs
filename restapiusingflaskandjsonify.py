# rest api using flask and jsonify using python
from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/armstrong/<int:n>')
def armstrong(n):
    n1=n
    s=0
    while n!=0:
        d=n%10
        s=s+d**3
        n//=10
    if s==n1:
        result={
        "Number":n1,   
        "Armstrong":True
        }


    else:
        result={
        "Number":n1,   
        "Armstrong":False
        }
    return result
if __name__ == "__main__":
    app.run(debug=True)
    