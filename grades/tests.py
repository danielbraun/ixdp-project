from django.test import TestCase
from .models import Class
from .utils import normalize_grade
from datetime import time


def create_class():
    return Class.objects.create(start_time=time(9, 30),
                                end_time=time(11, 30),
                                course_id=2, week_day=2)


class ClassTests(TestCase):
    def setUp(self):
        self.c1 = create_class()

    def test_duration_in_minutes(self):
        self.assertEqual(self.c1.duration_in_minutes(), 120)

    def test_minutes_since_day_start(self):
        self.assertEqual(self.c1.minutes_since_day_start(), 90)


class UtilTests(TestCase):

    def test_normalize_grade(self):
        self.assertEqual(normalize_grade(100), 1)
        self.assertEqual(normalize_grade(60), 0)
        self.assertEqual(normalize_grade(80), 0.5)
