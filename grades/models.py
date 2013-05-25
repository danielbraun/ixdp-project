from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=120)


class Class(models.Model):
    DAYS_OF_THE_WEEK = (
        ('1', 'Sunday'),
        ('2', 'Monday'),
        ('3', 'Tuesday'),
        ('4', 'Wednesday'),
        ('5', 'Thursday'),
        ('6', 'Friday'),
    )

    course = models.ForeignKey('Course')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_day = models.PositiveIntegerField(choices=DAYS_OF_THE_WEEK)
    grade = models.SmallIntegerField(choices=[(i, i) for i in range(101)])
