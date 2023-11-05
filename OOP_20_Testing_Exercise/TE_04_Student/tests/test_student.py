import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Student('Ivan')

    def test_proper_init_with_no_courses(self):
        self.assertEqual('Ivan', self.s.name)
        self.assertEqual({}, self.s.courses)

    def test_init_with_courses(self):
        s = Student('Ivan', {'math': [5, 6, 3]})
        self.assertEqual({'math': [5, 6, 3]}, s.courses)

    def test_enroll_new_course_with_notes(self):
        actual = self.s.enroll('math', [5, 6, 3])
        self.assertEqual({'math': [5, 6, 3]}, self.s.courses)
        self.assertEqual("Course and course notes have been added.", actual)

    def test_enroll_new_course_without_adding_notes(self):
        actual = self.s.enroll('math', [5, 6, 3], "N")
        self.assertEqual({'math': []}, self.s.courses)
        self.assertEqual("Course has been added.", actual)

    def test_enroll_with_course_already_added_to_update_notes(self):
        self.s.enroll('math', [5, 6, 3], "N")
        actual = self.s.enroll('math', [4, 4], "N")
        self.assertEqual({'math': [4, 4]}, self.s.courses)
        self.assertEqual("Course already added. Notes have been updated.", actual)

    def test_add_notes_add_note_of_existing_course(self):
        self.s.enroll('math', [], "N")
        actual = self.s.add_notes('math', 4)
        self.assertEqual({'math': [4]}, self.s.courses)
        self.assertEqual("Notes have been updated", actual)

    def test_add_notes_add_another_note_to_existing_course(self):
        self.s.enroll('math', [5], "Y")
        actual = self.s.add_notes('math', 4)
        self.assertEqual({'math': [5, 4]}, self.s.courses)
        self.assertEqual("Notes have been updated", actual)

    def test_add_notes_course_not_in_list_raises_exception(self):
        self.s.enroll('math', [], "N")
        with self.assertRaises(Exception) as ex:
            self.s.add_notes('biology', 5)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_raises_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.s.leave_course('biology')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_course_found(self):
        self.s.enroll('math', [], "N")
        actual = self.s.leave_course('math')
        self.assertEqual({}, self.s.courses)
        self.assertEqual("Course has been removed", actual)

if __name__ == '__main__':
    unittest.main()
