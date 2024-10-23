from flask import Flask, request, jsonify, send_from_directory
import os
import random
from flask_cors import CORS
from question_bank import QuestionBank
from quiz_bank import QuizBank
from googlesearch import search
import logging
from waitress import serve

app = Flask(__name__)
CORS(app)

# setup
UPLOAD_FOLDER = r'BackEnd\content_hub'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

question_bank = QuestionBank()

quiz_bank = QuizBank()

# Content Hub
@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'File uploaded successfully', 200

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return 'File deleted successfully', 200
    except FileNotFoundError:
        return 'File not found', 404

# Question & Answer
@app.route('/get_questions', methods=['POST'])
def get_questions():
    data = request.json
    subject = data.get('subject')
    difficulty = data.get('level')
    num_questions = int(data.get('num_questions'))
    questions, answers = question_bank.get_questions_and_answers(subject, difficulty, num_questions)
    if questions is None:
        return jsonify({'error': 'Invalid subject or difficulty level'}), 400
    return jsonify({'questions': questions, 'answers': answers})

@app.route('/verify_answer', methods=['POST'])
def verify_answer():
    data = request.json
    question = data.get('question')
    answer = data.get('answer')
    user_answer = data.get('user_answer')
    result = question_bank.verify_answer(question, answer, user_answer)
    return jsonify({'result': result})

# quiz
@app.route('/get_quiz', methods=['POST'])
def get_quiz():
    data = request.json
    subject = data.get('subject')
    difficulty = data.get('level')
    question = data.get('questions')
    quiz_data = quiz_bank.get_quiz_data(subject, difficulty, question)
    return jsonify(quiz_data)

# magic search
@app.route('/search', methods=['POST'])
def search_files():
    data = request.json
    query = data.get('query')
    file_type = data.get('fileType')

    # Build the search query for Google
    file_extension = {
        "pdf": "filetype:pdf",
        "word": "filetype:doc OR filetype:docx",
        "number": "filetype:xls OR filetype:xlsx"
    }

    search_query = f"{query} {file_extension.get(file_type, '')}"

    # Perform Google search using `googlesearch` library
    search_results = search(search_query, num_results=10)

    # Return the results to the front-end
    return jsonify({"links": list(search_results)})

if __name__ == '__main__':
    app.run(debug=True)
    # app.debug = True  # Enable debug mode
    # logging.basicConfig(level=logging.INFO)  # Enable logging
    # serve(app, host="0.0.0.0", port=5000, threads=4) # if want to run it as script
