from controll import db

class Vocabulary(db.Model):
    __table_args__=(CheckConstraint('vocab_phase >=0 AND vocab_phase <= 6', name='check_vocab_phase'),)#Ensure vocab_phase is between 0 and 6
    id = db.Column(db.Integer, primary_key=True)# Primary Key
    vocab_phase=db.Column(db.Integer,nullable=False,default=0)#Phase of the vocabulary word in the learning process default 0
    word_foreign = db.Column(db.String(100), unique=True, nullable=False)# Foreign word
    word_native = db.Column(db.String(200), nullable=False)# Native word
    word_synonyms = db.Column(db.String(200), nullable=True)# Synonyms of the native word
    word_tips = db.Column(db.String(200), nullable=True)# Tips for learning the word
    example_sentence = db.Column(db.String(300), nullable=True)# Example sentence using the foreign word
