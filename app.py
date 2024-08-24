from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'sum': a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
