from flask import Blueprint
from flask import request, jsonify
from database.vocab import set_phase
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

