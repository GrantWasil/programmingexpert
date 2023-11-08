import unittest


def sort_employees(employees, sort_by):
    sort_values = ["name", "age", "salary"]
    index = sort_values.index(sort_by)

    def get_sort_value(item: dict):
        return item[index]

    return sorted(employees, key=get_sort_value)


# This suite of tests is written to run against your code
# so that we can check its correctness.


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "age"
        expected = [
            ["Sarah", 24, 75000],
            ["Connor", 25, 110000],
            ["Jason", 26, 55000],
            ["Josie", 29, 100000],
            ["John", 33, 65000],
        ]
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_2(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "salary"
        expected = [
            ["Jason", 26, 55000],
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Connor", 25, 110000],
        ]
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_3(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "name"
        expected = [
            ["Connor", 25, 110000],
            ["Jason", 26, 55000],
            ["John", 33, 65000],
            ["Josie", 29, 100000],
            ["Sarah", 24, 75000],
        ]
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_4(self):
        employees = []
        sort_by = "salary"
        expected = []
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_5(self):
        employees = []
        sort_by = "name"
        expected = []
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_6(self):
        employees = []
        sort_by = "age"
        expected = []
        result = sort_employees(employees, sort_by)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
