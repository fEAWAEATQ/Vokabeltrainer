from logic.vocab_stats import get_vocab_stats
class DummyVocab:
    def __init__(self, phase):
        self.vocab_phase = phase
def test_get_vocab_stats():
    vocabularies = [
        DummyVocab(0),
        DummyVocab(1),
        DummyVocab(2),
        DummyVocab(2),
        DummyVocab(3),
        DummyVocab(6),
        DummyVocab(6),
        DummyVocab(6),
    ]
    stats = get_vocab_stats(vocabularies)
    assert stats["total_vocab"] == 8
    assert stats["learned_vocab"] == 3
    assert stats["phase_distribution"] == {
        0: 1,
        1: 1,
        2: 2,
        3: 1,
        4: 0,
        5: 0,
        6: 3,
    }