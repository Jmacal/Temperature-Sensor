import subprocess
import time
from flask import Flask, render_template
import json

app=Flask(__name__)

@app.route('/data')
def outputdata():
    Temperature,Time=collectdata()
    datavalues={ 'Temperature': Temperature,
                 'Time': Time
                 }
    print(Temperature)
    print(Time)

     
    return json.dumps(datavalues)

@app.route('/')
def outputwebpage():
    return render_template('index.html')
    


def collectdata():
    temp=subprocess.check_output("pcsensor")
    Time=temp[:19]
    celcius=float(temp[39:(len(temp)-2)])

    return celcius,Time
         



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

