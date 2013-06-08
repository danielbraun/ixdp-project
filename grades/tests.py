from django.test import TestCase
from grades.models import Class
from datetime import time


class ClassTests(TestCase):

    def test_duration_in_minutes(self):
        c1 = Class.objects.create(start_time=time(8, 00), end_time=time(10, 00),
                                  course_id=2, week_day=2)
        self.assertEqual(c1.duration_in_minutes(), 120)
