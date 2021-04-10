import os
from flask import Flask, render_template, jsonify
from flask import request
from Algorithm import Algorithm
from MemoryGame import MemoryGame

FILE_DIR = os.path.dirname(os.path.abspath(__file__))  # absolute path to this file
UPLOAD_FOLDER = os.path.join(FILE_DIR, 'data\images')
DESCRIPTORS_FOLDER = os.path.join(FILE_DIR, 'data\descriptors')
KEYPOINTS_FOLDER = os.path.join(FILE_DIR, 'data\keypoints')
RESULTS_FOLDER = os.path.join(FILE_DIR, 'data\\results')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DESCRIPTORS_FOLDER'] = DESCRIPTORS_FOLDER
app.config['KEYPOINTS_FOLDER'] = KEYPOINTS_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER


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

    # empty the UPLOAD folder first
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

    print("saving to folder: " + app.config['UPLOAD_FOLDER'])
    i = 1
    for file in files:
        if file and allowed_file(file.filename):
            filename = "img" + str(i) + ".jpeg"  # secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            i += 1
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


@app.route('/runAlgorithm', methods=['GET', 'POST'])
def run_algorithm():
    # empty the Descriptors, Keypoints and Results folders first
    for f in os.listdir(app.config['DESCRIPTORS_FOLDER']):
        os.remove(os.path.join(app.config['DESCRIPTORS_FOLDER'], f))
    for f in os.listdir(app.config['KEYPOINTS_FOLDER']):
        os.remove(os.path.join(app.config['KEYPOINTS_FOLDER'], f))
    for f in os.listdir(app.config['RESULTS_FOLDER']):
        os.remove(os.path.join(app.config['RESULTS_FOLDER'], f))

    algorithm = Algorithm()
    result = algorithm.run_algorithm()
    if result == "success":
        resp = jsonify({'message': 'Algorithm successfully run'})
        resp.status_code = 200
        return resp


@app.route('/runGame', methods=['GET', 'POST'])
def run_game():
    memory_game = MemoryGame()
    memory_game.run_game()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
