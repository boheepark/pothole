from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/pothole/')
def pothole(name=None):
    return render_template('base.html')

@app.route('/logdata', methods=['POST', 'GET'])
def logdata():
    lat = request.args.get('lat', '')
    long = request.args.get('long', '')
    z = request.args.get('z', '')
    output = '{ "lat": ' + lat + ', "long": ' + long + ', "z": ' + z + ' }'
    return output
    # return render_template('logdata.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
