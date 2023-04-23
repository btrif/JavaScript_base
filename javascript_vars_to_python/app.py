#  Created by btrif Trif on 23-04-2023 , 11:40 AM.
# https://dataanalyticsireland.ie/2021/12/13/how-to-pass-a-javascript-variable-to-python-using-json/

import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output) #this converts the json output to a python dictionary
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary
    return result



if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True)