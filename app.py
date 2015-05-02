from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/logdata')
def logdata():
    # Expecting Data in GET variables
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
