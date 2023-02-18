from flask import Flask
from flask import url_for, render_template, send_file, redirect
import datetime
import time as t
# import jsonify
import json,requests

app = Flask(__name__)




@app.route('/')
def hello_world():  # put application's code here
    # return url_for('static', filename="index.html")
    # return send_file('static/index.html')
    time = datetime.datetime.now()
    arr = ['Temperature','Water',8,3,7,6,8,1]
    return render_template("index.html", title=time, head1="head", time=time, arr=arr, sleep=t.sleep)

@app.route('/home')
def home():
    return 'Home!'

@app.route('/home2')
def home_alone_2():
    time = datetime.datetime.now()
    title = 'Temperature'
    response = requests.get("http://localhost:8000/cgi-bin/rest.py")
    json_data = json.loads(response.text)
    temp = json_data.get('temperature')
    return render_template('temp.html',title=title,temp=temp,time=time)

# @app.route('/home2')
# def api():
#     dict1 = {
#         "key1":"value1",
#         "key2": "value2",
#     }
#     return json.dumps(dict1)


if __name__ == '__main__':
    app.run(debug=True)
