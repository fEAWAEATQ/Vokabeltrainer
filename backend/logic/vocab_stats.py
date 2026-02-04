PHASE_COUNTER = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
def get_vocab_stats(vocabularies):# Returns statistics about the vocabulary phases
    stats = PHASE_COUNTER.copy()
    for vocab in vocabularies:
        if vocab.vocab_phase in stats:
            stats[vocab.vocab_phase] += 1
    return {
        "total_vocab": len(vocabularies),
        "learned_vocab": stats[6],
        "phase_distribution": stats
    }