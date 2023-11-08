# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest


def get_n_longest_unique_words(words, n):
    # 1. Track occurence of words in a dict
    # 2. Put all single occurenes into a list
    # 3. Sort the list by len of strings
    # 4. Return the sorted list sliced by n
    tracker = {}
    data = []
    for word in words:
        tracker[word] = tracker.get(word, 0) + 1

    for word, value in tracker.items():
        if value > 1:
            continue
        else:
            data.append(word)

    data.sort(reverse=True, key=len)

    return data[:n]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
        n = 3
        expected = ["Whatever", "Ball", "Rock"]
        self.assertCountEqual(get_n_longest_unique_words(words, n), expected)

    def test_case_2(self):
        words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
        n = 1
        expected = [
            "Whatever",
        ]
        self.assertCountEqual(get_n_longest_unique_words(words, n), expected)

    def test_case_3(self):
        words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
        n = 0
        expected = []
        self.assertCountEqual(get_n_longest_unique_words(words, n), expected)

    def test_case_4(self):
        words = [
            "Hello",
            "AlgoExpert",
            "Algo",
            "Testing",
            "Programming",
            "Programming",
            "Coding",
            "Python",
            "JavaScript",
            "Coding",
            "Ruby",
        ]
        n = 5
        expected = ["AlgoExpert", "JavaScript", "Testing", "Python", "Hello"]
        self.assertCountEqual(get_n_longest_unique_words(words, n), expected)

    def test_case_5(self):
        words = ["Hello", "Hello", "Hello", "Abcd", "bcd", "a", "ab"]
        n = 2
        expected = ["Abcd", "bcd"]
        self.assertCountEqual(get_n_longest_unique_words(words, n), expected)


if __name__ == "__main__":
    unittest.main()
