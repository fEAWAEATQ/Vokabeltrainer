from flask import Blueprint
from flask import request, jsonify
from database.vocab import set_phase, add_vocab
from database.lesson import get_vocabularies_of_lesson, add_lesson
vocab_routes = Blueprint('vocab_routes', __name__)  # Blueprint for vocab_routes

@vocab_routes.route('/vocab/answer', methods=['POST'])
def answer_vocab():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    word_foreign = data.get('word_foreign')
    username = data.get('username')
    lesson_name = data.get('lesson_name')
    correct = data.get('correct')
    if not all([word_foreign, username, lesson_name, isinstance(correct, bool)]):
        return jsonify({'error': 'Invalid input'}), 400
    vocab = set_phase(word_foreign=word_foreign, username=username, lesson_name=lesson_name, answer_bool=correct)
    if vocab is None:
        return jsonify({'error': 'Vocabulary word not found'}), 404
    return jsonify({"word_foreign": vocab.word_foreign, "new_phase": vocab.vocab_phase, "correct": correct}), 200

@vocab_routes.route('/users/<username>/lessons/<lesson_name>/vocab', methods=['GET'])
def get_lesson_vocab(username, lesson_name):
    vocabularies = get_vocabularies_of_lesson(lesson_name, username)
    return jsonify([{
        "word_foreign": vocab.word_foreign,
        "word_native": vocab.word_native,
        "vocab_phase": vocab.vocab_phase
    } for vocab in vocabularies]), 200

@vocab_routes.route('/users/<username>/lessons', methods=['POST'])
def create_lesson(username):
    data= request.get_json()
    if data is None:
        return jsonify({'error': 'No input data provided'}), 400
    lesson_name = data.get('lesson_name')
    if not lesson_name:
        return jsonify({'error': 'Invalid input'}), 400
    lesson=add_lesson(lesson_name, username)
    if lesson is None:
        return jsonify({'error': 'Lesson could not be created'}), 400
    return jsonify({"lesson_name": lesson.lesson_name, "user_id": lesson.user_id}), 201

@vocab_routes.route('/users/<username>/lessons/<lesson_name>/vocab', methods=['POST'])
def add_vocab_to_lesson(username, lesson_name):
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No input data provided'}), 400
    word_foreign = data.get('word_foreign')
    word_native = data.get('word_native')
    if not all([word_foreign, word_native]):
        return jsonify({'error': 'foreign and native words are required'}), 400
    vocab = add_vocab(word_foreign, word_native, username, lesson_name)
    if vocab is None:
        return jsonify({'error': 'Vocabulary could not be added'}), 400
    return jsonify({
        "word_foreign": vocab.word_foreign,
        "word_native": vocab.word_native,
        "phase": vocab.vocab_phase
    }), 201