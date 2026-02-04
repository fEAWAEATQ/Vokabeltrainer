from logic.vocab_phase import calculate_next_phase

def test_correct_answer_increases_phase():
    assert calculate_next_phase(0, True) == 1
    assert calculate_next_phase(3, True) == 4
def test_phase_does_not_exceed_max():
    assert calculate_next_phase(6, True) == 6
def test_wrong_answer_fallback():
    assert calculate_next_phase(0, False) == 0
    assert calculate_next_phase(1, False) == 0
    assert calculate_next_phase(2, False) == 1
    assert calculate_next_phase(3, False) == 1
    assert calculate_next_phase(4, False) == 2
    assert calculate_next_phase(5, False) == 3
    assert calculate_next_phase(6, False) == 4
def test_combined_scenarios():
    assert calculate_next_phase(2, True) == 3
    assert calculate_next_phase(3, False) == 1
    assert calculate_next_phase(1, True) == 2
    assert calculate_next_phase(2, False) == 1