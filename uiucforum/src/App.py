from flask import Flask, jsonify
import csv
from flask_cors import CORS
app = Flask(__name__)

app.config['SECRET_KEY'] = 'sdmak12n292edf9nrn1f1d9end1'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

'''@app.route('/submit-post', methods=['POST'])
def submit_post():
    data = request.json
    username = data.get('username')
    class1 = data.get('class1')
    number = data.get('number')
    title = data.get('title')
    body = data.get('body')
    '''



@app.route('/data')
def data():
    class_values = []
    number_values = []

    with open('class_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            class_values.append(row['Class'])
            number_values.append(row['Number'])

    unique_classes = list(set(class_values))
    unique_numbers = list(set(number_values))
    unique_classes.sort()
    unique_numbers.sort()
 
    return jsonify({"unique_classes": unique_classes, "unique_numbers": unique_numbers})

CORS(app, origins='*')



@app.route('/')
def home():
    return "hello"

                                                 
if (__name__) == '__main__':
    app.run(debug=True)
