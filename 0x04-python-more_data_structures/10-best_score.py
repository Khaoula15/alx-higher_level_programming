#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_score = None
    best_key = None
    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            best_key = key
    return best_key
