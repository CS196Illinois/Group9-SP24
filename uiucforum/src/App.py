from flask import Flask, jsonify, request
import csv
from flask_cors import CORS
app = Flask(__name__)

app.config['SECRET_KEY'] = 'sdmak12n292edf9nrn1f1d9end1'

posts = []

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/api/posts', methods=['POST'])
def post():
    # Get data from the request
    data = request.json
    posts.append(data)

    return jsonify({'message': 'Post submitted successfully'})

@app.route('/api/posts1', methods=['GET'])
def post1():
    return jsonify(posts)


@app.route('/data')
def data():
    class_values = []
    number_values = []
    name_values = []

    with open('class_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            class_values.append(row['Class'])
            number_values.append(row['Number'])
            name_values.append(row['Name'])

    unique_classes = list(set(class_values))
    unique_numbers = list(set(number_values))
    unique_names = list(set(name_values))
    unique_classes.sort()
    unique_numbers.sort()
    unique_names.sort()

 
    return jsonify({"unique_classes": unique_classes, "unique_numbers": unique_numbers, "unique_names": unique_names})

CORS(app, origins='*')



@app.route('/')
def home():
    return "hello"

                                                 
if (__name__) == '__main__':
    app.run(debug=True)
