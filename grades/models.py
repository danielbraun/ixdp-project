from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(_('name'), max_length=120, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Class(models.Model):
    DAYS_OF_THE_WEEK = (
        (1, _('Sunday')),
        (2, _('Monday')),
        (3, _('Tuesday')),
        (4, _('Wednesday')),
        (5, _('Thursday')),
        (6, _('Friday')),
    )

    course = models.ForeignKey('Course', verbose_name=_('course'))
    start_time = models.TimeField(_('Class Start Time'))
    end_time = models.TimeField(_('Class End Time'))
    week_day = models.PositiveIntegerField(_('Week Day'),
                                           choices=DAYS_OF_THE_WEEK)

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')

    def __unicode__(self):
        return u'%s - %s (%s-%s)' % (self.course, self.get_week_day_display(),
                                     self.start_time, self.end_time)


class ClassEvaluation(models.Model):
    related_class = models.ForeignKey('Class', verbose_name=_('Class'))
    grade = models.SmallIntegerField(_('Grade'),
                                     choices=[(i, i) for i in range(101)])
    student = models.ForeignKey(User, editable=False)

    class Meta:
        verbose_name = _('Class Evaluation')
        verbose_name_plural = _('Class Evaluations')
