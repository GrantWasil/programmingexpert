
import unittest

class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100]")
        self._grade = grade
            
    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1
        sum = 0
        for student in students:
            sum += student.grade
        return sum / len(students)
    
    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)
    
    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None
        
        def get_grade_value(student):
            return student.grade

        return sorted(cls.all_students, reverse=True, key=get_grade_value)[0]

        
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        average_grade_without_students = Student.get_average_grade()
        self.assertEqual(average_grade_without_students, -1)
        self.assertEqual(Student.get_best_student(), None)

    def test_case_2(self):
        student1 = Student("Antoine", 75)
        average = Student.get_average_grade()
        best_student = Student.get_best_student()
        self.assertEqual(average, 75)
        self.assertEqual(best_student, student1)
        self.assertEqual("Antoine", best_student.name)

    def test_case_3(self):
        student2 = Student("Tim", 81)
        average = Student.get_average_grade()
        best_student = Student.get_best_student()
        self.assertEqual(average, 78)
        self.assertEqual(best_student, student2)
        self.assertEqual("Tim", best_student.name)

    def test_case_4(self):
        student3 = Student("Clement", 30)
        average = Student.get_average_grade()
        best_student = Student.get_best_student()
        self.assertEqual(average, 62)
        self.assertEqual("Tim", best_student.name)

    def test_case_5(self):
        best_student = Student.get_best_student()
        best_student.grade = best_student.grade - 10
        new_best_student = Student.get_best_student()
        self.assertEqual("Antoine", new_best_student.name)

    def test_case_6(self):
        best_student = Student.get_best_student()
        with self.assertRaises(ValueError):
            best_student.grade = 150

    def test_case_7(self):
        students = [
            Student("Simon", 55),
            Student("Alex", 69),
            Student("James", 8),
        ]
        self.assertEqual(44, Student.calculate_average_grade(students))


if __name__ == "__main__":
    unittest.main()
