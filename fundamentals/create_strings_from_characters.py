# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest


# Frequencies
# 2 if we can create both strings without re-using characters
# 1 can create either string without re-using characters
# 0 if we cannot create either string without re-using characters
def create_strings_from_characters(frequencies, string1, string2):
    chart1 = {}
    chart2 = {}
    combined = {}
    for char in string1:
        chart1[char] = chart1.get(char, 0) + 1
        combined[char] = combined.get(char, 0) + 1

    for char in string2:
        chart2[char] = chart2.get(char, 0) + 1
        combined[char] = combined.get(char, 0) + 1

    if can_first_dict_support_second_dict(frequencies, combined):
        return 2
    elif can_first_dict_support_second_dict(
        frequencies, chart1
    ) or can_first_dict_support_second_dict(frequencies, chart2):
        return 1
    else:
        return 0


def can_first_dict_support_second_dict(dic1, dic2):
    for key, value in dic2.items():
        if value > dic1.get(key, 0):
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
        string1 = "hello"
        string2 = "world"
        expected = 1
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_2(self):
        frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
        string1 = "hello"
        string2 = "world"
        expected = 1
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_3(self):
        frequencies = {"a": 3, "b": 5, "c": 3, "d": 2, "e": 1}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 2
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_4(self):
        frequencies = {"a": 3, "b": 1, "c": 3, "d": 2, "e": 1}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 0
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_5(self):
        frequencies = {}
        string1 = "aaabbbc"
        string2 = "bbccde"
        expected = 0
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_6(self):
        frequencies = {}
        string1 = ""
        string2 = ""
        expected = 2
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )

    def test_case_7(self):
        frequencies = {"a": 1}
        string1 = ""
        string2 = ""
        expected = 2
        self.assertEqual(
            create_strings_from_characters(frequencies, string1, string2),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
