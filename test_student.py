import unittest
from student import add_student, students


class TestStudent(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        student = add_student(
            "Rahul", "101", "rahul@example.com"
        )
        self.assertEqual(student["name"], "Rahul")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            add_student("", "101", "rahul@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            add_student("Rahul", "101", "invalid-email")


if __name__ == "__main__":
    unittest.main()
