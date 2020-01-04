from flask import Flask, jsonify, request
from flask_cors import CORS
import trainer
app = Flask(__name__)
CORS(app)

@app.route('/api/talk',methods=['POST'])
def index():
    user_input = request.json['user_input']
    return jsonify({'msg':str(trainer.brain(user_input))})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 