from django.test import TestCase
from main_app.models import Lesson, Assignment, ClassFile
# Create your tests here.

class LessonTestCase(TestCase):
    def setUp(self):
        Lesson.objects.create(number=41, title="Impossible Lesson", date="2019-01-01")


    def test_lesson_title_shows(self):
        """Lessons that can be displayed by title will be displayed"""
        impossible = Lesson.objects.get(number=41)
        self.assertEqual(impossible.title, "Impossible Lesson")


class AssignmentTestCase(TestCase):
    def setUp(self):
        x = Lesson.objects.create(number=41, title="Impossible Lesson", date="2019-01-01")
        Assignment.objects.create(lesson_due=x, title="Test Lesson", points=50)


    def test_assignment_shows_points(self):
        """Assignment that can be displayed has correct point value"""
        first_assign = Assignment.objects.get(title="Test Lesson")
        self.assertEqual(first_assign.points, 50)



class ClassFileTestCase(TestCase):
    def setUp(self):
        x = Lesson.objects.create(number=41, title="Impossible Lesson", date="2019-01-01")
        ClassFile.objects.create(id=50, lesson_being_used=x,title="Test ClassFile")


    def test_classfile_shows_title(self):
        """ClassFiles display the proper title"""

        a_file = ClassFile.objects.get(id=50)
        self.assertEqual(a_file.title, "Test ClassFile")
