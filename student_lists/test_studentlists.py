'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from .studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def common_add_many_students(self):
        common_class = ClassList(5)
        common_class.add_student('Test Student')
        common_class.add_student('Another Test Student')
        common_class.add_student('Yet Another Test Student')
        common_class.add_student('One More Test Student')
        common_class.add_student('Last Test Student')
        return common_class

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    def test_remove_student_not_in_list(self):
        test_class = self.common_add_many_students()
        with self.assertRaises(StudentError):
            test_class.remove_student('Unentered Student')

    def test_remove_student_not_in_empty_list(self):
        test_class = ClassList(0)
        with self.assertRaises(StudentError):
            test_class.remove_student('Should Be No Student')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_is_enrolled_student_not_enrolled(self):
        test_class = self.common_add_many_students()
        self.assertFalse(test_class.is_enrolled('Definitely Not Enrolled'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_no_students_in_list(self):
        test_class = ClassList(0)
        self.assertIsNone(test_class.index_of_student('Should Be No Student'))

    def test_index_of_missing_student_in_list(self):
        test_class = self.common_add_many_students()
        self.assertIsNone(test_class.index_of_student('Last Test Student JK'))

    def test_is_class_full(self):
        test_class = self.common_add_many_students()
        self.assertTrue(test_class.is_class_full())

    def test_is_class_full_empty(self):
        test_class = ClassList(0)
        self.assertTrue(test_class.is_class_full())

    def test_is_class_full_high_max(self):
        test_class = ClassList(1)
        self.assertFalse(test_class.is_class_full())
