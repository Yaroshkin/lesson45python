import random

from flask import Flask
from flask import url_for, render_template, send_file, redirect
import datetime
import time as t
# import jsonify
import json, requests

app = Flask(__name__)


foot = "Serhii Yaroshkin\n+380-63-698-83-58"

@app.route('/')
def hello_world():  # put application's code here
    # return url_for('static', filename="index.html")
    # return send_file('static/index.html')
    global foot
    time = datetime.datetime.now()
    arr = ['Temperature','Water',8,3,7,6,8,1]
    return render_template("index.html", title=time, time=time, arr=arr, footer=foot)

@app.route('/hum')
def home():
    global foot
    time = datetime.datetime.now()
    title = 'Humidity'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    hum = json_data.get('humidity')
    return render_template('hum.html', title=title, hum=hum, time=time, footer=foot)

@app.route('/temperature')
def home_alone_2():
    global foot
    head1 = 'HEll'
    time = datetime.datetime.now()
    title = 'Temperature'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    temp = json_data.get('temperature')
    return render_template('temp.html',title=title,temp=temp,time=time,head1=head1, footer=foot)

@app.route('/meter')
def meter():
    global foot
    title = 'Meter'
    return render_template('meter.html',title=title)

@app.route('/meter/ele')
def ele():
    global foot
    time = datetime.datetime.now()
    title = 'Electricity'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    met = json_data['meter']['electricity']['reading']
    met1 = json_data['meter']['electricity']['consumption']
    return render_template('ele.html',ele=met,ele1=met1,title=title,footer=foot)

@app.route('/meter/gaz')
def gaz():
    global foot
    time = datetime.datetime.now()
    title = 'Gaz'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    gaz = json_data['meter']['gas']['reading']
    gaz_n = json_data['meter']['gas']['consumption']
    return render_template('gaz.html',gaz=gaz,gaz1=gaz_n,title=title,footer=foot)

@app.route('/meter/water')
def wat():
    global foot
    time = datetime.datetime.now()
    title = 'Water'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    wat = json_data['meter']['water']['reading']
    wat_n = json_data['meter']['water']['consumption']
    return render_template('water.html',water=wat,water1=wat_n,title=title,footer=foot)

@app.route('/boiler')
def boil():
    global foot
    time = datetime.datetime.now()
    title = 'Boiler'
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    boil = json_data['boiler']['isRun']
    boil_tem = json_data['boiler']['temperature']
    boil_pre = json_data['boiler']['pressure']
    return render_template('boiler.html',boil=boil,boil1=boil_tem,boil2=boil_pre,title=title,footer=foot)

@app.route('/home2')
def api():
    obj = None
    with open('static/example.json', 'r') as file:
        obj = json.load(file)

    obj['temperature'] = random.randint(-15, 25)
    obj['humidity'] = random.randint(0, 100)
    obj['meter']['electricity']['reading'] = round(random.uniform(12345.9, 12347.9), 3)
    obj['meter']['electricity']['consumption'] = round(random.uniform(0.1, 2.0), 1)
    obj['meter']['gas']['reading'] = round(random.uniform(2367.9, 2369.9), 3)
    obj['meter']['gas']['consumption'] = round(random.random(), 1)
    obj['meter']['water']['reading'] = round(random.uniform(1212.9, 1214.9), 3)
    obj['meter']['water']['consumption'] = round(random.uniform(0.1, 1.0), 1)
    obj['boiler']['isRun'] = random.choice([True, False])
    obj['boiler']['temperature'] = random.randint(60, 65)
    obj['boiler']['pressure'] = round(random.uniform(1.0, 2.0), 1)

    return json.dumps(obj)
    # return json.dumps(dict1)




if __name__ == '__main__':
    app.run(debug=True)
