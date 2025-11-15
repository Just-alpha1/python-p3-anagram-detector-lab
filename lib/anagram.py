class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)
        for candidate in candidates:
            if sorted_word == sorted(candidate.lower()):
                matches.append(candidate)
        return matches
