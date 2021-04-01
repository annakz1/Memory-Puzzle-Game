import json
import os
from flask import Flask, render_template, jsonify
from flask import request
from MemoryGame import MemoryGame
from werkzeug.utils import secure_filename

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(FILE_DIR, 'data\images')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        print("saving to folder: " + app.config['UPLOAD_FOLDER'])
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 206
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp


@app.route('/runGame', methods=['GET', 'POST'])
def runGame():
    print("in Run Game")
    memory_game = MemoryGame()
    memory_game.run_game()


# @app.route('/signUpUser', methods=['POST'])
# def signUpUser():
#     pass
# memory_game = MemoryGame()
#
# memory_game.run_game()

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
