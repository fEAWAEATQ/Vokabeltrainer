MAX_PHASE = 6
PHASE_FALLBACK = {
    0: 0,
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 3,
    6: 4,
}
def calculate_next_phase(current_phase: int, correct: bool) -> int:# Calculates the next vocab_phase based on the current phase and whether the answer was correct
    if correct:
        return min(MAX_PHASE, current_phase + 1)
    return PHASE_FALLBACK[current_phase]
