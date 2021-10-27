from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey MuZakkir, I am from Server-1..How may I help you??'
#@app.route('/server1')
#def index2():
#    return 'Hey MuZakkir, I am from Server-1..How may I help you??'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 5001)

