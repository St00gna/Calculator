
from flask import Flask, request, jsonify
from calculator import calculator
from files import check_file_format
import os


app = Flask(__name__)


@app.route('/api/process_file', methods=['POST'])
def process_file():
    file = request.files['file']
    cur_dir = os.getcwd()
    filename = file.filename
    file_path = os.path.join(cur_dir, filename)
    file.save(file_path)

    text = check_file_format('./file').split()

    results = {}
    for element in text:
        result = calculator(element)
        results.update({element: str(result)})

    return jsonify(results)




