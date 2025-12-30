from controller import db
def get_vocab(word_foreign): #Returns all Data from the Vocabulary with the fitting word_foreign
    return Vocabulary.query.filter_by(word_foreign=word_foreign).first()
def create_vocab(word_foreign,word_native,): #Inserts a new vocabulary word into the database
    try:
        vocab=Vocabulary(word_foreign=word_foreign,word_native=word_native,vocab_phase=0)
        db.session.add(vocab)
        db.session.commit()
        return vocab
    except IntegrityError:
        db.session.rollback()
        return None

