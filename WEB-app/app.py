import json
from flask import Flask, render_template, jsonify
from flask import request
from MemoryGame import MemoryGame

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


@app.route('/runGame', methods=['GET'])
def runGame():
    MemoryGame.run_game()


@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    memory_game = MemoryGame()

    memory_game.run_game()

# @app.route('/signUpUser', methods=['POST'])
# def signUpUser():
#     if request.method == 'POST':
#         predictions = []
#
#     for key in ['product', 'address']:
#         field_val = request.form[key]
#
#         prediction = model.predict_our_model(field_val)
#
#         pred_obj = {
#             "field": key,
#             "field_val": field_val,
#             "prediction": prediction,
#         }
#         predictions.append(pred_obj)
#
#     return jsonify(render_template('dynamic_data.html', predictions=predictions))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
