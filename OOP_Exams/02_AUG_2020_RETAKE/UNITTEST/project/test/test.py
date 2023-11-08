import unittest

from project.student_report_card import StudentReportCard


class TestStudentReportCard(unittest.TestCase):
    def setUp(self) -> None:
        self.test = StudentReportCard('TestName', 10)

    def test_proper_init(self):
        self.assertEqual('TestName', self.test.student_name)
        self.assertEqual(10, self.test.school_year)
        self.assertEqual({}, self.test.grades_by_subject)

    def test_student_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_range_1_to_12(self):
        for year in range(1, 13):
            self.test.school_year = year
            self.assertEqual(year, self.test.school_year)

    def test_school_year_less_than_1_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_more_than_12_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_subject_not_yet_in_subject_dict(self):
        self.test.add_grade('Math', 5)
        self.assertEqual({'Math': [5]}, self.test.grades_by_subject)

    def test_add_grade_subject_already_in_dict(self):
        self.test.add_grade('Math', 5)
        self.test.add_grade('Math', 4)
        self.assertEqual({'Math': [5, 4]}, self.test.grades_by_subject)

    def test_report_average_grade_for_each_subject_proper_output(self):
        self.test.add_grade('Math', 5)
        self.test.add_grade('Math', 4)
        self.test.add_grade('English', 4)
        self.test.add_grade('Biology', 6)
        self.test.add_grade('Biology', 5)
        self.test.add_grade('Biology', 2)
        self.assertEqual(3, len(self.test.grades_by_subject.keys()))
        self.assertEqual(6, sum(len(grade) for grade in self.test.grades_by_subject.values()))
        expected = "Math: 4.50\nEnglish: 4.00\nBiology: 4.33"
        actual = self.test.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_report_average_grade_for_each_subject_no_subjects(self):
        self.assertEqual('', self.test.average_grade_by_subject())

    def test_average_grade_for_all_subject_proper_result(self):
        self.test.add_grade('Math', 5)
        self.test.add_grade('Math', 4)
        self.test.add_grade('English', 4)
        self.test.add_grade('Biology', 6)
        self.test.add_grade('Biology', 5)
        self.test.add_grade('Biology', 2)
        expected = "Average Grade: 4.33"
        actual = self.test.average_grade_for_all_subjects()
        self.assertEqual(expected, actual)

    def test_repr_method(self):
        self.test.add_grade('Math', 5)
        self.test.add_grade('Math', 4)
        self.test.add_grade('English', 4)
        self.test.add_grade('Biology', 6)
        self.test.add_grade('Biology', 5)
        self.test.add_grade('Biology', 2)
        expected = "Name: TestName\nYear: 10\n----------\nMath: 4.50\nEnglish: 4.00\nBiology: 4.33\n----------\nAverage Grade: 4.33"
        self.assertEqual(expected, self.test.__repr__())


if __name__ == '__main__':
    unittest.main()
