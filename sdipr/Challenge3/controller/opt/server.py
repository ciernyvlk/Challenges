from flask import Flask, jsonify, request, make_response
import requests
import os

app = Flask(__name__)


@app.route('/%s/test' % os.environ['SECRET'], methods=['GET'])
def test():
    return make_response('OK', 200)


@app.route('/' + os.environ['SECRET'], methods=['POST'])
def solution_check():
    submitted_solution = request.json['solution']
    
    if submitted_solution != 'G00d':
         return jsonify(solved=False)
         
    return jsonify(solved=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=False)
