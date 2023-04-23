#  Created by btrif Trif on 23-04-2023 , 11:40 AM.
# https://dataanalyticsireland.ie/2022/03/28/how-to-pass-python-variables-to-javascript/
# https://www.youtube.com/watch?v=rq4t_JK91Xc


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = ['Joe','John','Jim','Paul','Niall','Tom']
    return render_template('index.html', name=name)



if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True)